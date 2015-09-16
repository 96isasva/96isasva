# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 14:59:59 2015

@author: 96isasva
"""

class Crop:
    def __init__(self,growth_rate, light_need, water_need):
        
        self._growth = 0
        self._days_groowing = 0
        self._growth_rate = growth_rate
        self._light_need = light_need
        self._water_need = water_need
        self._status = "Seed"
        self._type = "Generic"
        
def main():
    new_crop = Crop(1,4,3)
    print(new_crop._status)
    print(new_crop._light_need)
    print(new_crop._water_need)
    new_crop2 = Crop(1,5,9)
    print(new_crop2._status)
    print(new_crop2._light_need)
    print(new_crop2._water_need)
    
if __name__ == "__main__":
    main()
