import numpy as np 

def funkcja(liczba,potega):
    x = np.logspace(1,potega,num=liczba,base=2)
    return x 


print(funkcja(2,4))