# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 17:53:30 2020

@author: user1
"""
import one

print("top-level in two.py")

one.func()

if __name__ == "__main__":
    print("two.py is being run directly")
else:
    print("two.py is being imported into another module")
