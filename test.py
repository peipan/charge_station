#!/usr/bin/env python 
# -*- coding: utf-8 -*-
import sys
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QLabel, QWidget, QApplication

import base64
import io
from PIL import Image

class Demo(QWidget):
    def __init__(self):
        super().__init__()
        pix = QPixmap('UI/image/edge.png')

        lb1 = QLabel(self)
        lb1.setGeometry(0,0,500,210)
        lb1.setStyleSheet("border: 2px solid red")
        lb1.setPixmap(pix)

        lb2 = QLabel(self)
        lb2.setGeometry(0,250,500,210)
        lb2.setPixmap(pix)
        lb2.setStyleSheet("border: 2px solid red")
        lb2.setScaledContents(True)   #自适应QLabel大小

        self.lb3 = QLabel(self)
        self.lb3.setGeometry(0, 500, 500, 210)
        self.lb3.setPixmap(pix)
        self.lb3.setStyleSheet("border: 2px solid red")
        self.lb3.setScaledContents(True)  # 自适应QLabel大小

def set_img_on_label(lb, img_b64):
    img_b64decode = base64.b64decode(img_b64)  #[21:]
    img_io = io.BytesIO(img_b64decode)
    img=Image.open(img_io)
    pix = img.toqpixmap()
    lb.setScaledContents(True)  # 自适应QLabel大小
    lb.setPixmap(pix)

if __name__== '__main__':
    app = QApplication([]);  # argv)
    # icon = QIcon("logo.ico")
    # app.setWindowIcon(icon)
    win = Demo()
    win.show()
    sFile = open("UI/image/edge.png", "rb").read()
    img_b64 = base64.b64encode(sFile)
    set_img_on_label(win.lb3,img_b64)
    sys.exit(app.exec_())