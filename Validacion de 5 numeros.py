#2.	Diseñe un algoritmo que capture 5 números del usuario y determinar en cada caso, 
#si se trata de un valor positivo, negativo o nulo (0)

print("Recepción de datos numericos")

"""a = 0
b = 0
c = 0
d = 0
e = 0


a = float (input("\nIngrese el primer valor : "))

b = float (input("\nIngrese el segundo valor : "))

c = float (input("\nIngrese el tercer valor : "))

d = float (input("\nIngrese el cuarto valor : "))

e = float (input("\nIngrese el quinto valor : "))



if a < 0:
    print("\nEl primer valor es negativo")
elif a == 0:
    print("\nEl primer valor es 0 o nulo")
else:
    print("\nEl primer valor es positivo")

if b < 0:
    print("\nEl segundo valor es negativo")
elif b == 0:
    print("\nEl segundo valor es 0 o nulo")
else:
    print("\nEl segundo valor es positivo")

if c < 0:
    print("\nEl tercer valor es negativo")
elif c == 0:
    print("\nEl tercer valor es 0 o nulo")
else:
    print("\nEl tercer valor es positivo")

if d < 0:
    print("\nEl cuarto valor es negativo")
elif d == 0:
    print("\nEl cuarto valor es 0 o nulo")
else:
    print("\nEl cuarto valor es positivo")

if e < 0:
    print("\nEl quinto valor es negativo")
elif e == 0:
    print("\nEl quinto valor es 0 o nulo")
else:
    print("\nEl quinto valor es positivo")"""

numero = 0

i = 0

while i < 6:
    numero = int(input("Ronda {} Favor ingresar un numero: ".format(i + 1)))
    if numero < 0:
        print("El numero es negativo")
    elif numero == 0:
        print("El numero es nulo")
    elif numero > 0:
        print("El numero es positivo")
    i += 1