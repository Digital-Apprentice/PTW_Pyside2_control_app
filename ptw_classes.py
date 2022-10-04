# ptw_classes.py - 'Put to Wall concept' classes
# Author: Tomasz Zgrys AiR, 2021/2022, WWSIS Horyzont
# Copyright: Tomasz Zgrys & WWSIS Horyzont
# Classes related to the PTW order picking wall
# Batch class - a class related to batch and wall initialization
# Shelf class - all variables and methods for each compartment / shelf
# Statistics class - basic statistics for Batch

from PySide2.QtCore import QDateTime

class Shelf:
    def __init__(self, shelf_no):
        self.shelf_no = shelf_no
        self.shelf_no_label = ()
        self.shelf_no_progressbar = ()
        self.shelf_no_order_label = ()
        self.shelf_qty_label = ()
        self.shelf_init()

    def shelf_init(self):
        self.shelf_empty = True
        self.shelf_full = False
        self.waiting_front_conf = False
        self.waiting_back_conf = False
        self.order_no = None
        self.error = False
        self.start_time = 0
        self.end_time = 0
        self.items_qty = 0
        self.item_no = 0
        self.start_time = 0
        self.end_time = 0
        self.progress = 0
        self.item_mt_id = []


class Batch:
    def __init__(self):
        self.batch_init()

    def batch_init(self):
        self.batch_no = None
        self.orders_qty = 0
        self.carts_qty = 0
        self.items_qty = 0
        self.items_in_carts = []
        self.batch_button = False
        self.waiting_front_conf = None
        self.waiting_back_conf = []
        self.error = False
        self.background_flag = False
        self.start_time = 0
        self.end_time = 0
        self.progress = 0
        self.orders_in_shelves = []
        self.empty_shelves = []
        self.batch_stats = {}
        self.shelf_label_background = {}

class Statistics():
    def __init__(self):
        self.stats_init()

    def stats_init(self):
        self.present_stats = {}
        self.loaded_stats = {}
        self.last_loaded_filename = ''

    def format_time(self, time):
        if time > 0:
            hours = time // 3600
            minutes = time % 3600 // 60
            seconds = time % 3600 % 60
            if hours == 0 and minutes == 0:
                result = str(int(seconds)) + 's'
            elif hours == 0:
                result = str(int(minutes))+'m'+str(int(seconds))+'s'
            else:
                result = str(int(hours))+'h'+str(int(minutes))+'m'+str(int(seconds))+'s'
            return result

    def batch_time(self,start_time,end_time):
        if start_time and end_time:
            difference = end_time - start_time
            return difference
        elif start_time and end_time == 0:
            difference = QDateTime.currentDateTime().toTime_t() - start_time
            return difference
        else:
            return 0
