
##======================================================##
##                                                      ##
##   Práctica GIT                                       ##
##                                                      ##
##   Autores:                                           ##
##   Erik Johannes Orihuela Nilsson                     ##
##   George Ababei                                      ##
##                                                      ##
##======================================================##



import numpy as np

print("Suma de tres números aleatorios: ")
print(" ")

np.random.seed(0) #Preparamos la semilla
x=np.random.randint(100)
y=np.random.randint(100)
z=np.random.randint(100)
suma=x+y+z

print(x," + ",y," + ",z," = ",suma)
