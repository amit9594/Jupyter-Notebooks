# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 15:53:45 2020

@author: user1
"""
# see how to import functions/modules from packages
# . operaor use to grab from see here we grab myprogram.py script module from 
# from main_pacakge_python bcoz it is save under this folder folder is nothing but packages
# and we import directly function which is in myprogram module


from main_package_python.myprogram import my_func,is_even


my_func()

is_even()

# see here how we rab report main() function it is save under main_pacakge_python then
# sub_packages then under that other_sub_script then it is available in this location 
# so import functions whichever u want and call it to run
from main_package_python.sub_package.other_sub_script import report_main
report_main()


# another way to grab same
from main_package_python.sub_package import other_sub_script

other_sub_script.report_main()

# but 1st main package should be import i.e u can't directly access from main package directly
# like this below we have to import atleast one file
#main_pacakge_python.sub_package.other_sub_script.report_main()