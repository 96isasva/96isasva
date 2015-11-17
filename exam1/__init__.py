# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 08:55:47 2015

@author: 96isasva
"""
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *




class Exam(QMainWindow):
    def __init__(self, parent=None):  
        super(Exam, self).__init__()
        self.setWindowTitle("Exam")
        self.initUI()
    
    def initUI(self):
        self.frame = QWidget(self)
        self.setCentralWidget(self.frame)
        
    def run(self):
        self.show()
        sys.exit(app.exec_())
        

app = QApplication(sys.argv)
Exam().run()

