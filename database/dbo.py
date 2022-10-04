# dbo.py - 'Put to Wall concept' database operations
# Author: Tomasz Zgrys AiR, 2021/2022, WWSIS Horyzont
# Copyright: Tomasz Zgrys & WWSIS Horyzont


from PySide2.QtCore import Qt
from PySide2.QtGui import QBrush, QColor
from PySide2.QtSql import QSqlQuery, QSqlQueryModel, QSqlDatabase, QSqlTableModel
from PySide2.QtWidgets import QMessageBox

counter = 0


def dbConnect():
    global db
    db = QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName('database/ptw.sqlite')
    if not db.open():
        QMessageBox.critical(
            None,
            "Problem with connection - Error!",
            "Database Error: %s" % db.lastError().databaseText(),
        )
        return False
    return True


class lopiModel(QSqlQueryModel):
    def __init__(self, batch_no='%', parent=None):
        QSqlQueryModel.__init__(self, parent=parent)
        self.batch_no = batch_no
        self.lopi_query()
        self.cf = True

    def update_flag(self):
        self.cf = not self.cf

    def lopi_query(self):
        self.query = QSqlQuery()
        self.query.prepare(
            '''SELECT 
                    Batch.Batch_no as 'Batch no',
                    Orders.Order_no as 'Order no',
                    Item.Item_barcode as 'Item barcode',
                    Item.Item_name as 'Item name',
                    Cart.Cart_barcode as 'Cart barcode',
                    PTW_main_table.Shelf_no as 'Shelf no',
                    PTW_main_table.Item_number as 'Ordinal no',
                    PTW_main_table.Confirmation_time as 'Timestamp',
                    PTW_main_table.Status
                FROM
                    PTW_main_table
                    INNER JOIN Batch ON Batch.Batch_id = PTW_main_table.Batch_no_id
                    INNER JOIN Orders ON Orders.Order_id = PTW_main_table.Order_no_id 
                    INNER JOIN Item ON Item.Item_id = PTW_main_table.Item_no_id 
                    INNER JOIN Cart ON Cart.Cart_Id = PTW_main_table.Cart_no_id 
                WHERE
                    Batch.Batch_no LIKE :batch_no AND
                    PTW_main_table.Status >= 1
                ORDER BY
                    Batch.Batch_no,
                    Orders.Order_no
                    '''
        )
        self.query.bindValue(":batch_no", self.batch_no)
        self.query.exec_()
        self.setQuery(self.query)

    def data(self, item, role):
        if role == Qt.BackgroundRole:
            status = QSqlQueryModel.data(self, self.index(item.row(), 8), Qt.DisplayRole)
            if status == 1:
                if self.cf:
                    return QBrush(QColor('#FF6600'))
                else:
                    return QBrush(QColor('#2E2E2E'))
            if status == 2:
                return QBrush(QColor('#FF0000'))
            elif status == 3:
                if self.cf:
                    return QBrush(QColor('#00AA00'))
                else:
                    return QBrush(QColor('#2E2E2E'))
            elif status == 4:
                return QBrush(QColor('#006600'))
            elif status == 5:
                return QBrush(QColor('#000066'))

        return QSqlQueryModel.data(self, item, role)


def dv_table_model(self, batch_no='%', order_no="%", item_barcode="%", cart_barcode="%"):
    model = QSqlQueryModel()
    query = QSqlQuery()
    query.prepare('''
                    SELECT 
                        Batch.Batch_no as 'Batch no',
                        Orders.Order_no as 'Order no',
                        Item.Item_barcode as 'Item barcode',
                        Item.Item_name as 'Item name',
                        Cart.Cart_barcode as 'Cart barcode',
                        PTW_main_table.Status,
                        PTW_main_table.PTW_mt_Id
                    FROM
                        PTW_main_table
                        INNER JOIN Batch ON Batch.Batch_id = PTW_main_table.Batch_no_id
                        INNER JOIN Orders ON Orders.Order_id = PTW_main_table.Order_no_id 
                        INNER JOIN Item ON Item.Item_id = PTW_main_table.Item_no_id 
                        INNER JOIN Cart ON Cart.Cart_Id = PTW_main_table.Cart_no_id 
                    WHERE
                        Batch.Batch_no LIKE :batch_no AND
                        (Orders.Order_no LIKE :order_no OR
                        Item_barcode LIKE :item_barcode OR
                        Cart.Cart_barcode LIKE :cart_barcode)
                    ORDER BY 
                        Batch.Batch_no ASC,
                        Orders.Order_no ASC,
                        Item.Item_barcode ASC

                    ''')
    query.bindValue(":batch_no", batch_no)
    query.bindValue(":order_no", order_no)
    query.bindValue(":item_barcode", item_barcode)
    query.bindValue(":cart_barcode", cart_barcode)
    query.exec_()
    model.setQuery(query)
    return model


