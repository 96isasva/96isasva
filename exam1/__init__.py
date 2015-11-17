# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 08:55:47 2015

@author: 96isasva
"""
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import model



class MyProgram(QMainWindow):
    
    def __init__(self, parent=None):  
        super(MyProgram, self).__init__()
        self.setWindowTitle("MyProgram")
        self.initUI()
    
    def initUI(self):
        self.frame = QWidget(self)
        self.setCentralWidget(self.frame)
        
    def run(self):
        self.show()
        sys.exit()
        
MyProgram().run()
app = QApplication(sys.argv)
