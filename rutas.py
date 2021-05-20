from tarifas import *
import var, conexion
from ventana import *
from PyQt5 import QtWidgets
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

