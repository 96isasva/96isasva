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
        self.layout = QVBoxLayout()
        self.form_layout = QFormLayout()
        
        self.inputs = QTextEdit(self)
        self.inputs.setReadOnly(True)
        self.form_layout.addRow('Inputs: ',self.inputs)
        
        self.name = QLineEdit(self)
        self.name.setMinimumWidth(130)
        self.form_layout.addRow('Input: ', self.name)
        self.name.move(50,50)
        #self.led.returnPressed.connect()
        
        self.inputs = QTextEdit(self)
        self.inputs.setReadOnly(True)
        self.form_layout.addRow('Inputs: ',self.inputs)
        
        self.name = QLineEdit(self)
        self.name.setMinimumWidth(130)
        self.form_layout.addRow('Input: ', self.name)
        self.name.move(300,50)
        #self.led.returnPressed.connect()
        
        
        self.btn_ok = QPushButton("ok",self)
        self.btn_ok.move(150,150)
        #self.btn_ok.clicked.connect()
        
        self.btn_clear = QPushButton("rensa",self)
        self.btn_clear.move(100,100)
        #self.btn_ok.clicked.connect()
        

        
        
        
        
        
    def run(self):
        self.show()
        sys.exit(app.exec_())
        

app = QApplication(sys.argv)
Exam().run()

