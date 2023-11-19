# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 20:34:42 2023

@author: sedak
"""

def f(x):
    return x ** 3 + 4 * x ** 2 - 10

a = 1
b = 2



def ikiye_bolme(a , b , max_iterasyon):
    iterasyon = 0 
    
    
    while iterasyon < max_iterasyon:
        
        c = (a + b) / 2 
        
        if f(c) == 0:
            break
        elif f(c) * f(a) < 0:
            b = c
        else:
            a = c
            
            iterasyon += 1
            
            return (a + b) / 2
        
  max_iterasyon = 4


kok = ikiye_bolme(a, b, max_iterasyon)    

print(f"denklemin koku: {kok}")
    

