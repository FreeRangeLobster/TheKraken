#Read on https://www.youtube.com/watch?v=sRNjcyBXruA

from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap


import json



def Convert():
    dlg.lineEdit_2.setText(str(float(dlg.lineEdit_1.text())*1.25))

app = QtWidgets.QApplication([])
dlg = uic.loadUi("test.ui")

def addItem():
    if not dlg.lineEdit_1.text()=="":
        dlg.listWidget.addItem(dlg.lineEdit_1.text())
        dlg.lineEdit_1.setText("")
    else:
        show_Message("Warning", "Nothing typed")


def show_Message(title="Test",message="Test"):
    QMessageBox.information(None,title,message)



show_Message()
dlg.pushButton.clicked.connect(addItem)




#dlg.lineEdit_1.setFocus()
#dlg.lineEdit_1.setPlaceholderText("£")

#dlg.pushButton.clicked.connect(Convert)
#dlg.pushButton.clicked.connect(Convert)
#dlg.lineEdit_2.setReadOnly(True)


dlg.show()
app.exec()