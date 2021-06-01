# -*- coding: utf-8 -*-

import locale
# Form implementation generated from reading ui file 'main.py'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import sys
from datetime import datetime

from tarifas import *

import conexion
import eventos
import rutas
import var
import informes
from calendar import *

locale.setlocale(locale.LC_ALL, 'es-Es')


class DialogCalendar(QtWidgets.QDialog):
    def __init__(self):
        super(DialogCalendar, self).__init__()
        var.dlgCalendar = Ui_dlgCalendar()
        var.dlgCalendar.setupUi(self)
        dia = datetime.now().day
        mes = datetime.now().month
        ano = datetime.now().year
        var.dlgCalendar.Calendar.setSelectedDate((QtCore.QDate(ano, mes, dia)))
        var.dlgCalendar.Calendar.clicked.connect(eventos.Eventos.cargaFecha)


class DialogTarifas(QtWidgets.QDialog):
    def __init__(self):
        super(DialogTarifas, self).__init__()
        var.dlgTarifas = Ui_dlgTarifas()
        var.dlgTarifas.setupUi(self)
        var.tarifas = [var.dlgTarifas.txtLocal, var.dlgTarifas.txtProvincial, var.dlgTarifas.txtRegional, var.dlgTarifas.txtNacional]
        var.dlgTarifas.btnActualizarTarifas.clicked.connect(conexion.Conexion.actualizarTarifas)


from ventana import Ui_MainWindow


class Main(QtWidgets.QMainWindow):
    def __init__(self):
        '''
        genera y conecta los eventos
        '''
        super(Main, self).__init__()
        var.ui = Ui_MainWindow()
        var.ui.setupUi(self)

        '''Instanciar ventanas auxiliares'''

        var.dlgCalendar = DialogCalendar()
        var.dlgTarifas = DialogTarifas()

        '''
        Conexión a la base de datos.
        '''
        conexion.Conexion.db_connect(self)
        conexion.Conexion.listarFurgo(self)
        conexion.Conexion.listarCon(self)
        conexion.Conexion.listarRuta(self)
        conexion.Conexion.cargarCmbMat(var.ui.cmbMat)
        conexion.Conexion.cargarCmbCon(var.ui.cmbCon)

        '''
        llamadas a los eventos de los botones
        '''
        var.ui.btnGrabar.clicked.connect(eventos.Eventos.cargaFurgo)
        var.ui.txtMatricula.editingFinished.connect(eventos.Eventos.matCapital)
        var.ui.btnReload.clicked.connect(eventos.Eventos.limpiaFurgo)
        var.ui.btnEliminar.clicked.connect(eventos.Eventos.bajaFurgo)
        var.ui.btnModif.clicked.connect(eventos.Eventos.modificaFurgo)
        var.ui.btnAltaCon.clicked.connect(eventos.Eventos.altaCon)
        var.ui.btnEliminarCon.clicked.connect(eventos.Eventos.bajaCon)
        var.ui.txtDni.editingFinished.connect(eventos.Eventos.dniCapital)
        var.ui.txtNombre.editingFinished.connect(eventos.Eventos.nombreCapital)
        var.ui.btnModifCon.clicked.connect(eventos.Eventos.modificaCon)
        var.ui.btnReloadCon.clicked.connect(eventos.Eventos.limpiaCon)
        var.ui.txtDni.editingFinished.connect(eventos.Eventos.validarDni)
        var.ui.btnCalendar.clicked.connect(eventos.Eventos.abrirCalendar)
        var.ui.txtKmFin.editingFinished.connect(eventos.Eventos.calculaDistancia)
        var.ui.btnAltaRuta.clicked.connect(eventos.Eventos.altaRuta)
        var.ui.btnBajaRuta.clicked.connect(rutas.Rutas.bajaRuta)
        var.ui.btnLimpiaRuta.clicked.connect(eventos.Eventos.limpiaRuta)
        var.ui.btnSalir.clicked.connect(eventos.Eventos.salir)
        var.ui.btnModifRuta.clicked.connect(rutas.Rutas.modificaRuta)
        '''
        eventos de las tablas
        '''

        var.ui.tabFurgo.clicked.connect(eventos.Eventos.datosUnaFurgo)
        var.ui.tabFurgo.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
        var.ui.tabFurgo.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        var.ui.tabConductor.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
        var.ui.tabConductor.clicked.connect(eventos.Eventos.datosUnCon)
        var.ui.tabConductor.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        var.ui.tabRutas.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
        var.ui.tabRutas.clicked.connect(rutas.Rutas.cargaUnaRuta)


        '''
        eventos tarifas
        '''
        var.ui.btnTipoRuta.buttonClicked.connect(eventos.Eventos.calculaTarifa)



        '''
        eventos rutas
        '''


        '''
        eventos menuBar
        '''
        var.ui.menuBarSalir.triggered.connect(eventos.Eventos.salir)
        var.ui.menuBarTarifas.triggered.connect(rutas.Rutas.mostrarTarifas)
        var.ui.reportRutas.triggered.connect(informes.Informes.informeRutas)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    # window.setFixedSize(1204, 768)
    window.setMinimumSize(800, 650)
    # window.showMaximized()
    window.show()
    sys.exit(app.exec())
