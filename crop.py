# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 14:59:59 2015

@author: 96isasva
"""
import math
import random
class Crop:
    def __init__(self,growth_rate, light_need, water_need):
        
        self._growth = 0
        self._days_growing = 0
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
    def _update_status(self):
        if self._growth > 15:
            self._status = "old"
        
        
    def grow(self,light,water):
        if light >= self._light_need and water >= self._water_need:
            self._growth += self._growth_rate
        self._days_growing += 1
        self._update_status()
    
def autogrow(crop,days):
    for day in range(days):
        light = random.randint(1,10)
        water = random.randint(1,10)
        crop.grow(light,water)

def main():
    new_crop = Crop(1,5,9)
    autogrow(new_crop,30)
    print(new_crop._status)
    print(new_crop.report())

    
if __name__ == "__main__":
    main()
