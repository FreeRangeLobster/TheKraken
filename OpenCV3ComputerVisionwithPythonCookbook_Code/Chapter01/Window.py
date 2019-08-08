import sys
from PyQt5 import QtWidgets

def window():
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QWidget()
    window.SetWindowTitle("Hey")
    window.setGeometry(50,50,500,500)
    window.show()
    sys.exec_info(app.exec_())

window()