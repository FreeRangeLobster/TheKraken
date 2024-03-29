#Read on https://www.youtube.com/watch?v=sRNjcyBXruA

from PyQt5 import QtWidgets, uic, QtSerialPort,QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import json
import cv2
import numpy as np
import imutils
import First
import sys
import glob
import serial #only used to list ports available



from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel

#piimageseachr
#Shape detector
#detect shapes

def Convert():
    dlg.lineEdit_2.setText(str(float(dlg.lineEdit_1.text())*1.25))

@QtCore.pyqtSlot()
def send(self):
        a = "$$" + "\r\n"
        #self.serial.write(a.encode())


def ParseMessage_MachineStatus(sMessage):
    sStatusList = (sMessage.split(',', 1))
    sStatus=sStatusList[0]
    sStatus=sStatus.replace("<", "")
    return sStatus

@QtCore.pyqtSlot()
def receive():
    while Qserial.canReadLine():
        text = Qserial.readLine().data().decode()
        text = text.rstrip('\r\n')
        sStatus=ParseMessage_MachineStatus(text)
        print(sStatus)
        dlg.lineRobotStatus.setText(sStatus)
        dlg.listWidget.addItem(text)
        dlg.listWidget.scrollToBottom()

app = QtWidgets.QApplication([])
dlg = uic.loadUi("test.ui")
Qserial = QtSerialPort.QSerialPort('COM4', baudRate=QtSerialPort.QSerialPort.Baud9600,readyRead=receive)
#serial.open(QtCore.QIODevice.ReadWrite)




picName = "Lena.png"
bTimerEnabled = 0
bColour =1


def addItem():
    if not dlg.lineEdit_1.text()=="":
        dlg.listWidget.addItem(dlg.lineEdit_1.text())
        dlg.lineEdit_1.setText("")
    else:
        show_Message("Warning", "Nothing typed")

def SendCommand():
    if not dlg.lineCommand.text()=="":
        dlg.listWidget.addItem("Command:  " + dlg.lineCommand.text())
        a = dlg.lineCommand.text() + "\r\n"
        Qserial.write(a.encode())



        #dlg.lineEdit_1.setText("")
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
    a = "$$" + "\r\n"
    Qserial.write(a.encode())

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

def GaussianFilter(image):
    image = cv2.imread(image)
    resized = imutils.resize(image, width=300)
    ratio = image.shape[0] / float(resized.shape[0])
    gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    cv2.imshow("Image Blurred", blurred)
    thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]


    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    cv2.imshow("Image Blurred", thresh)
    print(cnts)

    for c in cnts:
        # compute the center of the contour, then detect the name of the
        # shape using only the contour
        M = cv2.moments(c)
        cX = int((M["m10"] / M["m00"]) * ratio)
        cY = int((M["m01"] / M["m00"]) * ratio)
        #shape = sd.detect(c)

        # multiply the contour (x, y)-coordinates by the resize ratio,
        # then draw the contours and the name of the shape on the image
        c = c.astype("float")
        c *= ratio
        c = c.astype("int")
        cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
        #cv2.putText(image, shape, (cX, cY), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

        # show the output image
        cv2.imshow("Image", image)
        cv2.waitKey(0)

    cv2.waitKey(0)

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


def OpenPort():
    sSerialPort = dlg.cBoxPortList.currentText()
    print(sSerialPort)
    Qserial.open(QtCore.QIODevice.ReadWrite)

def GetStatusReport():
    a = "?" + "\r\n"
    Qserial.write(a.encode())
    #dlg.cmdGetStatusReport.setColor(self.backgroundRole(), Qt.white)
    dlg.cmdGetStatusReport.setStyleSheet("background-color: red")

#def Move(Direction,Distance):
#    if Direction
#    a = "?" + "\r\n"
#    serial.write(a.encode())


def timerEvent():
    global bTimerEnabled
    global bColour
    if bTimerEnabled == 1 :
        global time
        time = time.addSecs(1)
        print(time.toString("hh:mm:ss"))
        a = "?" + "\r\n"
        Qserial.write(a.encode())
        First.foo()
        if bColour == 1:
            bColour = 0
            dlg.lblLoop.setStyleSheet("background-color: red")
        else:
            bColour = 1
            dlg.lblLoop.setStyleSheet("background-color: white")

def enablePeriodicUpdate():
    #QColor
    global bTimerEnabled
    if bTimerEnabled == 0:
        # dlg.lblLoop.setStyleSheet("background-color: red")
        dlg.cmdPeriodicUpdate.setStyleSheet("background-color: green")
        bTimerEnabled = 1

    else:
        bTimerEnabled = 0
        dlg.cmdPeriodicUpdate.setStyleSheet("background-color: gray")
        # dlg.lblLoop.setStyleSheet("background-color: white")

        # Gets the colour of the button
    color = dlg.lblLoop.palette().button().color()
    print(color.name())


def serial_ports():
    """ Lists serial port names
        :raises EnvironmentError:
            On unsupported or unknown platforms
        :returns:
            A list of the serial ports available on the system
    """
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
            dlg.cBoxPortList.addItem(port)
        except (OSError, serial.SerialException):
            pass
    return result





def main():
   # w = Widget()
   # w.show()
    print(serial_ports())

    #Bindings
    showimageWithQTAndOpenCV("Lena.png")
    dlg.pushButton.clicked.connect(addItem)
    dlg.cmdSendCommand.clicked.connect(SendCommand)
    dlg.cmdGetImageName.clicked.connect(GetImageName)
    dlg.cmdShowMessage.clicked.connect(lambda: show_Message('hey','Boy'))
    dlg.cmdShowImageUsingOpenCV.clicked.connect(lambda: showimageUsingOpenCV2())
    dlg.cmdShowFilteredImage.clicked.connect(lambda: FilterImageAndSave("Lena.png"))
    dlg.cmdShowImage.clicked.connect(lambda: showimageWithQTAndOpenCV(picName))
    dlg.cmdGaussianBlur.clicked.connect(lambda: GaussianFilter(picName))
    dlg.cmdOpenPort.clicked.connect(lambda: OpenPort())
    dlg.cmdGetStatusReport.clicked.connect(lambda: GetStatusReport())
    dlg.cmdPeriodicUpdate.clicked.connect(lambda: enablePeriodicUpdate())








    #showimage("Lena.png")
    #FilterImageAndSave("Lena.png")
    #FilterImage("Lena.png")








#dlg.lineEdit_1.setFocus()
#dlg.lineEdit_1.setPlaceholderText("£")

if __name__ == '__main__':              # if we're running file directly and not importing it
    timer = QtCore.QTimer()
    time = QtCore.QTime(0, 0, 0)

    main()

    #Timer
    timer.timeout.connect(timerEvent)
    timer.start(3000)





dlg.show()
app.exec()