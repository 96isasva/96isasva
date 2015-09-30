# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 15:06:34 2015

@author: 96isasva
"""

class Animals:
    def __init__(self,growth_rate, food_need, water_need):
        
        self._weight = 0
        self._days_growing = 0
        self._growth_rate = growth_rate
        self._food_need = food_need
        self._water_need = water_need
        self._status = "Seed"
        self._type = "Generic"
        self._name = "kossamu"
    def needs(self):
        return {'food_need':self._food_need, 'water_need':self._water_need}
    
    def grow(self,food,water):
        if food >= self._food_need and water >= self._water_need:
            self._growth += self._growth_rate
        self._days_growing += 1
        self._update_status()
    
    def update_status(self):
         if self._growth > 15:
            self._status = "old"
    def set_type(self,typ):
        self._type = typ
        
        
class Cow(Animals):
    def __init__(self):
        super().__init__(1,3,6)
    
    def grow(self,food,water):
        if food >= self._food_need and water >= self._water_need:
            if self._status == "seeding" and water > self._water_need:
                self._growth += self._growth_rate * 1.5
            elif self._status == "Young" and water > self._water_need:
                self._growth += self._growth_rate * 1.25
            else:
                self._growth += self._growth_rate
        self._days_growing += 1
        self._update_status()
    def set_type(self,typ):
        self._type = typ
        
class Sheep(Animals):
      def __init__(self):
        super().__init__(2,4,7)  

      def grow(self,food,water):
         if food >= self._food_need and water >= self._water_need:
             if self._status == "seeding" and water > self._water_need:
                self._growth += self._growth_rate * 1.75
             elif self._status == "Young" and water > self._water_need:
                self._growth += self._growth_rate * 1.5
             else:
                self._growth += self._growth_rate
         self._days_growing += 1
         self._update_status()
    
      def set_type(self,typ):
        self._type = typ    
    