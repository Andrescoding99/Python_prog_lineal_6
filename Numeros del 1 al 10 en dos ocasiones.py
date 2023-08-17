#1.	Diseñe un algoritmo muestre los números del 1 al 10, en dos ocasiones antes de pasar 
#al siguiente valor relativo, utilice la estructura de su preferencia. 

"""i = 1

while i < 11:
    print (i)
    print (i)
    i += 1"""

#i = 1

"""numeroVeces = 0 # Este es el controlador que contará el numero de veces, que ha sido mostrado el numero.

while i <= 10:
    print(i)
    numeroVeces += 1
    if numeroVeces == 2:
        i += 1
        numeroVeces == 0"""



lit2 = int(input("Ingrese el ultimo valor del rango para la repeticion: "))

lit2 = lit2 * 2 + 1

numeroVeces2 = 1 # Este es el controlador, pero va a controlar el numero en sí que se muestra

for i in range (1,lit2):
    print(numeroVeces2)
    if i % 2 == 0:
        numeroVeces2 += 1

#------------------------------------------------------------------------------#

"""lit = 10 #Esta es la variable limite, para el numero de vueltas

i = 1
j = 0


while i <= lit:
    j = i + 2
    while j > i:
        print(i)
        j -= 1
    i += 1"""


