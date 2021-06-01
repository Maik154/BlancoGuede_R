import eventos
import rutas
import var, conexion
import var


class Rutas():
    '''
    Módulos de gestión de rutas
    '''

    def mostrarTarifas(self):
        try:
            var.dlgTarifas.show()
            conexion.Conexion.cargarTarifas(self)
        except Exception as error:
            print('Error mostrar ventana tarifas. %s' % str(error))
            return None

    def cargaUnaRuta(self):
        try:
            fila = var.ui.tabRutas.selectedItems()
            if fila:
                fila = [dato.text() for dato in fila]

            var.ui.lblRuta.setText(fila[0])
            var.ui.txtFecha.setText(fila[1])
            var.ui.cmbMat.setCurrentText(fila[2])
            var.ui.cmbCon.setCurrentText(fila[3])
            var.ui.lblKmTotal.setText(str(int(fila[5]) - int(fila[4])))
            var.ui.lblPrecio.setText(fila[6])

        except Exception as error:
            print('Error cargar ruta %s' % str(error))

    def bajaRuta(self):
        try:
            numRuta = int(var.ui.lblRuta.text())
            conexion.Conexion.bajaRuta(numRuta)
            conexion.Conexion.listarRuta(self)
        except Exception as error:
            print('Error baja ruta %s' % str(error))

    def modificaRuta(self):
        try:
            newData = []
            newData.append(var.ui.txtFecha.text())
            newData.append(var.ui.cmbMat.currentText())
            newData.append(var.ui.cmbCon.currentText())
            # newData.append(var.ui.txtKmIni.text())
            # newData.append(var.ui.txtKmFin.text())
            cod = var.ui.lblRuta.text()
            conexion.Conexion.modifRuta(cod, newData)
            # eventos.Eventos.calculaTarifa(self)
            conexion.Conexion.listarRuta(self)


        except Exception as error:
            print('Error al modificar ruta. %s' % str(error))
