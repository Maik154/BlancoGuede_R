import os
from datetime import datetime

from PyQt5 import QtSql
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

import var


class Informes:
    def cabecer(self):
        try:
            logo = '.\\img\icono.png'
            var.informe.drawImage(logo, 450, 760)
            var.titulo = 'LISTADO RUTAS'
            var.informe.drawCentredString(290, 750, var.titulo)
            var.informe.line(40, 740, 525, 740)
            var.informe.line(40, 735, 525, 735)
            var.informe.setFont('Helvetica-Bold', size=16)
            var.informe.drawString(50, 790, 'TRANSPORTES BLANCO')

        except Exception as error:
            print('Error cabecera informe. %s' % str(error))

    def informeRutas(self):
        try:
            var.informe = canvas.Canvas('reportes/listadorutas.pdf', pagesize=A4)
            Informes.cabecer(self)
            Informes.pie(self)
            rootPath = '.\\reportes'
            cont = 0
            query = QtSql.QSqlQuery()
            query.prepare('select * from ruta')

            if query.exec_():
                i = 50  # eje horizontal
                j = 690  # altura desde donde empieza a listar
                # cambiar valores pa mover
                # hacer cabecera de valores,  hacer cantidad total de rutas,
                # km totales, cantidad facturada
                while query.next():
                    if j <= 80:
                        var.informe.drawString(440, 70, 'Página siguiente.....')
                    var.informe.setFont('Helvetica', size=10)
                    var.informe.drawString(i, j, str(query.value(0)))
                    var.informe.drawString(i + 50, j, str(query.value(1)))
                    var.informe.drawString(i + 120, j, str(query.value(2)))
                    var.informe.drawString(i + 190, j, str(query.value(3)))
                    var.informe.drawRightString(i + 260, j, str(query.value(4)))
                    var.informe.drawRightString(i + 300, j, str(query.value(5)))
                    var.informe.drawString(i + 330, j, str(query.value(6)))
                    kmt = int(query.value(5)) - int(query.value(4))
                    print(kmt)
                    tarifaTotal = float(kmt) * float(query.value(6))
                    print(tarifaTotal)
                    var.informe.drawRightString(i + 420, j, str('{0:.2f}'.format(float(tarifaTotal)) + ' €'))

                    j = j - 25
            var.informe.save()
            for file in os.listdir(rootPath):
                if file.endswith('listadorutas.pdf'):
                    os.startfile('%s/%s' % (rootPath, file))
                cont += 1
        except Exception as error:
            print('Error cuerpo informe. %s' % str(error))

    def pie(self):
        try:
            #
            var.informe.line(40, 70, 525, 70)
            dia = datetime.now().day
            mes = datetime.now().month
            ano = datetime.now().year
            var.informe.setFont('Helvetica-Oblique', size=12)
            var.informe.drawString(250, 55, var.titulo)
            var.informe.drawString(460, 60, str(dia) + "/" + str(mes) + "/" + str(ano))
        except Exception as error:
            print('Error pie informe. %s' % str(error))
