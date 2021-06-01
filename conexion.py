from PyQt5 import QtSql

import var
from ventana import *


class Conexion():
    def db_connect(self):
        filename = 'logista.db'
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName(filename)
        if not db.open():
            QtWidgets.QMessageBox.critical(None, 'No se puede abrir la BBDD',
                                           'Imposible Conexión.\n' 'Haga Click para Cancelar.',
                                           QtWidgets.QMessageBox.Cancel)
            return False
        else:

            QtWidgets.QMessageBox.warning(None, 'Abierta Base de Datos',
                                          'Haga Click para Continuar')

            print('Conexion Establecida')

    '''
    Funciones xestión furgonetas
    '''

    def altaFurgo(newfurgo):
        query = QtSql.QSqlQuery()
        query.prepare('insert into furgoneta (matricula, marca, modelo)'
                      'VALUES (:matricula, :marca, :modelo)')
        query.bindValue(':matricula', str(newfurgo[0]))
        query.bindValue(':marca', str(newfurgo[1]))
        query.bindValue(':modelo', str(newfurgo[2]))
        if query.exec_():
            QtWidgets.QMessageBox.information(None, 'Alta Furgoneta Correcta',
                                              'Haga Click para Continuar')

        else:
            QtWidgets.QMessageBox.warning(None, query.lastError().text(),
                                          'Haga Click para Continuar')

    def listarFurgo(self):
        index = 0
        query = QtSql.QSqlQuery()
        query.prepare('select matricula, marca, modelo from furgoneta')
        if query.exec_():
            while query.next():
                var.ui.tabFurgo.setRowCount(index + 1)  # creo la fila
                var.ui.tabFurgo.setItem(index, 0, QtWidgets.QTableWidgetItem(query.value(0)))
                var.ui.tabFurgo.setItem(index, 1, QtWidgets.QTableWidgetItem(query.value(1)))
                var.ui.tabFurgo.setItem(index, 2, QtWidgets.QTableWidgetItem(query.value(2)))
                index += 1
        else:
            QtWidgets.QMessageBox.warning(None, query.lastError().text(),
                                          'Haga Click para Continuar')

    def deleteFurgo(matricula):
        query = QtSql.QSqlQuery()
        query.prepare('delete from furgoneta where matricula = :matricula')
        query.bindValue(':matricula', str(matricula))
        if query.exec_():
            QtWidgets.QMessageBox.information(None, 'Furgoneta Eliminada',
                                              'Haga Click para Continuar')
        else:
            QtWidgets.QMessageBox.warning(None, query.lastError().text(),
                                          'Haga Click para Continuar')

    def modifFurgo(furgomodif):
        query = QtSql.QSqlQuery()
        print(furgomodif)
        query.prepare('update furgoneta set marca=:marca, modelo=:modelo'
                      ' where matricula=:matricula')
        query.bindValue(':marca', str(furgomodif[1]))
        query.bindValue(':modelo', str(furgomodif[2]))
        query.bindValue(':matricula', str(furgomodif[0]))
        if query.exec_():
            QtWidgets.QMessageBox.information(None, 'Furgoneta Modificada',
                                              'Haga Click para Continuar')
        else:
            QtWidgets.QMessageBox.warning(None, query.lastError().text(),
                                          'Recuerde que no puede modificar la matrícula. Haga Click para Continuar')

    '''
    Gestión de conductores
    '''

    def nuevoCon(newCon):
        query = QtSql.QSqlQuery()
        query.prepare('insert into conductor (dni, nombre)'
                      'VALUES (:dni, :nombre)')
        query.bindValue(':dni', str(newCon[0]))
        query.bindValue(':nombre', str(newCon[1]))
        if query.exec_():
            QtWidgets.QMessageBox.information(None, 'Alta Conducor Correcta',
                                              'Haga Click para Continuar')

        else:
            QtWidgets.QMessageBox.warning(None, query.lastError().text(),
                                          'Haga Click para Continuar')

    def listarCon(self):
        index = 0
        query = QtSql.QSqlQuery()
        query.prepare('select dni, nombre from conductor')
        if query.exec_():
            while query.next():
                var.ui.tabConductor.setRowCount(index + 1)
                var.ui.tabConductor.setItem(index, 0, QtWidgets.QTableWidgetItem(query.value(0)))
                var.ui.tabConductor.setItem(index, 1, QtWidgets.QTableWidgetItem(query.value(1)))
                index += 1
        else:
            QtWidgets.QMessageBox.warning(None, query.lastError().text(),
                                          "Haga click para continuar")

    def deleteCon(dni):
        query = QtSql.QSqlQuery()
        query.prepare('delete from conductor where dni = :dni')
        query.bindValue(':dni', str(dni))
        if query.exec_():
            QtWidgets.QMessageBox.information(None, 'Conductor Eliminado',
                                              'Haga Click para Continuar')
        else:
            QtWidgets.QMessageBox.warning(None, query.lastError().text(),
                                          'Haga Click para Continuar')

    def modifCon(conModif):
        query = QtSql.QSqlQuery()
        print(conModif)
        query.prepare('update conductor set nombre=:nombre'
                      ' where dni=:dni')
        query.bindValue(':nombre', str(conModif[1]))
        query.bindValue(':dni', str(conModif[0]))
        if query.exec_():
            QtWidgets.QMessageBox.information(None, 'Conductor Modificado',
                                              'Haga Click para Continuar')
        else:
            QtWidgets.QMessageBox.warning(None, query.lastError().text(),
                                          'Recuerde que no puede modificar el dni. Haga Click para Continuar')

    def cargarCmbCon(cmbCon):
        cmbCon.clear()
        cmbCon.addItem('Elija conductor')
        query = QtSql.QSqlQuery()
        query.prepare('select nombre from conductor')
        if query.exec_():
            while query.next():
                cmbCon.addItem(str(query.value(0)))

    def cargarCmbMat(cmbMat):
        cmbMat.clear()
        cmbMat.addItem('')
        query = QtSql.QSqlQuery()
        query.prepare('select matricula from furgoneta')
        if query.exec_():
            while query.next():
                cmbMat.addItem(str(query.value(0)))

    def cargarTarifas(self):
        tar = []
        query = QtSql.QSqlQuery()
        query.prepare('select * from tarifas')
        if query.exec_():
            while query.next():
                var.tarifas[0].setText(str(query.value(1)))
                tar.append(query.value(1))
                var.tarifas[1].setText(str(query.value(2)))
                tar.append(query.value(2))
                var.tarifas[2].setText(str(query.value(3)))
                tar.append(query.value(3))
                var.tarifas[3].setText(str(query.value(4)))
                tar.append(query.value(4))
        return tar

    def actualizarTarifas(self):
        try:
            nuevaTarifa = []
            id = 1
            for i, dato in enumerate(var.tarifas):
                nuevaTarifa.append('{0:.2f}'.format(float(dato.text())))
            print(nuevaTarifa)
            query = QtSql.QSqlQuery()
            query.prepare(
                'update tarifas set local=:local, provincial=:provincial, regional=:regional, nacional=:nacional '
                'where id=:id')
            query.bindValue(':id', int(id))
            query.bindValue(':local', '{0:.2f}'.format(float(nuevaTarifa[0])))
            query.bindValue(':provincial', '{0:.2f}'.format(float(nuevaTarifa[1])))
            query.bindValue(':regional', '{0:.2f}'.format(float(nuevaTarifa[2])))
            query.bindValue(':nacional', '{0:.2f}'.format(float(nuevaTarifa[3])))
            if query.exec_():
                QtWidgets.QMessageBox.information(None, 'Tarifas modificadas',
                                                  'Haga Click para Continuar')
            else:
                QtWidgets.QMessageBox.warning(None, query.lastError().text(),
                                              'Recuerde que las tarifas son únicas. Haga Click para Continuar')
        except Exception as error:
            print('Error actualizar tarifas: %s: ' % str(error))

    def altaRuta(newruta):
        print(newruta)
        query = QtSql.QSqlQuery()
        query.prepare('insert into ruta (fecha, matricula, conductor, kmIni, kmFin, tarifa)'
                      'VALUES (:fecha, :matricula, :conductor, :kmIni, :kmFin, :tarifa)')
        query.bindValue(':fecha', str(newruta[0]))
        query.bindValue(':matricula', str(newruta[1]))
        query.bindValue(':conductor', str(newruta[2]))
        query.bindValue(':kmIni', str(newruta[3]))
        query.bindValue(':kmFin', str(newruta[4]))
        query.bindValue(':tarifa', str(newruta[5]))
        if query.exec_():
            QtWidgets.QMessageBox.information(None, 'Alta tarifa?',
                                              'Haga Click para Continuar')
        else:
            QtWidgets.QMessageBox.warning(None, query.lastError().text(),
                                          'Recuerde que las tarifas son únicas. Haga Click para Continuar')

    def listarRuta(self):
        index = 0
        query = QtSql.QSqlQuery()
        query.prepare('select * from ruta')
        if query.exec_():
            while query.next():
                var.ui.tabRutas.setRowCount(index + 1)
                var.ui.tabRutas.setItem(index, 0, QtWidgets.QTableWidgetItem(str(query.value(0))))
                var.ui.tabRutas.setItem(index, 1, QtWidgets.QTableWidgetItem(query.value(1)))
                var.ui.tabRutas.setItem(index, 2, QtWidgets.QTableWidgetItem(query.value(2)))
                var.ui.tabRutas.setItem(index, 3, QtWidgets.QTableWidgetItem(query.value(3)))
                var.ui.tabRutas.setItem(index, 4, QtWidgets.QTableWidgetItem(str(query.value(4))))
                var.ui.tabRutas.setItem(index, 5, QtWidgets.QTableWidgetItem(str(query.value(5))))
                var.ui.tabRutas.setItem(index, 6, QtWidgets.QTableWidgetItem(str(query.value(6))))
                total = float(query.value(6)) * float(int(query.value(5)) - int(query.value(4)))
                var.ui.tabRutas.setItem(index, 7, QtWidgets.QTableWidgetItem(str(total)))
                var.ui.tabRutas.item(index, 0).setTextAlignment(QtCore.Qt.AlignCenter)
                var.ui.tabRutas.item(index, 1).setTextAlignment(QtCore.Qt.AlignCenter)
                var.ui.tabRutas.item(index, 4).setTextAlignment(QtCore.Qt.AlignRight)
                var.ui.tabRutas.item(index, 5).setTextAlignment(QtCore.Qt.AlignRight)
                var.ui.tabRutas.item(index, 6).setTextAlignment(QtCore.Qt.AlignRight)
                var.ui.tabRutas.item(index, 7).setTextAlignment(QtCore.Qt.AlignRight)

                index += 1
        # if int(index) > 0:
        #     rutas.Rutas.

        else:
            QtWidgets.QMessageBox.warning(None, 'Haga click para continuar',
                                          query.lastError().text())

    def bajaRuta(numRuta):
        try:
            query = QtSql.QSqlQuery()
            query.prepare('delete from ruta where codigo = :numRuta')
            query.bindValue(':numRuta', int(numRuta))
            if query.exec_():
                QtWidgets.QMessageBox.information(None, 'Ruta Eliminada',
                                                  'Haga Click para Continuar')
            else:
                QtWidgets.QMessageBox.warning(None, query.lastError().text(),
                                              'Haga Click para Continuar')
        except Exception as error:
            print('Cargar ruta. %s:' % str(error))

    @classmethod
    def modifRuta(self, cod, newData):
        query = QtSql.QSqlQuery()

        query.prepare('update ruta set fecha=:fecha, matricula=:matricula, conductor=:conductor '
                      'where codigo=:cod')
        query.bindValue(':codigo', int(cod))
        query.bindValue(':fecha', str(newData[0]))
        query.bindValue(':matricula', str(newData[1]))
        query.bindValue(':conductor', str(newData[2]))
        # query.bindValue(':kmIni', str(newData[3]))
        # query.bindValue(':kmFin', str(newData[4]))
        if query.exec_():
            QtWidgets.QMessageBox.information(None, 'Ruta modificada',
                                              'Haga Click para Continuar')
        else:
            QtWidgets.QMessageBox.warning(None, query.lastError().text(),
                                          'Haga Click para Continuar')
