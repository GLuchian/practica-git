
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

#np.random.seed(10)   #La semilla que tienes que introducir al cambiar el archivo .py (ese 10 puede ser cualquier número)
x=np.random.randint(100)
y=np.random.randint(100)
z=np.random.randint(100)
suma=(x+y)+z

print("(",x," + ",y,") + ",z," = ",suma)
