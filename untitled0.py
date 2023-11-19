def f(x):
    return x ** 3 - 2 * x ** 2 - 5

a = 2
b = 4



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
    

