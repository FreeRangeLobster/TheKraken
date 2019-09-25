#Read on https://www.youtube.com/watch?v=sRNjcyBXruA

from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import json
import cv2
import numpy as np

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel

#piimageseachr
#Shape detector
#detect shapes

def Convert():
    dlg.lineEdit_2.setText(str(float(dlg.lineEdit_1.text())*1.25))

app = QtWidgets.QApplication([])
dlg = uic.loadUi("test.ui")
picName = "Lena.png"

def addItem():
    if not dlg.lineEdit_1.text()=="":
        dlg.listWidget.addItem(dlg.lineEdit_1.text())
        dlg.lineEdit_1.setText("")
    else:
        show_Message("Warning", "Nothing typed")


def GetImageName():
    if not dlg.txtImageFileName.text() == "":
        global picName
        picName = dlg.txtImageFileName.text()
        print(picName)
    else:
        show_Message("Warning", "Nothing typed")


def show_Message(title="Test",message="Test"):
    QMessageBox.information(None,title,message)


def showimageWithQTAndOpenCV(image):
    img = cv2.imread(image,-1)
    height, width, channel = img.shape
    bytesPerLine = 3 * width
    qImg = QImage(img.data, width, height, bytesPerLine, QImage.Format_RGB888).rgbSwapped()
    pixmap = QPixmap.fromImage(qImg)
    dlg.lblImage.setPixmap(pixmap)
    dlg.lblImage.show

def showimageUsingOpenCV(image):
    img = cv2.imread(image, -1)
    cv2.imshow('image',img)
    cv2.waitKey(0)

def showimageUsingOpenCV2():
    img = cv2.imread(picName, -1)
    cv2.imshow('image', img)
    cv2.waitKey(0)


def showimage2(image):
    pixmap = QPixmap('Lena.png')
    dlg.lblImage.setPixmap(pixmap)




def FilterImage(image):
    img = cv2.imread(image)
    #kernel = np.ones((5, 5), np.float32) / 25
    #dst = cv2.filter2D(img, -1, kernel)
    dst = cv2.medianBlur(img,3)
    pixmap = QPixmap(dst)
    dlg.lblImage.setPixmap(pixmap)
    dlg.lblImage.show

def FilterImageAndSave(image):
    image = cv2.imread(image)
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imwrite('C:/Users/Juan/Desktop/TheKraken/OnStage/LenaB.png', image_gray)

    pixmap = QPixmap('LenaB.png')
    dlg.lblImage.setPixmap(pixmap)



def main():
    #showimageUsingOpenCV("Lena.png")
    #show_Message()
    dlg.pushButton.clicked.connect(addItem)
    dlg.cmdGetImageName.clicked.connect(GetImageName)


    #dlg.cmdShowMessage.clicked.connect(show_Message2)
    dlg.cmdShowMessage.clicked.connect(lambda: show_Message('hey','Boy'))
    #dlg.cmdShowImageUsingOpenCV.clicked.connect(lambda: showimageUsingOpenCV("Lena.png"))
    dlg.cmdShowImageUsingOpenCV.clicked.connect(lambda: showimageUsingOpenCV2())
    dlg.cmdShowFilteredImage.clicked.connect(lambda: FilterImageAndSave("Lena.png"))
    #dlg.cmdShowImage.clicked.connect(lambda: showimageWithQTAndOpenCV("Lena.png"))
    dlg.cmdShowImage.clicked.connect(lambda: showimageWithQTAndOpenCV(picName))


    #showimage("Lena.png")
    #FilterImageAndSave("Lena.png")
   # FilterImage("Lena.png")


    showimageWithQTAndOpenCV("Lena.png")



    #dlg.lblimage.text="Hello"

#dlg.lineEdit_1.setFocus()
#dlg.lineEdit_1.setPlaceholderText("£")

if __name__ == '__main__':              # if we're running file directly and not importing it
    main()

#dlg.pushButton.clicked.connect(Convert)
#dlg.pushButton.clicked.connect(Convert)
#dlg.lineEdit_2.setReadOnly(True)


dlg.show()
app.exec()