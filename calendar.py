# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calendar.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_dlgCalendar(object):
    def setupUi(self, dlgCalendar):
        dlgCalendar.setObjectName("dlgCalendar")
        dlgCalendar.setWindowModality(QtCore.Qt.ApplicationModal)
        dlgCalendar.resize(400, 300)
        dlgCalendar.setModal(True)
        self.Calendar = QtWidgets.QCalendarWidget(dlgCalendar)
        self.Calendar.setGeometry(QtCore.QRect(10, 10, 381, 281))
        self.Calendar.setObjectName("Calendar")

        self.retranslateUi(dlgCalendar)
        QtCore.QMetaObject.connectSlotsByName(dlgCalendar)

    def retranslateUi(self, dlgCalendar):
        _translate = QtCore.QCoreApplication.translate
        dlgCalendar.setWindowTitle(_translate("dlgCalendar", "Seleccione Fecha"))
