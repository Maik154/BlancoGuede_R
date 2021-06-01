import sys

import conexion
import var
from ventana import *


class Eventos():

    def matCapital():
        matricula = str(var.ui.txtMatricula.text())

        var.ui.txtMatricula.setText(matricula.upper())

    def cargaFurgo(self):
        try:
            furgo = [var.ui.txtMatricula, var.ui.txtMarca, var.ui.txtModelo]
            for i in furgo:
                var.newFurgo.append(i.text())
            print(var.newFurgo)
            conexion.Conexion.altaFurgo(var.newFurgo)
            conexion.Conexion.listarFurgo(self)
            conexion.Conexion.cargarCmbMat(var.ui.cmbMat)
        except Exception as error:
            print('Error carga furgo: %s ' % str(error))

    def bajaFurgo(self):
        try:
            matricula = var.ui.txtMatricula.text()
            conexion.Conexion.deleteFurgo(matricula)
            conexion.Conexion.listarFurgo(self)
            conexion.Conexion.cargarCmbMat(var.ui.cmbMat)

        except Exception as error:
            print('Error baja furgo: %s ' % str(error))

    def modificaFurgo(self):
        try:
            oldFurgo = [var.ui.txtMatricula, var.ui.txtMarca, var.ui.txtModelo]
            furgoModif = []
            for i in oldFurgo:
                furgoModif.append(i.text())
            conexion.Conexion.modifFurgo(furgoModif)
            conexion.Conexion.listarFurgo(self)
            conexion.Conexion.cargarCmbMat(var.ui.cmbMat)

        except Exception as error:
            print('Error modificar furgo: %s' % str(error))

    def datosUnaFurgo(self):
        try:
            fila = var.ui.tabFurgo.selectedItems()
            furgo = [var.ui.txtMatricula, var.ui.txtMarca, var.ui.txtModelo]
            if fila:
                fila = [dato.text() for dato in fila]
                for i, dato in enumerate(furgo):
                    dato.setText(fila[i])
        except Exception as error:
            print('Error al cargar datos de una furgo: %s ' % str(error))

    def limpiaFurgo():
        try:
            furgo = [var.ui.txtMatricula, var.ui.txtMarca, var.ui.txtModelo]
            for i in range(len(furgo)):
                furgo[i].setText('')

        except Exception as error:
            print('Error al limpiar datos de una furgo: %s ' % str(error))

    def altaCon(self):
        try:
            var.newCon = []
            con = [var.ui.txtDni, var.ui.txtNombre]
            for i in con:
                var.newCon.append(i.text())
            if Eventos.validoDni():
                conexion.Conexion.nuevoCon(var.newCon)
                conexion.Conexion.listarCon(self)
                conexion.Conexion.cargarCmbCon(var.ui.cmbCon)
            else:
                QtWidgets.QMessageBox.critical(None, 'Datos no válidos',
                                               'Compruebe dni y nombre')
        except Exception as error:
            print('Error carga furgo: %s ' % str(error))

    def datosUnCon(self):
        try:
            fila = var.ui.tabConductor.selectedItems()
            con = [var.ui.txtDni, var.ui.txtNombre]

            if fila:
                fila = [dato.text() for dato in fila]
            i = 0
            for i, dato in enumerate(con):
                dato.setText(fila[i])
            var.ui.lblValidar.setText('')
        except Exception as error:
            print('Error al cargar datos de un conductor: %s ' % str(error))

    def bajaCon(self):
        try:
            dni = var.ui.txtDni.text()
            conexion.Conexion.deleteCon(dni)
            conexion.Conexion.listarCon(self)
            conexion.Conexion.cargarCmbCon(var.ui.cmbCon)
        except Exception as error:
            print('Error baja conductor: %s ' % str(error))

    def dniCapital():
        dni = str(var.ui.txtDni.text())
        var.ui.txtDni.setText(dni.upper())

    def nombreCapital():
        nombre = str(var.ui.txtNombre.text())
        var.ui.txtNombre.setText(nombre.title())

    def modificaCon(self):
        try:
            con = [var.ui.txtDni, var.ui.txtNombre]
            conModif = []
            for i in con:
                conModif.append(i.text())
            conexion.Conexion.modifCon(conModif)
            conexion.Conexion.listarCon(self)
            conexion.Conexion.cargarCmbCon(var.ui.cmbCon)

        except Exception as error:
            print('Error modificar furgo: %s' % str(error))

    def limpiaCon():
        try:
            con = [var.ui.txtDni, var.ui.txtNombre]
            for i in range(len(con)):
                con[i].setText('')

        except Exception as error:
            print('Error al limpiar datos de un conductor: %s ' % str(error))

    def validoDni():
        try:
            dni = var.ui.txtDni.text()
            tabla = 'TRWAGMYFPDXBNJZSQVHLCKE'
            dig_ext = 'XYZ'
            reemp_dig_ext = {'X': '0', 'Y': '1', 'Z': '2'}
            numeros = '0123456789'
            dni = dni.upper()
            if len(dni) == 9:
                dig_control = dni[8]
                dni = dni[:8]
                if dni[0] in dig_ext:
                    dni = dni.replace(dni[0], reemp_dig_ext[dni[0]])
                return len(dni) == len([n for n in dni if n in numeros]) and tabla[int(dni) % 23] == dig_control

        except Exception as error:
            print('Error módulo validar DNI %s' % str(error))
            return None

    def validarDni():
        try:
            if Eventos.validoDni():
                var.ui.lblValidar.setStyleSheet('QLabel {color:green;}')
                var.ui.lblValidar.setText('V')
            else:
                var.ui.lblValidar.setStyleSheet('QLabel {color:red}')
                var.ui.lblValidar.setText('X')
        except Exception as error:
            print('Error módulo validar DNI %s' % str(error))
            return None

    def abrirCalendar(self):
        try:
            var.dlgCalendar.show()

        except Exception as error:
            print('Error abrir Calendario' % str(error))
            return None

    def cargaFecha(qDate):
        try:
            data = ('{0}/{1}/{2}'.format(qDate.day(), qDate.month(), qDate.year()))
            var.ui.txtFecha.setText(str(data))
            var.dlgCalendar.hide()

        except Exception as error:
            print('Error abrir calendario %s' % str(error))
            return None

    def calculaDistancia():
        try:
            inicio = int(var.ui.txtKmIni.text())
            final = int(var.ui.txtKmFin.text())
            if final <= inicio:
                var.ui.lblKmTotal.setStyleSheet('QLabel {color:red; background-color: rgb(252, 255, 180);}')
                var.ui.lblKmTotal.setText('Comprueba los km')
            else:
                var.ui.lblKmTotal.setStyleSheet('QLabel {color:black; background-color: rgb(252, 255, 180);}')
                var.ui.lblKmTotal.setText(str(final - inicio))
        except Exception as error:
            print('Error calcular distancia' % str(error))
            return None

    def calculaTarifa(self):
        try:
            coste = []
            coste = conexion.Conexion.cargarTarifas(self)
            print('hola')
            total = int(var.ui.txtKmFin.text()) - int(var.ui.txtKmIni.text())
            print(total)
            if total <= 0:
                var.ui.lblPrecio.setStyleSheet('QLabel {color:red; background-color: rgb(252, 255, 180);}')
                var.ui.lblPrecio.setText('Valores km incorrectos')
            else:
                var.ui.lblPrecio.setStyleSheet('QLabel {color:black; background-color: rgb(252, 255, 180);}')
                if var.ui.rbtLocal.isChecked():
                    var.ui.lblPrecio.setText(str('{0:.2f}'.format(total * coste[0])))

                if var.ui.rbtProvincial.isChecked():
                    var.ui.lblPrecio.setText(str('{0:.2f}'.format(total * coste[1])))

                if var.ui.rbtRegional.isChecked():
                    var.ui.lblPrecio.setText(str('{0:.2f}'.format(total * coste[2])))

                if var.ui.rbtNacional.isChecked():
                    var.ui.lblPrecio.setText(str('{0:.2f}'.format(total * coste[3])))

        except Exception as error:
            print('Error calcular tarifa. %s' % str(error))
            return None

    def altaRuta(self):
        try:
            var.newRuta = []
            tar = conexion.Conexion.cargarTarifas(self)
            tarifa = 0.00
            if var.ui.rbtLocal.isChecked():
                tarifa = tar[0]
            if var.ui.rbtProvincial.isChecked():
                tarifa = tar[1]
            if var.ui.rbtRegional.isChecked():
                tarifa = tar[2]
            if var.ui.rbtNacional.isChecked():
                tarifa = tar[3]
            ruta = [var.ui.txtFecha.text(), var.ui.cmbMat.currentText(),
                    var.ui.cmbCon.currentText(), var.ui.txtKmIni.text(),
                    var.ui.txtKmFin.text(), str(tarifa)]
            print(tarifa)
            for i in ruta:
                var.newRuta.append(i)
            conexion.Conexion.altaRuta(var.newRuta)
            conexion.Conexion.listarRuta(self)

        except Exception as error:
            print('Error alta tarifa. %s' % str(error))

    def limpiaRuta(self):
        try:
            con = [var.ui.lblRuta, var.ui.txtFecha,
                   var.ui.txtKmIni, var.ui.txtKmFin,
                   var.ui.lblKmTotal, var.ui.lblPrecio]
            for i in range(len(con)):
                con[i].setText('')
            var.ui.cmbMat.setCurrentIndex(0)
            var.ui.cmbCon.setCurrentIndex(0)

        except Exception as error:
            print('Error al limpiar datos de un conductor: %s ' % str(error))


    '''
    eventos generales
    '''

    def salir(self):
        try:
            ret = QtWidgets.QMessageBox.question(None, 'Salir',
                                                 '¿Desea salir?')
            if ret == QtWidgets.QMessageBox.Yes:
                sys.exit(0)
            if ret == QtWidgets.QMessageBox.No:
                QtWidgets.QMessageBox.hide()

        except Exception as error:
            print('Error calcular distancia %s' % str(error))
            return None