def batch_query_distinct_list(self):
    query = QSqlQuery()
    query.prepare('''
                    SELECT DISTINCT
                        Batch.Batch_no
                    FROM
                        PTW_main_table
                    INNER JOIN Batch ON Batch.Batch_id = PTW_main_table.Batch_no_id
                    ''')
    query.exec_()
    return query


def orders_query_distinct_list(self, batch_no):
    model = QSqlQueryModel()
    query = QSqlQuery()
    query.prepare('''
                    SELECT DISTINCT
                        Orders.Order_no
                    FROM 
                        PTW_main_table
                    INNER JOIN Batch ON Batch.Batch_id = PTW_main_table.Batch_no_id
                    INNER JOIN Orders ON Orders.Order_id = PTW_main_table.Order_no_id
                    WHERE
                        Batch.Batch_no LIKE :batch_no
                    ''')
    query.bindValue(":batch_no", batch_no)
    query.exec_()
    model.setQuery(query)
    model.layoutChanged.emit()
    return model


def cart_items_query_distinct_list(self, batch_no):
    query = QSqlQuery()
    query.prepare('''
                    SELECT DISTINCT
                        Cart.Cart_barcode, COUNT(Item_no_id) AS Items_qty
                    FROM 
                        PTW_main_table
                    INNER JOIN Batch ON Batch.Batch_id = PTW_main_table.Batch_no_id
                    INNER JOIN Cart ON Cart.Cart_id = PTW_main_table.Cart_no_id
                    WHERE 
                        Batch.Batch_no LIKE :batch_no
                    GROUP BY 
                        Cart.Cart_barcode
                    ''')
    query.bindValue(":batch_no", batch_no)
    query.exec_()
    return query


def content_batch_query(self, batch_no='%'):
    model = QSqlQueryModel()
    query = QSqlQuery()
    query.prepare('''
                SELECT 
                    Batch.Batch_no,
                    Orders.Order_no as 'Order no',
                    Item.Item_barcode as 'Item barcode',
                    Item.Item_name as 'Item name',
                    Cart.Cart_barcode as 'Cart barcode',
                    PTW_main_table.Status
                FROM
                    PTW_main_table
                    INNER JOIN Batch ON Batch.Batch_id = PTW_main_table.Batch_no_id
                    INNER JOIN Orders ON Orders.Order_id = PTW_main_table.Order_no_id 
                    INNER JOIN Item ON Item.Item_id = PTW_main_table.Item_no_id 
                    INNER JOIN Cart ON Cart.Cart_Id = PTW_main_table.Cart_no_id 
                WHERE
                    Batch.Batch_no LIKE :batch_no
                ORDER BY 
                    Orders.Order_no ASC,
                    Item.Item_barcode ASC
                ''')
    query.bindValue(":batch_no", batch_no)
    query.exec_()
    model.setQuery(query)
    model.layoutChanged.emit()
    return model


def query_num_rows(self, query):
    __num_rows = query.last()
    __num_rows = query.at() + 1
    return __num_rows


def orderCount(self, batch_no):
    orders_qty = orders_query_distinct_list(self, batch_no).rowCount()
    return orders_qty


def itemCount(self, batch_no):
    item_qty = content_batch_query(self, batch_no).rowCount()
    return item_qty


def cartItemsCount(self, batch_no):
    cart_items_list = []
    cart_items_query = cart_items_query_distinct_list(self, batch_no)
    num_rows = query_num_rows(self, cart_items_query)
    if cart_items_query.isSelect() and cart_items_query.isActive() and num_rows > 0:
        cart_items_query.first()
        for i in range(num_rows):
            cart_items_list.append(cart_items_query.value('Items_qty'))
            cart_items_query.next()
        return cart_items_list


