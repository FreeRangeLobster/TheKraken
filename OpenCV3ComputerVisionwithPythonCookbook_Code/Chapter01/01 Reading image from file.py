#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import sys
from PyQt5 import QtWidgets
import cv2

parser = argparse.ArgumentParser()
parser.add_argument('--path', default='../data/Lena.png', help='Image path.')
params = parser.parse_args()

img = cv2.imread(params.path)

# Check if image was successfully read.
assert img is not None

print('read {}'.format(params.path))
print('shape:', img.shape)
print('dtype:', img.dtype)

img = cv2.imread(params.path, cv2.IMREAD_GRAYSCALE)
assert img is not None
print('read {} as grayscale'.format(params.path))
print('shape:', img.shape)
print('dtype:', img.dtype)

def window():

    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QWidget()
    window.SetWindowTitle("Hey")
    window.setGeometry(50,50,500,500)
    window.show()
    sys.exec_info(app.exec_())

window()