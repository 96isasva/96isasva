# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 15:17:06 2015

@author: 96isasva
"""

from animals.py import *

class Field:
    
    def __init__(self,max_animals,max_crops):
        self._crops = []
        self._animals = []
        self._max_animals = max_animals
        self._max_crops = max_crops
        
def main():
    new_field = Field(5,2)
    print(new_field.crops)
    print(new_field._animals)
    print(new_field._max_animals)
    print(new_field._max_crops)

if __name__ == "__main__":
    main()