def ordersLeft(self, batch_no):
    model = QSqlQueryModel()
    query = QSqlQuery()
    query.prepare('''
                    SELECT COUNT (DISTINCT Order_no)
                    FROM 
                        PTW_main_table
                        INNER JOIN Orders ON Orders.Order_Id=PTW_main_table.Order_no_id
                        INNER JOIN Batch ON Batch.Batch_Id=PTW_main_table.Batch_no_id
                    WHERE 
                        (PTW_main_table.Status < 4 OR PTW_main_table.Status is Null) AND Batch.Batch_no LIKE :batch_no
                    ''')
    query.bindValue(":batch_no", batch_no)
    query.exec_()
    model.setQuery(query)
    query.first()
    return query.value(0)


def itemsLeft(self, batch_no):
    model = QSqlQueryModel()
    query = QSqlQuery()
    query.prepare('''
                SELECT COUNT (Item_barcode)
                FROM 
                    PTW_main_table
                    INNER JOIN Item ON Item.Item_Id=PTW_main_table.Item_no_id
                    INNER JOIN Batch ON Batch.Batch_Id=PTW_main_table.Batch_no_id
                WHERE 
                    (PTW_main_table.Status < 2 OR PTW_main_table.Status is Null) AND Batch.Batch_no LIKE :batch_no
                ''')
    query.bindValue(":batch_no", batch_no)
    query.exec_()
    rec = query.record()
    name = rec.indexOf('COUNT (Item_barcode)')
    query.first()
    return query.value(0)


def showItemQty(self, batch_no):
    query = QSqlQuery()
    query.prepare('''
                        SELECT                        
                            Item.Item_barcode AS "Item barcode",
                            COUNT(Item.Item_barcode) AS "Items quantity",
                            Cart.Cart_barcode as 'Cart barcode'
                        FROM
                            PTW_main_table
                            INNER JOIN Batch ON Batch.Batch_id = PTW_main_table.Batch_no_id
                            INNER JOIN Item ON Item.Item_id = PTW_main_table.Item_no_id 
                            INNER JOIN Cart ON Cart.Cart_Id = PTW_main_table.Cart_no_id
                        WHERE
                            Batch_no_id like (SELECT Batch_Id FROM Batch WHERE Batch_no LIKE  :batch_no)        
                        GROUP BY 
                            Item.Item_barcode,
                            Cart.Cart_barcode
                        ORDER BY 
                            Item.Item_barcode,
                            COUNT(Item.Item_barcode),
                            Cart.Cart_barcode
                        ''')

    query.bindValue(":batch_no", batch_no)
    query.exec_()
    return query


def check_item_in_DB(self, query_version, batch_no, order_no, item_barcode, shelf_no, status, item_no, conf_time,
                     mt_id):
    query = QSqlQuery()
    if query_version == 'all_null':
        clause_where = '''  Shelf_no is Null AND
                            Status is Null AND
                            Item_number is Null AND
                            Confirmation_time is Null '''
    elif query_version == 'only_shelf_rest_null':
        clause_where = '''  Shelf_no like :shelf_no AND
                            Status is Null AND
                            Item_number is Null AND
                            Confirmation_time is Null '''
    elif query_version == 'shelf_and_status_null':
        clause_where = '''  Shelf_no like :shelf_no AND
                            Status is Null'''
    elif query_version == 'shelf_and_status_like':
        clause_where = '''  Shelf_no like :shelf_no AND
                            Status like :status'''
    elif query_version == 'only_status':
        clause_where = ' AND Status ' + status + ' '
    elif query_version == 'full_list':
        clause_where = ''

    query.prepare('''
                    SELECT                        
                        Batch.Batch_no,
                        Orders.Order_no,
                        Item.Item_barcode,
                        PTW_main_table.Shelf_no,
                        PTW_main_table.Status,
                        PTW_main_table.Item_number,
                        PTW_main_table.Confirmation_time,
                        PTW_main_table.PTW_mt_Id
                    FROM
                        PTW_main_table
                        INNER JOIN Batch ON Batch.Batch_id = PTW_main_table.Batch_no_id
                        INNER JOIN Orders ON Orders.Order_id = PTW_main_table.Order_no_id 
                        INNER JOIN Item ON Item.Item_id = PTW_main_table.Item_no_id 
                    WHERE
                        PTW_mt_id like :mt_id AND
                        Batch_no_id like (SELECT Batch_Id FROM Batch WHERE Batch_no LIKE  :batch_no) AND
                        Order_no_id in (SELECT Order_id FROM Orders WHERE Order_no LIKE :order_no) AND
                        Item_no_id in (SELECT Item_Id FROM Item WHERE Item_barcode LIKE :item_barcode)
                     ''' + clause_where + '''                     
                    ORDER BY                        
                        PTW_main_table.Shelf_no NULLS LAST,
                        Orders.Order_no ASC,
                        Item.Item_barcode ASC
                    ''')

    query.bindValue(":mt_id", mt_id)
    query.bindValue(":batch_no", batch_no)
    query.bindValue(":order_no", order_no)
    query.bindValue(":item_barcode", item_barcode)
    query.bindValue(":shelf_no", shelf_no)
    query.bindValue(":status", status)
    query.bindValue(":item_no", item_no)
    query.bindValue(":conf_time", conf_time)
    query.exec_()
    return query


