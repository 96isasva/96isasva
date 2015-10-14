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
        
    def plant_crop(self,crop):
        if len(self._crops) < self._max_crops:
            self._crops.append(crop)
            return True
        else:
            return False
    def add_animal(self, animal):
        if len(self._animals) < self._max_animals:
            self._animals.append(animal)
            return True
        else:
            return False
            
    def harvest_crop(self,position):
        return self._crops.pop(position)
        
    def remove_animal(self,position):
        return self._crops.pop(position)
    
    def report_contents(self):
        crop_report = []
        animal_report = []
        for crop in self._crops:
            crop_report.append(crop.report())
            
    def report_need(self):
        food = 0
        light = 0
        water = 0
        for crop in self._crops:
            needs = crop.needs()
            if needs["light need"] > light:
                light = needs["light need"]
            if needs["water need"] > water:
                water= needs["water need"]
        for animal in self._animals:
            needs = animal.needs()
            food += needs["food need"]
            if needs["water need"] > water:
                water = needs["water_need"]
        return {"food":food,"light":light,"water":water}
            
 
def auto_grow(field,days):
    for day in range(days):
        light = random.randint(1,10)
        water = random.randint(1,10)
        food = random.randint(1,100)
        field.grow(light,food,water)

def manual_grow(field):
    valid = False
    while not valid:
        try:
            light = int(input("please enter a light value (1-10: "))
            if 1 <= light <= 10:
                vaild = True
            else:
                print("Value entered in not valid - please enter a value between 1 & 10")
        except ValueError:
            print("Value enterd not valid")
            
        valid = False
        while not valid:
            try:
                food = int(input("please enter a food value"))
                if 1 <= food <= 100:
                    valid = True
                else:
                    print("Value entered not valid")
            except ValueError:
                print("Value entered not valid")
                
        field.grow(ligt,food,water)
       
def display_crops(crop_list):
    print()
    print("The following crops are in this field:")
    pos = 1
    for crop in crop_list:
        print("{0:>2}. {1}".format(pos,crop.report())
    pos += 1
def display_animals(animal_list):
    print()
    print ("The following animals are in this field: ")
    pos = 1
    for animal in animal_list:
        print("{0:>2}. {1}".format(pos,animal.report())
    pos += 1

def select_crop(length_list):
    valid = False
    while not valid:
        selected = int(input("Please select a crop: ")):
        if selected in range(1,length_list+1):
            valid = True
        else:
            print("Please selected a valid option")
    return selected - 1
    
def select_animal(length_list):
    valid = False
    while not valid:
        selected = int(input("Please select a animal: ")):
        if selected in range(1,length_list+1):
            valid = True
        else:
            print("Please selected a valid option")
    return selected - 1

def harvest_crop_from_field(field):
    display_crops(field._crops)
    selected_crop = select_crop(len(field._crops))
    return field.harvest_crop(selected_crop)
    
def harvest_animal_from_field(field):
    display_animal(field._animal)
    selected_animal = select_animal(len(field._animals))
    return field.harvest_animal(selected_animal)
    
    
def main():
    new_field = Field(5,2)
    new_field.plant_crop(wheat())
    new_field.plant_crop(potato())
    new_field.add_animal(cow("Jim"))
    new_field.add_animal(sheep("Shaun"))
    harvest_crop_from_field(new_field)
    print(new_field._crops)
    remove_animals_from_field(new_field)
    print(new_field._animals)
    report = new_field.report_needs()
    print report()
    manual_grow(new_field.report_contents())
    print new_field.report_contents()

    
if __name__ == "__main__":
    main()