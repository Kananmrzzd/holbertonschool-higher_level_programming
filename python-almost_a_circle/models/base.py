#!/usr/bin/python3
'''
Model
'''
class Base:
    '''
    Base class
    '''
    __nb_objects = 0

    def __init__(self, id=None):
        '''
        Method Documentation
        '''
        __class__.__nb_objects += 1
        if id is not None:
            self.id = id
        else:
            self.id = __class__.__nb_objects