def add_row_into_DB(self, batch_no, order_no, item_barcode, cart_barcode):
    model = QSqlQueryModel()

    query = QSqlQuery()

    query.prepare('''
                    INSERT INTO PTW_main_table 
                        (Batch_no_id,Order_no_id,Item_no_id,Cart_no_id,Shelf_no,Status,Item_number,Confirmation_time)
                    VALUES   
                        ((SELECT Batch_Id FROM Batch WHERE Batch_no = :batch_no),
                        (SELECT Order_id FROM Orders WHERE Order_no = :order_no),
                        (SELECT Item_Id FROM Item WHERE Item_barcode = :item_barcode),
                        (SELECT Cart_Id FROM Cart WHERE Cart_barcode = :cart_barcode),
                        Null,Null,Null,Null)
                    ''')
    query.bindValue(":batch_no", batch_no)
    query.bindValue(":order_no", order_no)
    query.bindValue(":item_barcode", item_barcode)
    query.bindValue(":cart_barcode", cart_barcode)
    query.exec_()
    model.setQuery(query)
    model.layoutChanged.emit()
    return model


def change_data_in_DB(self, mt_id, batch_no, order_no, item_barcode, shelf_no, status, item_no, conf_time):
    query = QSqlQuery()
    if status == None or status == 1:
        clause_value = '''  Shelf_no = :shelf_no, 
                            Status = :status, 
                            Item_number = :item_no, 
                            Confirmation_time = :conf_time '''
    elif status > 1:
        clause_value = '''  Status = :status '''

    query.prepare('''
                    UPDATE PTW_main_table 
                    SET ''' + clause_value + '''  
                    WHERE
                        PTW_mt_Id like :mt_id AND
                        Batch_no_id like (SELECT Batch_Id FROM Batch WHERE Batch_no LIKE :batch_no) AND
                        Order_no_id in (SELECT Order_id FROM Orders WHERE Order_no LIKE :order_no) AND
                        Item_no_id in (SELECT Item_Id FROM Item WHERE Item_barcode LIKE :item_barcode)
                    ''')
    query.bindValue(":shelf_no", shelf_no)
    query.bindValue(":status", status)
    query.bindValue(":mt_id", mt_id)
    query.bindValue(":batch_no", batch_no)
    query.bindValue(":order_no", order_no)
    query.bindValue(":item_barcode", item_barcode)
    query.bindValue(":item_no", item_no)
    query.bindValue(":conf_time", conf_time)
    query.exec_()


def remove_data_from_DB(self, mt_id, batch_no, order_no, item_barcode, cart_barcode):
    query = QSqlQuery()
    query.prepare('''
                    DELETE FROM PTW_main_table
                    WHERE
                        PTW_mt_id like :mt_id AND
                        Batch_no_id like (SELECT Batch_Id FROM Batch WHERE Batch_no LIKE  :batch_no) AND
                        Order_no_id in (SELECT Order_id FROM Orders WHERE Order_no LIKE :order_no) AND
                        Item_no_id in (SELECT Item_Id FROM Item WHERE Item_barcode LIKE :item_barcode) AND
                        Cart_no_id in (SELECT Cart_Id FROM Cart WHERE Cart_barcode LIKE :cart_barcode)
                        ''')
    query.bindValue(":mt_id", mt_id)
    query.bindValue(":batch_no", batch_no)
    query.bindValue(":order_no", order_no)
    query.bindValue(":item_barcode", item_barcode)
    query.bindValue(":cart_barcode", cart_barcode)
    query.exec_()


def combo_model(self, table):
    model = QSqlTableModel()
    if table == 'Batch':
        model.setTable('Batch')
    elif table == 'Orders':
        model.setTable('Orders')
    elif table == 'Item':
        model.setTable('Item')
    elif table == 'Cart':
        model.setTable('Cart')
    model.select()
    return model
