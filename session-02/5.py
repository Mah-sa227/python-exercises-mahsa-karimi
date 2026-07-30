# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 22:08:26 2026

@author: user
"""

k=int(input('enter kilometr:'))
price="20.000 t"

if k<=2:
    print("price is :",price)
  
else:
        price=((k-2)*5000)+20000
        print("price is :",price,"toman")
        