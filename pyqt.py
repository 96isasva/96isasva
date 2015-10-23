# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 15:07:05 2015

@author: 96isasva
"""
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class CropWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Crop Simulator")

def main():
    crop_simulation = QApplication(sys.argv)
    crop_window = CropWindow()
    crop_window.show()
    crop_window.raise_()
    crop_simulation.exec_()
    
if __name__ == "__main__":
    main()
    