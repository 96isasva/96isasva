# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 14:59:59 2015

@author: 96isasva
"""
import math
class Crop:
    def __init__(self,growth_rate, light_need, water_need):
        
        self._growth = 0
        self._days_groowing = 0
        self._growth_rate = growth_rate
        self._light_need = light_need
        self._water_need = water_need
        self._status = "Seed"
        self._type = "Generic"
    
    def needs(self):
        return {'light_need':self._light_need, 'water_need':self._water_need}
    def report(self):
        return {'type':self._type,'status':self._status,'growth':self._status}
    
    def set_growth(self,value):
        self._growth = value
    def get_growth(self):
        return (self._growth)

def main():
    new_crop = Crop(1,4,3)
    print(new_crop.needs())
    print(new_crop.report())
    new_crop2 = Crop(1,5,9)
    print(new_crop2._status)
    print(new_crop2._light_need)
    print(new_crop2._water_need)
    help(Crop)
    help(math)
    print(math)
    new_crop.set_growth(5)
    
if __name__ == "__main__":
    main()
