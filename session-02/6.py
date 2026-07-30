# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 22:43:09 2026

@author: user
"""

cost=int(input("enter price:"))

if cost<500000:
    print("sorry you have'nt any discount :( ")
    
elif 500000<=cost<1000000:
        discount=(cost*10)/100
        cost=cost-discount
        print('your price after discount is:',cost)
        
elif cost>=1000000:
        discount=(cost*15)/100
        cost=cost-discount
        print("your price after discount is:",cost)

