#!/usr/bin/python3
'''
Module doc
'''

from models.base import Base

class Rectangle(Base):
    '''
    Rectangle class
    '''
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        '''
        width method
        '''
        return self.width

    @width.setter():
        '''
        with method
        '''
        if 
    

