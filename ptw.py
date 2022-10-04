# ptw.py - 'Put to Wall concept' logic and gui part
# Author: Tomasz Zgrys AiR, 2021/2022, WWSIS Horyzont
# Copyright: Tomasz Zgrys & WWSIS Horyzont


import time
from ui_PTW_gui import Ui_MainWindow
from PySide2.QtGui import QImage, QPixmap
from PySide2.QtWidgets import *
from PySide2.QtCore import QDate, QTime, QTimer, QFile, QIODevice
from database.dbo import *
from ptw_classes import *
from PySide2.QtSerialPort import *
import json
import barcode          #python-barcode
from barcode.writer import ImageWriter
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # self.setWindowFlag(Qt.FramelessWindowHint)  # then restore
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.first_run = True
        self.counter = 1

        # assigning gui fields to the variable of each compartment
        self.s_no_label = (self.ui.shelf_no_label_sh_1, self.ui.shelf_no_label_sh_2, self.ui.shelf_no_label_sh_3,
                           self.ui.shelf_no_label_sh_4, self.ui.shelf_no_label_sh_5, self.ui.shelf_no_label_sh_6,
                           self.ui.shelf_no_label_sh_7, self.ui.shelf_no_label_sh_8, self.ui.shelf_no_label_sh_9)
        self.s_progressBar = (
        self.ui.progressBar_sh_1, self.ui.progressBar_sh_2, self.ui.progressBar_sh_3, self.ui.progressBar_sh_4,
        self.ui.progressBar_sh_5, self.ui.progressBar_sh_6, self.ui.progressBar_sh_7, self.ui.progressBar_sh_8,
        self.ui.progressBar_sh_9)
        self.s_order_label = (
        self.ui.order_label_sh_1, self.ui.order_label_sh_2, self.ui.order_label_sh_3, self.ui.order_label_sh_4,
        self.ui.order_label_sh_5, self.ui.order_label_sh_6, self.ui.order_label_sh_7, self.ui.order_label_sh_8,
        self.ui.order_label_sh_9)
        self.s_qty_label = (
        self.ui.qty_label_sh_1, self.ui.qty_label_sh_2, self.ui.qty_label_sh_3, self.ui.qty_label_sh_4,
        self.ui.qty_label_sh_5, self.ui.qty_label_sh_6, self.ui.qty_label_sh_7, self.ui.qty_label_sh_8,
        self.ui.qty_label_sh_9)

        # batch initialization
        self.b = Batch()

        # Shelf initialization - 9 pcs
        self.s = [None] * 9
        for i in range(len(self.s)):
            self.s[i] = Shelf(i)
            self.s[i].shelf_no_label = self.s_no_label[i]
            self.s[i].shelf_no_progressbar = self.s_progressBar[i]
            self.s[i].shelf_no_order_label = self.s_order_label[i]
            self.s[i].shelf_qty_label = self.s_qty_label[i]

        self.stats = Statistics()

        if self.first_run == True:
            self.timer2 = QTimer(self)
            self.timer2.timeout.connect(self.ready)
            self.timer2.setInterval(1000)
            self.timer2.start()

        self.timer1 = QTimer(self)
        self.timer1.timeout.connect(lambda: self.lopi_model.update_flag())
        self.timer1.timeout.connect(lambda: self.lopi_tableview.doItemsLayout())
        self.timer1.timeout.connect(self.background_flag)
        self.timer1.timeout.connect(self.update_shelf_label_background)
        self.timer1.setInterval(500)

        self.ui.barcode_scan_lineEdit.setPlaceholderText('Scanning disabled')
        self.batch_br_list()
        self.ui.batch_br_tableView.selectionModel().selectionChanged.connect(self.batch_no_selection)

        self.ui.clear_status_br_pushButton.clicked.connect(self.clear_status_br_in_database)
        self.ui.register_br_pushButton.clicked.connect(self.handle_register_btn)
        self.ui.start_pushButton.clicked.connect(self.handle_scan_btn)

        self.combo_batch()
        self.combo_order()
        self.combo_item()
        self.combo_cart()

        self.locb_cb_list()
        self.dv_table_view()
        self.ui.locb_cb_tableView.selectionModel().selectionChanged.connect(self.dv_update_view)
        self.ui.cbfs_cb_pushButton.clicked.connect(lambda: self.dv_table_view('%'))
        self.ui.items_qty_pushButton.clicked.connect(self.show_items_qty)

        self.ui.add_item_cb_pushButton.clicked.connect(self.put_data_into_database)
        self.ui.add_item_cb_pushButton.clicked.connect(lambda: self.dv_update_view())
        self.ui.remove_batch_cb_pushButton.clicked.connect(lambda: self.remove_data_from_database('BATCH'))
        self.ui.remove_order_cb_pushButton.clicked.connect(lambda: self.remove_data_from_database('ORDER'))
        self.ui.remove_cart_cb_pushButton.clicked.connect(lambda: self.remove_data_from_database('CART'))
        self.ui.remove_row_cb_pushButton.clicked.connect(lambda: self.remove_data_from_database('ROW'))
        self.ui.clear_batch_status_cb_pushButton.clicked.connect(lambda: self.remove_data_from_database('STATUS_batch'))
        self.ui.clear_order_status_cb_pushButton.clicked.connect(lambda: self.remove_data_from_database('STATUS_order'))
        self.ui.clear_item_status_cb_pushButton.clicked.connect(lambda: self.remove_data_from_database('STATUS_item'))

        self.ui.barcode_scan_lineEdit.editingFinished.connect(lambda: self.get_barcode())
        self.uart = QSerialPort("/dev/ttyAMA0", baudRate=QSerialPort.Baud115200, readyRead=self.uart_read)

        self.ui.hboff_load_pushButton.clicked.connect(self.load_history)
        self.ui.hboff_clear_pushButton.clicked.connect(self.clear_hboff_textbrowser)
        self.ui.hboff_delete_pushButton.clicked.connect(self.delete_file)

        self.ui.bs_load_pushButton.clicked.connect(self.load_stats)
        self.ui.bs_present_pushButton.clicked.connect(self.present_stats)
        self.ui.bs_ll_pushButton.clicked.connect(self.last_loaded_stats)
        self.ui.bs_delete_pushButton.clicked.connect(self.delete_file)

    def ready(self):
        if self.first_run:
            self.ui.register_br_pushButton.setDisabled(True)
            self.uart_init()
            self.uart.open(QIODevice.ReadWrite)
            self.uart.setDataTerminalReady(True)
            self.send_data_to_wall('READY?', 9, None, None, None)

    def selftest(self):
        self.uart_init()
        self.uart.open(QIODevice.ReadWrite)
        self.uart.setDataTerminalReady(True)
        QTimer.singleShot(700, lambda: self.send_data_to_wall('SELFTEST', 9, None, None, None))

    def tb_counter(self):
        self.counter += 1

    def background_flag(self):
        self.b.background_flag = not self.b.background_flag

    def handle_register_btn(self):
        if self.ui.batch_no_br_label.text() != '' and self.ui.register_br_pushButton.isChecked() and self.get_br_batch_no():
            self.ui.shelf_textBrowser.clear()
            self.b.batch_no = self.ui.batch_no_br_label.text()
            self.b.orders_qty = self.ui.orders_qty_br_label.text()
            self.b.carts_qty = self.ui.carts_qty_br_label.text()
            self.b.items_qty = self.ui.items_qty_br_label.text()
            self.ui.batch_no_label.setText(self.b.batch_no)
            self.ui.orders_qty_label.setText(self.b.orders_qty)
            self.ui.carts_qty_label.setText(self.b.carts_qty)
            self.update_counters()  # items and orders left
            self.ui.register_br_pushButton.setChecked(True)
            self.ui.register_br_pushButton.setText('REGISTERING\nIN WALL')
            # self.display_message('Batch no <strong>' + str(self.b.batch_no) + '</strong> registered')

            self.uart.open(QIODevice.ReadWrite)
            self.uart_init()
            if self.b.batch_no != None:
                self.send_data_to_wall('U', 9, self.b.batch_no, None, None)


        else:
            if itemsLeft(self, self.b.batch_no):
                if self.show_message_box('warning',
                                         "WARNING , please read carefully !!!",
                                         "Batch already registered!\n"
                                         "Do you really want to unregister existed Batch????\n"
                                         "All progress will be lost!!!") is True:
                    self.display_message('<strong> Batch scanning interrupted !!!', 'red', 28)
                    # sending information about the deregistration to the order picking wall
                    if self.b.batch_no is not None:
                        self.send_unregister_to_wall()
                else:
                    self.ui.register_br_pushButton.setChecked(True)
            else:
                if self.b.batch_no is not None:
                    self.send_unregister_to_wall()

    def send_unregister_to_wall(self):
        self.ui.register_br_pushButton.setText('UNREGISTERING\nIN WALL')
        self.ui.register_br_pushButton.setChecked(False)
        self.uart.open(QIODevice.ReadWrite)
        self.send_data_to_wall('UNREGISTER', 9, self.b.batch_no, None, None)

    def register(self):
        self.b.start_time = QDateTime.currentDateTime().toTime_t()
        self.b.batch_stats.update({self.b.batch_no: [self.b.start_time, self.b.end_time, int(self.b.orders_qty),
                                                     self.b.items_in_carts, int(self.b.items_qty),
                                                     int(self.b.progress)]})

        self.lopi_table_qm()
        self.ui.register_br_pushButton.setChecked(True)
        self.ui.register_br_pushButton.setText('UNREGISTER')
        self.timer1.start()
        self.ui.clear_status_br_pushButton.setDisabled(True)
        self.ui.scanning_groupBox.setDisabled(False)
        self.ui.start_pushButton.setDisabled(False)
        self.ui.start_pushButton.setChecked(False)
        self.ui.start_pushButton.setStyleSheet('''
                                        background-color:qlineargradient(spread:pad, x1:0.503, y1:0, x2:0.513, y2:1, 
                                        stop:0.120192 rgba(36, 126, 0, 255), stop:1 rgba(0, 229, 33, 246));
                                        border-radius:15px;
                                        color: white;
                                        ''')
        self.ui.bs_filename_label.setText('Present Batch')
        self.display_statistics(self.b.batch_stats)

    def unregister(self):
        self.timer1.stop()  # stopping the timer, which causes the background blinking of rows and numbers of compartments
        # self.display_message('Batch no <b>' + str(self.b.batch_no) + '</b> unregistered')
        # clearing fields that display Batch data
        self.ui.batch_no_br_label.setText('')
        self.ui.orders_qty_br_label.setText('')
        self.ui.carts_qty_br_label.setText('')
        self.ui.items_qty_br_label.setText('')
        self.ui.items_left_label.setText('')
        self.ui.orders_left_label.setText('')
        self.ui.batch_no_label.setText('')
        self.ui.orders_qty_label.setText('')
        self.ui.carts_qty_label.setText('')

        # restore the state of the REGISTER button
        self.ui.clear_status_br_pushButton.setDisabled(False)

        self.b.end_time = QDateTime.currentDateTime().toTime_t()  # writing the end time to a variable
        self.time_difference = self.b.end_time - self.b.start_time  # time difference calculation
        self.b.batch_stats.update({self.b.batch_no: [self.b.start_time, self.b.end_time, int(self.b.orders_qty),
                                                     self.b.items_in_carts, int(self.b.items_qty),
                                                     int(self.b.progress)]})
        # self.stats.present_stats = self.b.batch_stats.copy()
        # self.stats.present_stats.update(self.b.orders_stats)

        for shelf_no in self.b.shelf_label_background.keys():
            self.b.shelf_label_background.update({shelf_no: 0})
        self.update_shelf_label_background()
        # saving files: history and statistics
        self.save_file('ptwh')
        self.save_file('ptws')
        # initialization of the Batch class and initialization of compartments in the Shelf class
        self.b.batch_init()
        self.update_progressbar_value()
        for i in range(len(self.s)):
            self.s[i].shelf_init()
            self.s[i].shelf_no_progressbar.setValue(0)
            self.s[i].shelf_no_order_label.setText('')
            self.s[i].shelf_qty_label.setText('')
        # setting the REGISTER button and deactivation of START / STOP scanning and the barcode input line
        self.ui.register_br_pushButton.setText('REGISTER')
        self.ui.register_br_pushButton.setChecked(False)
        self.ui.start_pushButton.setChecked(False)
        self.ui.scanning_groupBox.setDisabled(True)
        self.ui.start_pushButton.setDisabled(True)
        self.ui.start_pushButton.setStyleSheet('''             
                        background-image:url(:/glossy_buttons/glossy_button.png);
                        background-position: center center;
                        border-radius:15px;
                        color: white;
                        ''')
        self.ui.message_frame.setDisabled(True)
        self.ui.shelf_textBrowser.clear()
        self.ui.bs_filename_label.setText('Batch unregistered')
        # clearing of lopi - list of processed items
        try:
            self.lopi_model.setQuery("")
            self.ui.lopi_tableView.setModel(self.lopi_model)
            self.ui.lopi_tableView.update()
            self.lopi_tableview.doItemsLayout()
        except:
            pass

    def handle_scan_btn(self):

        if self.ui.start_pushButton.isChecked() and self.b.batch_no == self.ui.batch_no_label.text():
            self.ui.start_pushButton.setText('STOP\n\nSCANNING ')
            self.ui.start_pushButton.setStyleSheet('''
                background-color:qlineargradient(spread:pad, x1: 0.522, y1: 0.999682, x2: 0.499, y2: 0.00568182, 
                stop: 0.120192 rgba(255, 0, 0, 255), stop: 1 rgba(255, 0, 0, 255));
                border-radius:15px;
                color: white;
                ''')
            self.ui.start_pushButton.setChecked(True)
            self.ui.barcode_scan_lineEdit.setEnabled(True)
            self.ui.barcode_scan_lineEdit.setPlaceholderText('Scanning enabled')
            self.ui.batch_frame.setEnabled(True)
            self.ui.message_frame.setEnabled(True)
            self.ui.groupBox_shelf.setEnabled(True)
            self.ui.register_br_pushButton.setDisabled(True)
            self.display_message('Start scanning', font_size=14)
            QTimer.singleShot(800, lambda: self.ui.barcode_scan_lineEdit.setFocus())
            self.item_barcode = ''
        else:

            self.ui.start_pushButton.setChecked(False)
            self.ui.start_pushButton.setStyleSheet('''
                background-color:qlineargradient(spread:pad, x1:0.503, y1:0, x2:0.513, y2:1, 
                stop:0.120192 rgba(36, 126, 0, 255), stop:1 rgba(0, 229, 33, 246));
                border-radius:15px;
                color: white;
                ''')

            self.ui.register_br_pushButton.setDisabled(False)
            self.ui.barcode_scan_lineEdit.setEnabled(False)
            self.ui.barcode_scan_lineEdit.setPlaceholderText('Scanning disabled')
            self.ui.batch_frame.setEnabled(False)
            self.ui.groupBox_shelf.setEnabled(False)
            self.display_message('Scanning stopped', font_size=14)
            self.ui.start_pushButton.setText('START\n\nSCANNING')
            self.ui.barcode_label.setPixmap(None)
            self.item_barcode = ''

    def get_barcode(self):

        if self.b.waiting_front_conf is None:
            if self.ui.barcode_scan_lineEdit.text():
                self.item_barcode = self.ui.barcode_scan_lineEdit.text()
                bar_code = barcode.get('code128', self.item_barcode, writer=ImageWriter())
                filename = bar_code.save('code128')
                image_profile = QImage('code128.png')  # QImage object
                image_profile = image_profile.scaled(285, 250, aspectRatioMode=Qt.KeepAspectRatio,
                                                     transformMode=Qt.SmoothTransformation)  # To scale image for example and keep its aspect ratio
                self.ui.barcode_label.setPixmap(QPixmap.fromImage(image_profile))
                QTimer.singleShot(50, lambda: self.find_item_in_database())
        else:
            self.display_message('Please first confirm Item in Shelf no: <strong>' + str(self.b.waiting_front_conf + 1),
                                 'orange', font_size=15)
            self.send_data_to_wall("BLIP", 9, 1, 700, 2)
        QTimer.singleShot(700, lambda: self.ui.barcode_scan_lineEdit.setText(''))

    def check_shelves(self):
        self.b.empty_shelves.clear()
        self.b.orders_in_shelves.clear()
        for i in range(len(self.s)):
            if self.s[i].order_no and not self.s[i].shelf_empty:
                if self.s[i].order_no not in self.b.orders_in_shelves:
                    self.b.orders_in_shelves.append(self.s[i].order_no)
            else:
                self.b.empty_shelves.append(i)

    def update_progressbar_value(self, type=None, number=None):
        if type is None and number is None:
            if int(self.b.items_qty) > 0:
                self.b.progress = (1 - (
                            int(itemsLeft(self, self.b.batch_no)) + int(ordersLeft(self, self.b.batch_no))) / (
                                               int(self.b.items_qty) + int(self.b.orders_qty))) * 100
                self.ui.progressBar_batch.setValue(self.b.progress)
            else:
                self.ui.progressBar_batch.setValue(0)
        else:
            if self.s[number].items_qty > 0:
                self.s[number].progress = (len(self.s[number].item_mt_id) / self.s[number].items_qty) * 100
                self.s[number].shelf_no_progressbar.setValue(self.s[number].progress)
            else:
                self.s[number].shelf_no_progressbar.setValue(0)

    def update_shelf_label_background(self):
        if (len(self.b.shelf_label_background)):
            for shelf_no, status in self.b.shelf_label_background.items():
                if status == 1:
                    if self.b.background_flag:
                        self.s[shelf_no].shelf_no_label.setStyleSheet('background-color: #FF6600;color: white')
                    else:
                        self.s[shelf_no].shelf_no_label.setStyleSheet('background-color: #464646;color: white')
                elif status == 2:
                    self.s[shelf_no].shelf_no_label.setStyleSheet('background-color: #FF0000;color: white')
                elif status == 3:
                    if self.b.background_flag:
                        self.s[shelf_no].shelf_no_label.setStyleSheet('background-color: #00AA00;color: white')
                    else:
                        self.s[shelf_no].shelf_no_label.setStyleSheet('background-color: #464646;color: white')
                elif status == 4:
                    self.s[shelf_no].shelf_no_label.setStyleSheet('background-color: #006600;color: white')
                elif status == 5:
                    self.s[shelf_no].shelf_no_label.setStyleSheet('background-color: #000066;color: white')
                else:
                    self.s[shelf_no].shelf_no_label.setStyleSheet('background-color: #464646;color: white')

    def process_data_from_wall(self):
        print(self.update_list)
        if len(self.update_list) > 0:
            for data in self.update_list:
                message_type = data[0]
                object_type = data[1]
                shelf_no = int(data[2])
                id_number = data[3]
                command = data[4]
                len_data = len(data)
                if message_type == 'C':
                    if object_type == 'S':
                        if command == 'BFP' and self.s[shelf_no].waiting_front_conf is True and self.b.waiting_front_conf == shelf_no:
                            self.s[shelf_no].waiting_front_conf = False
                            self.b.waiting_front_conf = None
                            self.update_shelf(2, shelf_no, self.s[shelf_no].order_no, '%',
                                              self.s[shelf_no].item_mt_id[-1])
                        elif command == 'SFD':
                            if self.s[shelf_no].items_qty == len(self.s[shelf_no].item_mt_id):
                                self.update_shelf(3, shelf_no, self.s[shelf_no].order_no, '%', '%')
                                self.s[shelf_no].waiting_back_conf = True
                                self.s[shelf_no].shelf_full = True
                        elif command == 'BBP':
                            if self.s[shelf_no].shelf_full and self.s[shelf_no].items_qty == len(
                                    self.s[shelf_no].item_mt_id) and self.s[shelf_no].waiting_back_conf:
                                self.update_shelf(4, shelf_no, self.s[shelf_no].order_no, '%', '%')

                                print('batch stats w process from wall:  ', self.b.batch_stats)
                                print('bbp  -  b.orders in shelves after remove:  ', self.b.orders_in_shelves)
                    elif object_type == 'B' and shelf_no == 9:
                        if command == 'BA':
                            self.display_message('<strong>Batch no: ' + str(self.b.batch_no) + ' properly registered',
                                                 '#ff0040', 16)
                            self.register()
                        elif command == 'BATCH FINISHED' and id_number == self.b.batch_no:
                            self.check_batch()


                elif message_type == 'SELFTEST':
                    if command == 'IN PROGRESS':
                        self.display_message(
                            '<strong>First run. SELFTEST in progress. Wall is initializing. Please wait...', 'orange',
                            16)
                    elif command == 'FINISHED':
                        self.display_message('<strong> Test done. The wall is ready to work.', 'green', 16)
                        self.ui.register_br_pushButton.setDisabled(False)
                elif message_type == 'UNREGISTER':
                    if command == 'BATCH UNREGISTERED' and id_number == self.b.batch_no:
                        self.display_message(
                            '<strong> Batch no: ' + str(self.b.batch_no) + ' successfully checked out from the wall.',
                            'blueviolet', 16)  # '#ff0040'
                        self.unregister()
                    else:
                        self.display_message(
                            '<strong>Unregistering failed. Please try again. In wall is registered Batch no: ' + str(
                                self.b.batch_no), 'tomato', 16)

                elif message_type == 'READY':
                    if command == 'SELFTEST?':
                        self.timer2.stop()
                        self.first_run = False
                        self.selftest()

                if len(self.update_list):
                    self.update_list.remove(data)

    def update_shelf(self, status, shelf_no, order_no, item_barcode, mt_id):

        if self.s[shelf_no].order_no is None:
            self.s[shelf_no].order_no = order_no
            self.s[shelf_no].shelf_empty = False
            self.s[shelf_no].shelf_no_order_label.setText(order_no)
            self.s[shelf_no].start_time = QDateTime.currentDateTime().toTime_t()

        if not self.s[shelf_no].items_qty:
            self.check_item_query = ""
            self.check_item_query = check_item_in_DB(self, 'full_list', self.b.batch_no, order_no, '%', None, None,
                                                     None, None, '%')
            self.s[shelf_no].items_qty = query_num_rows(self, self.check_item_query)

        if status == 1:
            self.s[shelf_no].waiting_front_conf = True
            self.b.waiting_front_conf = shelf_no
            self.s[shelf_no].item_mt_id.append(mt_id)
            self.s[shelf_no].item_no = len(self.s[shelf_no].item_mt_id)
            self.s[shelf_no].shelf_qty_label.setText(
                str(self.s[shelf_no].item_no - 1) + ' of ' + str(self.s[shelf_no].items_qty))
            self.send_data_to_wall('U', shelf_no, self.s[shelf_no].order_no, None, None)
            change_data_in_DB(self, mt_id, self.b.batch_no, order_no, item_barcode, shelf_no + 1, status,
                              self.s[shelf_no].item_no, (
                                          QTime.currentTime().toString() + ' ' + QDate.currentDate().toString(
                                      Qt.DefaultLocaleShortDate)))

        elif status == 2:
            self.s[shelf_no].shelf_qty_label.setText(
                str(self.s[shelf_no].item_no) + ' of ' + str(self.s[shelf_no].items_qty))
            self.update_progressbar_value('s', shelf_no)
            self.update_progressbar_value()
            self.s[shelf_no].waiting_front_conf = False
            change_data_in_DB(self, mt_id, self.b.batch_no, order_no, '%', shelf_no + 1, status, '%', '%')
            self.display_message('Item in Shelf no: ' + str(shelf_no + 1) + ' confirmed')

        elif status == 3:
            change_data_in_DB(self, '%', self.b.batch_no, order_no, '%', '%', status, '%', '%')
            self.display_message('Order no: <strong>' + str(order_no) + '</strong> in Shelf no: <strong>' + str(
                shelf_no + 1) + '</strong> completed. Waiting for confirmation in wall.', 'lawngreen', 14)

        elif status == 4:
            change_data_in_DB(self, '%', self.b.batch_no, order_no, '%', '%', status, '%', '%')
            self.display_message('Order no: <strong>' + str(
                order_no) + '</strong> finished. Items picked up from Shelf no: <strong>' + str(shelf_no + 1),
                                 '#00AA00', 14)
            self.s[shelf_no].end_time = QDateTime.currentDateTime().toTime_t()
            print('bbp  -  b.orders in shelves:  ', self.b.orders_in_shelves)
            if self.b.orders_in_shelves.count(self.s[shelf_no].order_no):
                self.b.orders_in_shelves.remove(self.s[shelf_no].order_no)
            self.b.batch_stats.update({self.s[shelf_no].order_no: [shelf_no + 1, self.s[shelf_no].start_time,
                                                                   self.s[shelf_no].end_time,
                                                                   self.s[shelf_no].item_mt_id]})
            # Shelf (compartment) intitialization
            self.s[shelf_no].shelf_init()
            self.s[shelf_no].shelf_qty_label.setText('')
            self.s[shelf_no].shelf_no_order_label.setText('')
            self.update_progressbar_value('s', shelf_no)
            self.update_progressbar_value()
            if int(self.ui.orders_left_label.text()) != 0:
                self.display_message('Shelf no: ' + str(shelf_no + 1) + ' cleared. Ready for next order :)',
                                     'deepskyblue')

        self.check_item_query = ""

        if status > 3:
            self.b.shelf_label_background.update({shelf_no: 0})
        else:
            self.b.shelf_label_background.update({shelf_no: status})

        self.lopi_table_qm()
        self.content_batch_query(self.b.batch_no)
        self.update_counters()
        self.update_progressbar_value()
        self.b.batch_stats.update({self.b.batch_no: [self.b.start_time, self.b.end_time, int(self.b.orders_qty),
                                                     self.b.items_in_carts, int(self.b.items_qty),
                                                     int(self.b.progress)]})
        if self.ui.bs_filename_label.text() == ('Present Batch' or 'Batch finished'):
            self.display_statistics(self.b.batch_stats)

    def check_batch(self):
        if int(self.ui.orders_left_label.text()) == 0:
            self.display_message('Batch completed. Please unregister Batch', 'coral', 18)
            self.ui.bs_filename_label.setText('Batch finished')
            self.ui.start_pushButton.setChecked(False)
            self.handle_scan_btn()

    def find_item_in_database(self):
        self.check_item_query = ""
        self.check_item_query = check_item_in_DB(self, 'only_status', self.b.batch_no, '%', self.item_barcode, None,
                                                 'is Null', None, None, '%')
        __numRows = query_num_rows(self, self.check_item_query)
        self.check_shelves()

        if self.check_item_query.isSelect() and self.check_item_query.isActive() and __numRows > 0:
            self.check_item_query.first()
            if self.check_item_query.value('Shelf_no') != '' and int(self.check_item_query.value('Shelf_no')) >= 0:
                self.update_shelf(1, self.check_item_query.value('Shelf_no') - 1,
                                  self.check_item_query.value('Order_no'), self.check_item_query.value('Item_barcode'),
                                  self.check_item_query.value('PTW_mt_Id'))
            elif len(self.b.empty_shelves):
                change_data_in_DB(self, '%', self.b.batch_no, self.check_item_query.value('Order_no'), '%',
                                  self.b.empty_shelves[0] + 1, None, None, None)
                self.update_shelf(1, self.b.empty_shelves[0], self.check_item_query.value('Order_no'),
                                  self.check_item_query.value('Item_barcode'), self.check_item_query.value('PTW_mt_Id'))
            else:
                self.display_message(
                    '<b>Shelves in wall are full!!!</b> Please try to scan another item to finish previous orders and free some shelf!',
                    'orange', 15)
                self.send_data_to_wall("BLIP", 9, 3, 200, 30)
        else:
            self.check_item_query = check_item_in_DB(self, 'only_status', self.b.batch_no, '%', self.item_barcode, None,
                                                     "like '%'", None, None, '%')

            if query_num_rows(self, self.check_item_query) > 0:
                self.display_message('Item already processed. No more such items in Batch !!!', 'orange', 15)
                self.send_data_to_wall("BLIP", 9, 5, 300, 20)
            else:
                self.display_message(
                    'There is no such element in the batch or the barcode is damaged. Try to scan again.', 'orange', 15)
                self.send_data_to_wall("BLIP", 9, 9, 100, 10)
            self.check_item_query = ""

    def locb_cb_list(self):
        self.locb_model = QSqlQueryModel()
        self.locb = self.ui.locb_cb_tableView
        self.locb_model.setQuery(batch_query_distinct_list(self))
        self.locb.setModel(self.locb_model)
        self.locb.horizontalHeader().hide()
        self.locb.setSelectionBehavior(QTableView.SelectItems)
        self.locb.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def get_locb_batch_no(self):

        num_rows = self.locb_model.rowCount()
        if num_rows > 0:
            try:
                batch_locb_no = self.ui.locb_cb_tableView.currentIndex().siblingAtColumn(0).data()

                if batch_locb_no:
                    return batch_locb_no
                else:
                    return '%'
            except:
                return "'%'"
        else:
            return False

    def dv_update_view(self):
        locb_batch_no = self.get_locb_batch_no()
        self.dv_table_view(locb_batch_no)

    def dv_table_view(self, batch_no='%'):
        self.dv = self.ui.dv_cb_tableView
        self.dvmodel = dv_table_model(self, batch_no)
        self.dv.setModel(self.dvmodel)
        self.dv.hideColumn(6)  # hidden column with record id
        self.dv.setSelectionBehavior(QTableView.SelectRows)
        self.dv.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.dv.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def show_items_qty(self):

        self.dvmodel.setQuery(showItemQty(self, self.get_locb_batch_no()))
        self.dv.setModel(self.dvmodel)
        self.dvmodel.sort(0, Qt.AscendingOrder)
        self.dv.setSortingEnabled(True)

    def batch_br_list(self):
        self.batch_br_model = QSqlQueryModel()
        self.batch_br = self.ui.batch_br_tableView
        self.batch_br_model.setQuery(batch_query_distinct_list(self))

        self.batch_br.setModel(self.batch_br_model)
        self.batch_br.selectionModel().selectedRows()
        self.batch_br.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.batch_br.horizontalHeader().hide()

    def get_br_batch_no(self):

        num_rows = self.batch_br_model.rowCount()

        if num_rows > 0:
            try:
                batch_br_no = self.ui.batch_br_tableView.currentIndex().siblingAtColumn(0).data()
                if batch_br_no:
                    return batch_br_no
                else:
                    return '%'
            except:
                return '%'
        else:
            return '%'

    def batch_no_selection(self):

        br_batch_no = self.get_br_batch_no()
        if br_batch_no:
            if not self.ui.register_br_pushButton.isChecked():
                self.ui.batch_no_br_label.setText(str(br_batch_no))
                self.b.items_in_carts = cartItemsCount(self, br_batch_no)
                self.br_cart_qty = len(self.b.items_in_carts)
                self.br_order_qty = orderCount(self, br_batch_no)
                self.br_item_qty = itemCount(self, br_batch_no)
                self.ui.items_qty_br_label.setText(str(self.br_item_qty))
                self.ui.orders_qty_br_label.setText(str(self.br_order_qty))
                self.ui.carts_qty_br_label.setText((str(self.br_cart_qty)))
            self.content_batch_query(br_batch_no)
        else:
            self.content_batch_query('%')

    def content_batch_query(self, batch_no):
        self.batch_content_view = self.ui.content_br_tableView
        self.ucb_model = content_batch_query(self, batch_no)
        self.batch_content_view.setModel(self.ucb_model)
        self.batch_content_view.hideColumn(0)
        self.batch_content_view.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.batch_content_view.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # self.batch_content_view.resizeColumnsToContents()

    def lopi_table_qm(self):
        if self.b.batch_no:
            self.lopi_model = lopiModel(self.b.batch_no)
        else:
            if self.get_br_batch_no():
                self.lopi_model = lopiModel(self.get_br_batch_no())
            else:
                self.lopi_model = lopiModel('%')
        self.lopi_tableview = self.ui.lopi_tableView
        self.lopi_tableview.setModel(self.lopi_model)

        self.lopi_tableview.hideColumn(8)  # hide status column in lopi
        self.lopi_tableview.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.lopi_tableview.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.batch_content_view.resizeColumnsToContents()

    def combo_batch(self):
        self.combo = self.ui.batch_no_comboBox
        self.model_batch = combo_model(self, 'Batch')
        self.combo.setModel(self.model_batch)
        self.combo.setModelColumn(self.model_batch.fieldIndex('Batch_no'))

    def combo_order(self):
        self.combo = self.ui.order_no_comboBox
        self.model_order = combo_model(self, 'Orders')
        self.combo.setModel(self.model_order)
        self.combo.setModelColumn(self.model_order.fieldIndex('Order_no'))

    def combo_item(self):
        self.combo = self.ui.item_no_comboBox
        self.model_item = combo_model(self, 'Item')
        self.combo.setModel(self.model_item)
        self.combo.setModelColumn(self.model_item.fieldIndex('Item_barcode'))

    def combo_cart(self):
        self.combo = self.ui.cart_barcode_comboBox
        self.model_cart = combo_model(self, 'Cart')
        self.combo.setModel(self.model_cart)
        self.combo.setModelColumn(self.model_cart.fieldIndex('Cart_barcode'))

    def selected_row_dv_table_data(self):
        batch = self.ui.dv_cb_tableView.currentIndex().siblingAtColumn(0).data()
        order = self.ui.dv_cb_tableView.currentIndex().siblingAtColumn(1).data()
        item = self.ui.dv_cb_tableView.currentIndex().siblingAtColumn(2).data()
        cart = self.ui.dv_cb_tableView.currentIndex().siblingAtColumn(4).data()
        mt_id = self.ui.dv_cb_tableView.currentIndex().siblingAtColumn(6).data()

        return batch, order, item, cart, mt_id

    def put_data_into_database(self):

        batch = self.ui.batch_no_comboBox.currentText()
        order = self.ui.order_no_comboBox.currentText()
        item = self.ui.item_no_comboBox.currentText()
        cart = self.ui.cart_barcode_comboBox.currentText()
        add_row_into_DB(self, batch, order, item, cart)

        row_idx = self.ui.locb_cb_tableView.currentIndex().row()
        self.locb_model.setQuery(batch_query_distinct_list(self))
        self.batch_br_model.setQuery(batch_query_distinct_list(self))
        self.locb.update()
        self.batch_br.update()
        self.locb.doItemsLayout()
        self.batch_br.doItemsLayout()
        self.locb.selectRow(row_idx)
        self.dv_update_view()

    def clear_status_br_in_database(self):

        batch_br_idx = self.ui.batch_br_tableView.selectedIndexes()[0]
        if batch_br_idx:
            br_batch_no = self.ui.batch_br_tableView.model().data(batch_br_idx)
            if not self.ui.register_br_pushButton.isChecked():
                change_data_in_DB(self, '%', br_batch_no, '%', '%', None, None, None, None)
                self.batch_br_model.layoutChanged.emit()
            self.content_batch_query(br_batch_no)

    def remove_data_from_database(self, op_type):
        data = self.selected_row_dv_table_data()
        batch_locb = self.get_locb_batch_no()
        if batch_locb and batch_locb != '%':
            batch_no = batch_locb
        else:
            batch_no = data[0]

        order_no = data[1]
        item_barcode = data[2]
        cart_barcode = data[3]
        mt_id = str(data[4])
        print(batch_no, order_no, item_barcode, cart_barcode, mt_id)
        if op_type == 'BATCH':
            remove_data_from_DB(self, '%', batch_no, '%', '%', '%')
        elif op_type == "ORDER":
            remove_data_from_DB(self, '%', batch_no, order_no, '%', '%')
        elif op_type == "CART":
            remove_data_from_DB(self, '%', batch_no, '%', '%', cart_barcode)
        elif op_type == "ROW":
            remove_data_from_DB(self, mt_id, batch_no, order_no, item_barcode, cart_barcode)
        elif op_type == 'STATUS_batch':
            change_data_in_DB(self, '%', batch_no, '%', '%', None, None, None, None)
        elif op_type == 'STATUS_order':
            change_data_in_DB(self, '%', batch_no, order_no, '%', None, None, None, None)
        elif op_type == 'STATUS_item':
            change_data_in_DB(self, mt_id, batch_no, order_no, item_barcode, None, None, None, None)
        row_idx = self.ui.locb_cb_tableView.currentIndex().row()
        self.locb_model.setQuery(batch_query_distinct_list(self))
        self.batch_br_model.setQuery(batch_query_distinct_list(self))
        self.locb.update()
        self.batch_br.update()
        self.locb.doItemsLayout()
        self.batch_br.doItemsLayout()
        self.locb.selectRow(row_idx)
        self.dv_update_view()

    def display_message(self, text_to_show, text_color='LightGrey', font_size=14):
        text_to_display = '<html style="font-size:11px;">' + str(self.counter) + '. ' + QDate.currentDate().toString(
            Qt.DefaultLocaleShortDate) + ' ' + QTime.currentTime().toString() + '</html> - <html style="color:' + str(
            text_color) + ';font-size:' + str(font_size) + 'px;">' + str(text_to_show) + '<\html'
        self.ui.shelf_textBrowser.append(text_to_display)
        self.ui.pbo_textBrowser.append(text_to_display)
        self.tb_counter()

    def update_counters(self):
        self.ui.items_left_label.setText(str(itemsLeft(self, self.b.batch_no)))
        self.ui.orders_left_label.setText(str(ordersLeft(self, self.b.batch_no)))

    def send_data_to_wall(self, mess_type, shelf_no, id_number, command1, command2):
        tx_data = ''
        object_type = ''
        if shelf_no < 9:
            object_type = 'S'
        else:
            object_type = 'B'
            shelf_no = 9
        if (command1 and command2) is None:
            if shelf_no < 9:
                tx_data = str(mess_type) + '#' + str(object_type) + '#' + str(shelf_no) + '#' + str(
                    id_number) + '#' + str(len(self.s[shelf_no].item_mt_id)) + '#' + str(self.s[shelf_no].items_qty)
            else:
                tx_data = str(mess_type) + '#' + str(object_type) + '#' + str(shelf_no) + '#' + str(
                    id_number) + '#' + str(self.b.orders_qty) + '#' + str(self.b.carts_qty)
        else:
            if command2 == None:
                tx_data = mess_type + '#' + object_type + '#' + str(shelf_no) + '#' + str(id_number) + '#' + str(
                    command1)
            else:
                tx_data = mess_type + '#' + object_type + '#' + str(shelf_no) + '#' + str(id_number) + '#' + str(
                    command1) + '#' + str(command2)
        self.uart_write(tx_data)
        return

    def load_history(self):
        self.ui.hboff_textBrowser.setText(self.load_file('ptwh'))

    def load_stats(self):
        self.stats.loaded_stats.clear()
        self.stats.loaded_stats = dict(self.load_file('ptws'))
        self.display_statistics(self.stats.loaded_stats)

    def load_file(self, type):
        if type == 'ptwh':
            name = QFileDialog.getOpenFileName(self, 'Open file', '~/Put_to_wall/PTW_Pyside2_control_app/saved/',
                                               'History files (*.ptwh)')
            self.ui.hboff_filename_label.setText(name[0])
        elif type == 'ptws':
            name = QFileDialog.getOpenFileName(self, 'Open file', '~/Put_to_wall/PTW_Pyside2_control_app/saved/',
                                               'Statistic files (*.ptws)')
            filename = name[0][name[0].rfind('/'):]
            self.ui.bs_filename_label.setText(filename)
            self.stats.last_loaded_filename = filename
        if name[0]:
            file = open(name[0], 'r')
            with file:
                data = json.load(file)
            file.close()
            return data

    def save_file(self, type):
        if type == 'ptwh':
            content = self.ui.pbo_textBrowser.toHtml()
            # file_name = '~/PTW_Pyside2_control_app/saved/'+'History_'+QDate.currentDate().toString(Qt.DefaultLocaleShortDate)+'_'+QTime.currentTime().toString()+'.ptwh'
            file_name = '~/home/pi/Put_to_wall/PTW_Pyside2_control_app/saved/' + 'History_' + QDate.currentDate().toString(
                Qt.DefaultLocaleShortDate) + '.ptwh'
            with open(file_name, 'w') as file:
                json.dump(content, file)
        elif type == 'ptws':
            print('save:   ', self.b.batch_stats)
            file_name = '~/home/pi/Put_to_wall/PTW_Pyside2_control_app/saved/' + str(
                self.b.batch_no) + '_' + QDate.currentDate().toString(
                Qt.DefaultLocaleShortDate) + '_' + QTime.currentTime().toString() + '.ptws'
            with open(file_name, 'w') as file:
                json.dump(self.b.batch_stats, file)
        file.close()

    def delete_file(self):
        filename = QFileDialog.getOpenFileName(self, 'Remove file', '~/Put_to_wall/PTW_Pyside2_control_app/saved/',
                                               'Statistic files (*.ptw*)')
        QFile.remove(filename[0])

    def clear_hboff_textbrowser(self):
        self.ui.hboff_textBrowser.clear()

    def present_stats(self):
        self.ui.bs_filename_label.setText('Present Batch')
        self.display_statistics(self.b.batch_stats)

    def last_loaded_stats(self):
        if len(self.stats.last_loaded_filename) and len(self.stats.loaded_stats):
            self.ui.bs_filename_label.setText(self.stats.last_loaded_filename)
            self.display_statistics(self.stats.loaded_stats)

    def display_statistics(self, data):
        iq_min = 0
        oq_min = 0
        iq_avg = 0
        oq_avg = 0
        iq_max = 0
        oq_max = 0
        stats_ipc_qty = 0
        stats_items_qty = 0
        stats_orders_qty = 0
        total_orders_time = 0
        stats_carts_qty = 0
        order_time = 0
        items_qty = 0
        total_items = 0
        orders_qty = len(data) - 1
        print('len(data)  ', len(data))
        if len(data):
            for idx, (key, value) in enumerate(data.items()):
                if idx == 0:
                    self.ui.bs_batch_no_label.setText(key)
                    self.ui.bs_batch_progress_label.setText(str(value[5]) + '%')
                    batch_time = self.stats.batch_time(value[0], value[1])
                    self.ui.bs_batch_time_label.setText(self.stats.format_time(batch_time))
                    stats_orders_qty = int(value[2])
                    stats_carts = value[3]
                    stats_carts_qty = len(stats_carts)
                    stats_items_qty = int(value[4])
                    for quantity in stats_carts:
                        stats_ipc_qty += quantity
                    if stats_carts_qty > 0:
                        stats_ipc_qty /= stats_carts_qty
                else:
                    if orders_qty:
                        print('idx : ', idx, '  key:  ', key, '  value   : ', value)
                        items_qty = len(value[3])
                        total_items += items_qty
                        order_time = value[2] - value[1]
                        item_time = order_time / items_qty
                        total_orders_time += order_time
                        # time calculation in statistics min, average, max
                        if item_time < iq_min or iq_min == 0:
                            iq_min = item_time
                        print('item time:  ', item_time)
                        print('iq_min :   ', iq_min)
                        if item_time > iq_max:
                            iq_max = item_time
                        print('iq_max :   ', iq_max)
                        iq_avg = total_orders_time / total_items
                        print('order time:  ', order_time)
                        if order_time < oq_min or oq_min == 0:
                            oq_min = order_time
                        print('oq_min :   ', oq_min)
                        if order_time > oq_max:
                            oq_max = order_time
                        print('oq_max :   ', oq_max)
                        oq_avg = batch_time / orders_qty
        else:
            self.ui.bs_batch_no_label.setText('Batch number')
            self.ui.bs_batch_progress_label.setText(str(self.b.progress) + '%')
            self.ui.bs_batch_time_label.setText('N/A')

        self.ui.bs_iq_label.setText(str(stats_items_qty))
        self.ui.bs_oq_label.setText(str(stats_orders_qty))
        self.ui.bs_cq_label.setText(str(stats_carts_qty))
        if stats_carts_qty > 0:
            self.ui.bs_ipc_label.setText(str(round(stats_items_qty / stats_carts_qty, 1)))
        else:
            self.ui.bs_ipc_label.setText('0')
        if stats_orders_qty > 0:
            self.ui.bs_ipo_label.setText(str(round(stats_items_qty / stats_orders_qty, 1)))
        else:
            self.ui.bs_ipo_label.setText('0')
        self.ui.bs_iq_min_label.setText(self.stats.format_time(iq_min))
        self.ui.bs_iq_avg_label.setText(self.stats.format_time(iq_avg))
        self.ui.bs_iq_max_label.setText(self.stats.format_time(iq_max))
        self.ui.bs_oq_min_label.setText(self.stats.format_time(oq_min))
        self.ui.bs_oq_avg_label.setText(self.stats.format_time(oq_avg))
        self.ui.bs_oq_max_label.setText(self.stats.format_time(oq_max))

    def show_message_box(self, message_type, title, message):

        if message_type == 'warning':
            button = QMessageBox.warning(
                self,
                title,
                message,
                buttons=QMessageBox.Yes | QMessageBox.Cancel,
            )
        elif message_type == 'critical':
            button = QMessageBox.critical(
                self,
                title,
                message,
                buttons=QMessageBox.Yes | QMessageBox.Cancel,
            )
        elif message_type == 'question':
            button = QMessageBox.question(
                self,
                title,
                message,
                buttons=QMessageBox.Yes | QMessageBox.Cancel,
            )
        elif message_type == 'information':
            button = QMessageBox.information(
                self,
                title,
                message,
                buttons=QMessageBox.Yes | QMessageBox.Cancel,
            )

        if button == QMessageBox.Yes:
            print("Accepted!")
            return True
        else:
            print("Denied!")
            return False

    def uart_init(self):
        self.update_list = []
        self.error_messages = {}

    def uart_read(self):
        __rx_data = ''
        while self.uart.canReadLine():
            try:
                __rx_data = self.uart.readLine().data().decode('ascii')
                __rx_data = __rx_data.rstrip('\r\n')
            except:
                pass
        print('uart read :  ', __rx_data)
        if __rx_data != '':
            self.uart.clear()
            self.receive_commands(__rx_data)

    def uart_write(self, tx_data):
        __tx_data = '!' + str(tx_data) + '%'
        self.uart.write(__tx_data.encode())
        print('uart write : ', __tx_data)
        time.sleep(0.03)

    def receive_commands(self, data):
        self.received_commands = []
        hmb = 0
        hme = 0
        hmb, hme = str(data).count('!'), str(data).count('%')
        command_string = str(data)
        if len(command_string) and hme and hmb:
            while hme and hmb:
                beg = command_string.find('!')
                end = command_string.find('%')
                if len(command_string):
                    if beg < end:
                        self.update_list.append(command_string[beg + 1:end].split('#'))
                        hmb -= 1
                        hme -= 1
                        command_string = command_string[end + 1:]
                    else:
                        command_string = data[end + 1:]
        print(self.update_list)
        self.process_data_from_wall()

# The following code has been moved to the main.py file
#if __name__ == "__main__":
#    app = QApplication(sys.argv)
#    app.setStyle("Kvantum-dark")
#    if not dbConnect():
#        QSqlDatabase.removeDatabase(QSqlDatabase.database().connectionName())
#        sys.exit(1)
#    window = MainWindow()
#    window.show()
#    #if window.first_run is True:
#    #    window.selftest()
#    sys.exit(app.exec_())
