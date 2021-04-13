# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 17:50:11 2020

@author: user1
"""

def func():
    print("func() ran in one.py")

print("top-level print inside of one.py")

if __name__ == "__main__":
    print("one.py is being run directly")
else:
    print("one.py is being imported into another module")
    
# outpt:     
#top-level print inside of one.py
#one.py is being run directly


# here name is one and running in one.py so output will execute if statement true
