# main_classes.py - 'Put to Wall concept' main file
# Author: Tomasz Zgrys AiR, 2021/2022, WWSIS Horyzont
# Copyright: Tomasz Zgrys & WWSIS Horyzont


from ptw import *
from PySide2.QtWidgets import *
import sys


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Kvantum-dark")
    if not dbConnect():
        QSqlDatabase.removeDatabase(QSqlDatabase.database().connectionName())
        sys.exit(1)
    window = MainWindow()
    window.show()
    #if window.first_run is True:
    #    window.selftest()
    sys.exit(app.exec_())
