"""5.	Mostrar los números en pantalla en base a un limite determinado por el usuario empezando 
desde 0, además, 
preguntar si lo desea visualizar de forma descendiente o ascendente"""


print("Calculo de rango de numeros")

i = 0

lit = 0

ord = ""

lit = int(input("Favor ingresar el limite superior positivo: "))

print("Ordenamiento de datos Ascendente: a \n Descendente: d")

ord = input("Favor ingresar forma de ordenamiento: ")

while ord != "a" and ord != "d":
    print("Valor invalido, ingresa un nuevo valor: ")
    ord = input("Favor ingresar forma de ordenamiento: ") 
print("Valor aceptado")


if ord == "a":
    print("Ascendete")
    for i in range (i,lit):
        print(i)
else:
    print("Descendente")
    while i < lit:
        print(lit)
        lit -= 1
        