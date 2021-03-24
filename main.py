import sys
from ventana import *


class Main(QtWidgets.QMainWindow):
    def __init__(self):
        '''
        genera y conecta los eventos
        '''
        super(Main, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    window.setFixedSize(1204, 768)
    window.show()
    sys.exit(app.exec())