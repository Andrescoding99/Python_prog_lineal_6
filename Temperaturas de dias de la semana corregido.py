"""Una persona desea calcular la temperatura promedio para cada uno de los cinco días de la semana (L a V) 
y la temperatura promedio que se registro en esa semana, Deberá leer por consola la temperatura más alta y baja 
registrada por cada día. Cuando muestre la temperatura promedio de ese día, deberá mostrar el nombre del día y 
mostrar que tipo de día fue"""

"""Temperatura promedio                Tipo de dia

Debajo de los 20                    Dia muy frio
Entre los 21 y 31                   Dia con clima agradable
Arriba de los 31                    Dia muy caliente"""

print("Calculo de temperaturas de dias de la semana")

#Asignacion de variables

tempB = 0
tempA = 0
tempP = 0 #Temperatura promedio diaria
tempPs = 0 #Temperatura promedio semanal

FR = "Dia muy frio" #Dia muy frio
AG = "Dia con clima agradable" #Dia con clima agradable
CA = "Dia muy caliente" #Dia muy caliente


diaAct = 0 #Variable temporal que muestra el dia


#Iterador

i = 0

#Acumulador

acuTempP = 0 #Acumulador de temperaturas promedio

# Captura y muestra de datos

while i < 5:
    #Lectura y validacion de datos
    if i == 0:
        diaAct = "Lunes"
    elif i == 1:
        diaAct = "Martes"
    elif i == 2:
        diaAct = "Miercoles"
    elif i == 3:
        diaAct = "Jueves"
    elif i == 4:
        diaAct = "Viernes"

    tempB = float(input("Favor ingresar la temperatura mas baja para el dia {}: ".format(diaAct)))
    while tempB < -30 or tempB > 100:
        print("No es posible alcanzar esa temperatura favor ingresar nuevamente")
        tempB = float(input("Ingrese nuevamente la temperatura mas baja para el dia {}: ".format(diaAct)))
    print ("La  temperatura mas baja del dia {} es: {} grados celcius \n".format(diaAct,tempB))

    tempA = float(input("Favor ingresar la temperatura mas alta para el dia {}: ".format(diaAct)))
    while tempA < -30 or tempA > 100:
        print("No es posible alcanzar esa temperatura favor ingresar nuevamente")
        tempA = float(input("Ingrese nuevamente la temperatura mas alta para el dia {}: ".format(diaAct)))
    print ("La  temperatura mas alta del dia {} es: {} grados celcius \n".format(diaAct,tempA))


    #Calculo de datos

    tempP = (tempB + tempA) / 2
    print("La temperatura promedio del dia {} es {}".format(diaAct, tempP))

    if tempP > -30 and tempP <= 20:
        print("\nEl tipo de dia es: {}".format(FR))
    elif tempP >= 21 and tempP < 32:
        print("\nEl tipo de dia es: {}".format(AG))
    elif tempP >= 32 and tempP < 101:
        print("\nEl tipo de dia es: {}".format(CA))

    acuTempP += tempP #Si no hacia este paso solo  iba guardar la temperatura del dia viernes es decir el utlimo valor 
    #de dial viernes.

    i += 1

#Temperatura promedio semanal

tempPs = acuTempP / 5

print("La temperatura promedio semanal es: {}".format(tempPs))