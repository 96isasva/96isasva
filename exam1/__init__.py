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
        
        self.resize(325,375)
        

        self.nametext = QLabel('namn :',self)
        self.nametext.move(50,50)
        
        self.name = QLineEdit(self)
        self.name.setMinimumWidth(130)
        self.form_layout.addRow('namn: ', self.name)
        self.name.move(100,50)
        #self.led.returnPressed.connect()
        
        self.weighttext = QLabel('vikt : ',self)
        self.weighttext.move(50,100)        
        
        self.weight = QLineEdit(self)
        self.weight.setMinimumWidth(130)
        self.form_layout.addRow('vikt: ', self.name)
        self.weight.move(100,100)
        
        self.colortext = QLabel('färg : ',self)
        self.colortext.move(50,150)
        
        self.color = QLineEdit(self)
        self.color.setMinimumWidth(130)
        self.form_layout.addRow('färg: ', self.name)
        self.color.move(100,150)
        
        self.fordon = QComboBox(self)
        self.fordon.addItem("Välj fordon:")
        self.fordon.addItem("Car")
        self.fordon.addItem("buss")
        self.fordon.move(115,200)
        self.fordon.activated.connect(self.aktiverad) 
        #self.led.returnPressed.connect()
        
   #def aktiverad(self):
   #     self.fordon = QComboBox(self)
    #    self.fordon.addItem("Välj fordon:")
     #   self.fordon.addItem("Bil")
      #  self.fordon.addItem("buss")
       # self.fordon.move(30,30)
        #self.led.returnPressed.connect()
        
        
        self.btn_ok = QPushButton("ok",self)
        self.btn_ok.move(115,250)
        #self.btn_ok.clicked.connect()
        
        self.btn_clear = QPushButton("rensa",self)
        self.btn_clear.move(115,300)
        self.btn_clear.clicked.connect(self.clear)
          
    def aktiverad(self):
        self.fordon2 = QComboBox(self)
        self.fordon2.addItem("Välj fordon:")
        self.fordon2.addItem("Bil")
        self.fordon2.addItem("buss")
        self.fordon2.move(30,30)
        self.colortext.move(10,10)
        print("TEST")
        self.update()
        #self.led.returnPressed.connect()

        
    def clear(self):
        self.name.setText("")
        self.weight.setText("")
        self.color.setText("")
        
        
    def run(self):
        self.show()
        sys.exit(app.exec_())
        

app = QApplication(sys.argv)
Exam().run()

