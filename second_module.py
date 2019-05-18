# -*- coding: utf-8 -*-
"""
Created on Fri May 17 11:15:46 2019

@author: John
"""
import os
os.chdir('C:/Users/John/PycharmProjects/corey_schafer_oops')
os.getcwd()

import first_module

first_module.main()

print("Second Module's Name: {}".format(__name__))
