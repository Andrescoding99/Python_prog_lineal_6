"""Una persona desea calcular la temperatura promedio para cada uno de los cinco días de la semana (L a V) 
y la temperatura promedio que se registro en esa semana, Deberá leer por consola la temperatura más alta y baja 
registrada por cada día. Cuando muestre la temperatura promedio de ese día, deberá mostrar el nombre del día y 
mostrar que tipo de día fue"""

"""Temperatura promedio                Tipo de dia

Debajo de los 20                    Dia muy frio
Entre los 21 y 31                   Dia con clima agradable
Arriba de los 31                    Dia muy caliente"""

print("Calculo de temperaturas de dias de la semana")

lun1 = 0
lun2 = 0
lun3 = 0
lunT = 0 #lunT significa la suma de las 3 temperaturas del dia lunes

mar1 = 0
mar2 = 0
mar3 = 0
marT = 0 #marT significa la suma de las 3 tempraturas del dia martes

mie1 = 0
mie2 = 0
mie3 = 0
mieT = 0 #mieT significa la suma de las 3 tempraturas del dia miercoles

jue1 = 0
jue2 = 0
jue3 = 0
jueT = 0 #jueT significa la suma de las 3 tempraturas del dia jueves

vie1 = 0
vie2 = 0
vie3 = 0
vieT = 0 #vieT significa la suma de las 3 tempraturas del dia viernes

FR = "Dia muy frio" #Dia muy frio
AG = "Dia con clima agradable" #Dia con clima agradable
CA = "Dia muy caliente" #Dia muy caliente

tempP1 = 0 #temP1 significa debajo de los 20
tempP2 = 0 #temP2 significa entre los 21 y 31
tempP3 = 0 #temP3 significa arriba de los 32

print("-------------------------------------------------------------------------------------")

print("\nLUNES")

lun1 = int(input("\nIngrese la primera temperatura del dia lunes: "))

while lun1 < -30 or lun1 > 100:
    print("No es posible alcanzar esa temperatura favor ingresar nuevamente")
    lun1 = int(input("Ingrese nuevamente la primera temperatura del dia lunes: "))
print ("La primera temperatura del dia lunes es: {}".format(lun1))

lun2 = int(input("\nIngrese la segunda temperatura del dia lunes: "))

while lun2 < -30 or lun2 > 100:
    print("No es posible alcanzar esa temperatura favor ingresar nuevamente")
    lun2 = int(input("Ingrese nuevamente la segunda temperatura del dia lunes: "))
print ("La segunda temperatura del dia lunes es: {}".format(lun2))

lun3 = int(input("\nIngrese la tercera temperatura del dia lunes: "))

while lun3 < -30 or lun3 > 100:
    print("No es posible alcanzar esa temperatura favor ingresar nuevamente")
    lun3 = int(input("Ingrese nuevamente la tercera temperatura del dia lunes: "))
print ("La tercera temperatura del dia lunes es: {}".format(lun3))

lunT = (lun1 + lun2 + lun2) / 3

if lunT > -30 and lunT <= 20:
    print("\nEl dia es: Lunes")
    print("La temperatura promedio del dia lunes es: {}".format(lunT))
    print("El tipo de dia es: {}".format(FR))
    if lun1 > lun2 and lun1 > lun3:
        print("La temperatura mas alta del dia lunes fue: {}".format(lun1))
    elif lun2 > lun1 and lun2 > lun3:
        print("La temperatura mas alta del dia lunes fue: {}".format(lun2))
    elif lun3 > lun1 and lun3 > lun2:
        print("La temperatura mas alta del dia lunes fue: {}".format(lun3))
    else:
        print("No se puede determinar la temperatura mas alta para el dia lunes")
    if lun1 < lun2 and lun1 < lun3:
            print("La temperatura mas baja del dia lunes fue: {}".format(lun1))
    elif lun2 < lun1 and lun2 < lun3:
                print("La temperatura mas baja del dia lunes fue: {}".format(lun2))
    elif lun3 < lun1 and lun3 < lun2:
            print("La temperatura mas baja del dia lunes fue: {}".format(lun3))
    else:
        print("No se puede determinar la temperatura mas baja para el dia lunes")
elif lunT >= 21 and lunT < 32:
    print("\nEl dia es: Lunes")
    print("La temperatura promedio del dia lunes es: {}".format(lunT))
    print("El tipo de dia es: {}".format(AG))
    if lun1 > lun2 and lun1 > lun3:
        print("La temperatura mas alta del dia lunes fue: {}".format(lun1))
    elif lun2 > lun1 and lun2 > lun3:
        print("La temperatura mas alta del dia lunes fue: {}".format(lun2))
    elif lun3 > lun1 and lun3 > lun2:
        print("La temperatura mas alta del dia lunes fue: {}".format(lun3))
    else:
        print("No se puede determinar la temperatura mas alta para el dia lunes")
    if lun1 < lun2 and lun1 < lun3:
            print("La temperatura mas baja del dia lunes fue: {}".format(lun1))
    elif lun2 < lun1 and lun2 < lun3:
                print("La temperatura mas baja del dia lunes fue: {}".format(lun2))
    elif lun3 < lun1 and lun3 < lun2:
            print("La temperatura mas baja del dia lunes fue: {}".format(lun3))
    else:
        print("No se puede determinar la temperatura mas baja para el dia lunes")
elif lunT >= 32 and lunT < 101:
    print("\nEl dia es: Lunes")
    print("La temperatura promedio del dia lunes es: {}".format(lunT))
    print("El tipo de dia es: {}".format(CA))
    if lun1 > lun2 and lun1 > lun3:
        print("La temperatura mas alta del dia lunes fue: {}".format(lun1))
    elif lun2 > lun1 and lun2 > lun3:
        print("La temperatura mas alta del dia lunes fue: {}".format(lun2))
    elif lun3 > lun1 and lun3 > lun2:
        print("La temperatura mas alta del dia lunes fue: {}".format(lun3))
    else:
        print("No se puede determinar la temperatura mas alta para el dia lunes")
    if lun1 < lun2 and lun1 < lun3:
            print("La temperatura mas baja del dia lunes fue: {}".format(lun1))
    elif lun2 < lun1 and lun2 < lun3:
                print("La temperatura mas baja del dia lunes fue: {}".format(lun2))
    elif lun3 < lun1 and lun3 < lun2:
            print("La temperatura mas baja del dia lunes fue: {}".format(lun3))
    else:
        print("No se puede determinar la temperatura mas baja para el dia lunes")
else:
    print("La temperatura esta fuera de rango para el dia lunes")


print("-------------------------------------------------------------------------------------")

print("\nMARTES")

mar1 = int(input("\nIngrese la primera temperatura del dia martes: "))

while mar1 < -30 or mar1 > 100:
    print("No es posible alcanzar esa temperatura favor ingresar nuevamente")
    mar1 = int(input("Ingrese nuevamente la primera temperatura del dia martes: "))
print ("La primera temperatura del dia martes es: {}".format(mar1))

mar2 = int(input("\nIngrese la segunda temperatura del dia martes: "))

while mar2 < -30 or mar2 > 100:
    print("No es posible alcanzar esa temperatura favor ingresar nuevamente")
    mar2 = int(input("Ingrese nuevamente la segunda temperatura del dia martes: "))
print ("La segunda temperatura del dia martes es: {}".format(mar2))

mar3 = int(input("\nIngrese la tercera temperatura del dia martes: "))

while mar3 < -30 or mar3 > 100:
    print("No es posible alcanzar esa temperatura favor ingresar nuevamente")
    mar3 = int(input("Ingrese nuevamente la tercera temperatura del dia martes: "))
print ("La tercera temperatura del dia martes es: {}".format(mar3))

marT = (mar1 + mar2 + mar2) / 3

if marT > -30 and marT <= 20:
    print("\nEl dia es: martes")
    print("La temperatura promedio del dia martes es: {}".format(marT))
    print("El tipo de dia es: {}".format(FR))
    if mar1 > mar2 and mar1 > mar3:
        print("La temperatura mas alta del dia martes fue: {}".format(mar1))
    elif mar2 > mar1 and mar2 > mar3:
        print("La temperatura mas alta del dia martes fue: {}".format(mar2))
    elif mar3 > mar1 and mar3 > mar2:
        print("La temperatura mas alta del dia martes fue: {}".format(mar3))
    else:
        print("No se puede determinar la temperatura mas alta para el dia martes")
    if mar1 < mar2 and mar1 < mar3:
            print("La temperatura mas baja del dia martes fue: {}".format(mar1))
    elif mar2 < mar1 and mar2 < mar3:
                print("La temperatura mas baja del dia martes fue: {}".format(mar2))
    elif mar3 < mar1 and mar3 < mar2:
            print("La temperatura mas baja del dia martes fue: {}".format(mar3))
    else:
        print("No se puede determinar la temperatura mas baja para el dia martes")
elif marT >= 21 and marT < 32:
    print("\nEl dia es: martes")
    print("La temperatura promedio del dia martes es: {}".format(marT))
    print("El tipo de dia es: {}".format(AG))
    if mar1 > mar2 and mar1 > mar3:
        print("La temperatura mas alta del dia martes fue: {}".format(mar1))
    elif mar2 > mar1 and mar2 > mar3:
        print("La temperatura mas alta del dia martes fue: {}".format(mar2))
    elif mar3 > mar1 and mar3 > mar2:
        print("La temperatura mas alta del dia martes fue: {}".format(mar3))
    else:
        print("No se puede determinar la temperatura mas alta para el dia martes")
    if mar1 < mar2 and mar1 < mar3:
            print("La temperatura mas baja del dia martes fue: {}".format(mar1))
    elif mar2 < mar1 and mar2 < mar3:
                print("La temperatura mas baja del dia martes fue: {}".format(mar2))
    elif mar3 < mar1 and mar3 < mar2:
            print("La temperatura mas baja del dia martes fue: {}".format(mar3))
    else:
        print("No se puede determinar la temperatura mas baja para el dia martes")
elif marT >= 32 and marT < 101:
    print("\nEl dia es: martes")
    print("La temperatura promedio del dia martes es: {}".format(marT))
    print("El tipo de dia es: {}".format(CA))
    if mar1 > mar2 and mar1 > mar3:
        print("La temperatura mas alta del dia martes fue: {}".format(mar1))
    elif mar2 > mar1 and mar2 > mar3:
        print("La temperatura mas alta del dia martes fue: {}".format(mar2))
    elif mar3 > mar1 and mar3 > mar2:
        print("La temperatura mas alta del dia martes fue: {}".format(mar3))
    else:
        print("No se puede determinar la temperatura mas alta para el dia martes")
    if mar1 < mar2 and mar1 < mar3:
            print("La temperatura mas baja del dia martes fue: {}".format(mar1))
    elif mar2 < mar1 and mar2 < mar3:
                print("La temperatura mas baja del dia martes fue: {}".format(mar2))
    elif mar3 < mar1 and mar3 < mar2:
            print("La temperatura mas baja del dia martes fue: {}".format(mar3))
    else:
        print("No se puede determinar la temperatura mas baja para el dia martes")
else:
    print("La temperatura esta fuera de rango para el dia martes")

print("-------------------------------------------------------------------------------------")

print("\nMIERCOLES")

mie1 = int(input("\nIngrese la primera temperatura del dia miercoles: "))

while mie1 < -30 or mie1 > 100:
    print("No es posible alcanzar esa temperatura favor ingresar nuevamente")
    mie1 = int(input("Ingrese nuevamente la primera temperatura del dia miercoles: "))
print ("La primera temperatura del dia miercoles es: {}".format(mie1))

mie2 = int(input("\nIngrese la segunda temperatura del dia miercoles: "))

while mie2 < -30 or mie2 > 100:
    print("No es posible alcanzar esa temperatura favor ingresar nuevamente")
    mie2 = int(input("Ingrese nuevamente la segunda temperatura del dia miercoles: "))
print ("La segunda temperatura del dia miercoles es: {}".format(mie2))

mie3 = int(input("\nIngrese la tercera temperatura del dia miercoles: "))

while mie3 < -30 or mie3 > 100:
    print("No es posible alcanzar esa temperatura favor ingresar nuevamente")
    mie3 = int(input("Ingrese nuevamente la tercera temperatura del dia miercoles: "))
print ("La tercera temperatura del dia miercoles es: {}".format(mie3))

mieT = (mie1 + mie2 + mie2) / 3

if mieT > -30 and mieT <= 20:
    print("\nEl dia es: miercoles")
    print("La temperatura promedio del dia miercoles es: {}".format(mieT))
    print("El tipo de dia es: {}".format(FR))
    if mie1 > mie2 and mie1 > mie3:
        print("La temperatura mas alta del dia miercoles fue: {}".format(mie1))
    elif mie2 > mie1 and mie2 > mie3:
        print("La temperatura mas alta del dia miercoles fue: {}".format(mie2))
    elif mie3 > mie1 and mie3 > mie2:
        print("La temperatura mas alta del dia miercoles fue: {}".format(mie3))
    else:
        print("No se puede determinar la temperatura mas alta para el dia miercoles")
    if mie1 < mie2 and mie1 < mie3:
            print("La temperatura mas baja del dia miercoles fue: {}".format(mie1))
    elif mie2 < mie1 and mie2 < mie3:
                print("La temperatura mas baja del dia miercoles fue: {}".format(mie2))
    elif mie3 < mie1 and mie3 < mie2:
            print("La temperatura mas baja del dia miercoles fue: {}".format(mie3))
    else:
        print("No se puede determinar la temperatura mas baja para el dia miercoles")
elif mieT >= 21 and mieT < 32:
    print("\nEl dia es: miercoles")
    print("La temperatura promedio del dia miercoles es: {}".format(mieT))
    print("El tipo de dia es: {}".format(AG))
    if mie1 > mie2 and mie1 > mie3:
        print("La temperatura mas alta del dia miercoles fue: {}".format(mie1))
    elif mie2 > mie1 and mie2 > mie3:
        print("La temperatura mas alta del dia miercoles fue: {}".format(mie2))
    elif mie3 > mie1 and mie3 > mie2:
        print("La temperatura mas alta del dia miercoles fue: {}".format(mie3))
    else:
        print("No se puede determinar la temperatura mas alta para el dia miercoles")
    if mie1 < mie2 and mie1 < mie3:
            print("La temperatura mas baja del dia miercoles fue: {}".format(mie1))
    elif mie2 < mie1 and mie2 < mie3:
                print("La temperatura mas baja del dia miercoles fue: {}".format(mie2))
    elif mie3 < mie1 and mie3 < mie2:
            print("La temperatura mas baja del dia miercoles fue: {}".format(mie3))
    else:
        print("No se puede determinar la temperatura mas baja para el dia miercoles")
elif mieT >= 32 and mieT < 101:
    print("\nEl dia es: miercoles")
    print("La temperatura promedio del dia miercoles es: {}".format(mieT))
    print("El tipo de dia es: {}".format(CA))
    if mie1 > mie2 and mie1 > mie3:
        print("La temperatura mas alta del dia miercoles fue: {}".format(mie1))
    elif mie2 > mie1 and mie2 > mie3:
        print("La temperatura mas alta del dia miercoles fue: {}".format(mie2))
    elif mie3 > mie1 and mie3 > mie2:
        print("La temperatura mas alta del dia miercoles fue: {}".format(mie3))
    else:
        print("No se puede determinar la temperatura mas alta para el dia miercoles")
    if mie1 < mie2 and mie1 < mie3:
            print("La temperatura mas baja del dia miercoles fue: {}".format(mie1))
    elif mie2 < mie1 and mie2 < mie3:
                print("La temperatura mas baja del dia miercoles fue: {}".format(mie2))
    elif mie3 < mie1 and mie3 < mie2:
            print("La temperatura mas baja del dia miercoles fue: {}".format(mie3))
    else:
        print("No se puede determinar la temperatura mas baja para el dia miercoles")
else:
    print("La temperatura esta fuera de rango para el dia miercoles")


print("-------------------------------------------------------------------------------------")

print("\nJUEVES")

jue1 = int(input("\nIngrese la primera temperatura del dia jueves: "))

while jue1 < -30 or jue1 > 100:
    print("No es posible alcanzar esa temperatura favor ingresar nuevamente")
    jue1 = int(input("Ingrese nuevamente la primera temperatura del dia jueves: "))
print ("La primera temperatura del dia jueves es: {}".format(jue1))

jue2 = int(input("\nIngrese la segunda temperatura del dia jueves: "))

while jue2 < -30 or jue2 > 100:
    print("No es posible alcanzar esa temperatura favor ingresar nuevamente")
    jue2 = int(input("Ingrese nuevamente la segunda temperatura del dia jueves: "))
print ("La segunda temperatura del dia jueves es: {}".format(jue2))

jue3 = int(input("\nIngrese la tercera temperatura del dia jueves: "))

while jue3 < -30 or jue3 > 100:
    print("No es posible alcanzar esa temperatura favor ingresar nuevamente")
    jue3 = int(input("Ingrese nuevamente la tercera temperatura del dia jueves: "))
print ("La tercera temperatura del dia jueves es: {}".format(jue3))

jueT = (jue1 + jue2 + jue2) / 3

if jueT > -30 and jueT <= 20:
    print("\nEl dia es: jueves")
    print("La temperatura promedio del dia jueves es: {}".format(jueT))
    print("El tipo de dia es: {}".format(FR))
    if jue1 > jue2 and jue1 > jue3:
        print("La temperatura mas alta del dia jueves fue: {}".format(jue1))
    elif jue2 > jue1 and jue2 > jue3:
        print("La temperatura mas alta del dia jueves fue: {}".format(jue2))
    elif jue3 > jue1 and jue3 > jue2:
        print("La temperatura mas alta del dia jueves fue: {}".format(jue3))
    else:
        print("No se puede determinar la temperatura mas alta para el dia jueves")
    if jue1 < jue2 and jue1 < jue3:
            print("La temperatura mas baja del dia jueves fue: {}".format(jue1))
    elif jue2 < jue1 and jue2 < jue3:
                print("La temperatura mas baja del dia jueves fue: {}".format(jue2))
    elif jue3 < jue1 and jue3 < jue2:
            print("La temperatura mas baja del dia jueves fue: {}".format(jue3))
    else:
        print("No se puede determinar la temperatura mas baja para el dia jueves")
elif jueT >= 21 and jueT < 32:
    print("\nEl dia es: jueves")
    print("La temperatura promedio del dia jueves es: {}".format(jueT))
    print("El tipo de dia es: {}".format(AG))
    if jue1 > jue2 and jue1 > jue3:
        print("La temperatura mas alta del dia jueves fue: {}".format(jue1))
    elif jue2 > jue1 and jue2 > jue3:
        print("La temperatura mas alta del dia jueves fue: {}".format(jue2))
    elif jue3 > jue1 and jue3 > jue2:
        print("La temperatura mas alta del dia jueves fue: {}".format(jue3))
    else:
        print("No se puede determinar la temperatura mas alta para el dia jueves")
    if jue1 < jue2 and jue1 < jue3:
            print("La temperatura mas baja del dia jueves fue: {}".format(jue1))
    elif jue2 < jue1 and jue2 < jue3:
                print("La temperatura mas baja del dia jueves fue: {}".format(jue2))
    elif jue3 < jue1 and jue3 < jue2:
            print("La temperatura mas baja del dia jueves fue: {}".format(jue3))
    else:
        print("No se puede determinar la temperatura mas baja para el dia jueves")
elif jueT >= 32 and jueT < 101:
    print("\nEl dia es: jueves")
    print("La temperatura promedio del dia jueves es: {}".format(jueT))
    print("El tipo de dia es: {}".format(CA))
    if jue1 > jue2 and jue1 > jue3:
        print("La temperatura mas alta del dia jueves fue: {}".format(jue1))
    elif jue2 > jue1 and jue2 > jue3:
        print("La temperatura mas alta del dia jueves fue: {}".format(jue2))
    elif jue3 > jue1 and jue3 > jue2:
        print("La temperatura mas alta del dia jueves fue: {}".format(jue3))
    else:
        print("No se puede determinar la temperatura mas alta para el dia jueves")
    if jue1 < jue2 and jue1 < jue3:
            print("La temperatura mas baja del dia jueves fue: {}".format(jue1))
    elif jue2 < jue1 and jue2 < jue3:
                print("La temperatura mas baja del dia jueves fue: {}".format(jue2))
    elif jue3 < jue1 and jue3 < jue2:
            print("La temperatura mas baja del dia jueves fue: {}".format(jue3))
    else:
        print("No se puede determinar la temperatura mas baja para el dia jueves")
else:
    print("La temperatura esta fuera de rango para el dia jueves")


print("-------------------------------------------------------------------------------------")

print("\nVIERNES")

vie1 = int(input("\nIngrese la primera temperatura del dia viernes: "))

while vie1 < -30 or vie1 > 100:
    print("No es posible alcanzar esa temperatura favor ingresar nuevamente")
    vie1 = int(input("Ingrese nuevamente la primera temperatura del dia viernes: "))
print ("La primera temperatura del dia viernes es: {}".format(vie1))

vie2 = int(input("\nIngrese la segunda temperatura del dia viernes: "))

while vie2 < -30 or vie2 > 100:
    print("No es posible alcanzar esa temperatura favor ingresar nuevamente")
    vie2 = int(input("Ingrese nuevamente la segunda temperatura del dia viernes: "))
print ("La segunda temperatura del dia viernes es: {}".format(vie2))

vie3 = int(input("\nIngrese la tercera temperatura del dia viernes: "))

while vie3 < -30 or vie3 > 100:
    print("No es posible alcanzar esa temperatura favor ingresar nuevamente")
    vie3 = int(input("Ingrese nuevamente la tercera temperatura del dia viernes: "))
print ("La tercera temperatura del dia viernes es: {}".format(vie3))

vieT = (vie1 + vie2 + vie2) / 3

if vieT > -30 and vieT <= 20:
    print("\nEl dia es: viernes")
    print("La temperatura promedio del dia viernes es: {}".format(vieT))
    print("El tipo de dia es: {}".format(FR))
    if vie1 > vie2 and vie1 > vie3:
        print("La temperatura mas alta del dia viernes fue: {}".format(vie1))
    elif vie2 > vie1 and vie2 > vie3:
        print("La temperatura mas alta del dia viernes fue: {}".format(vie2))
    elif vie3 > vie1 and vie3 > vie2:
        print("La temperatura mas alta del dia viernes fue: {}".format(vie3))
    else:
        print("No se puede determinar la temperatura mas alta para el dia viernes")
    if vie1 < vie2 and vie1 < vie3:
            print("La temperatura mas baja del dia viernes fue: {}".format(vie1))
    elif vie2 < vie1 and vie2 < vie3:
                print("La temperatura mas baja del dia viernes fue: {}".format(vie2))
    elif vie3 < vie1 and vie3 < vie2:
            print("La temperatura mas baja del dia viernes fue: {}".format(vie3))
    else:
        print("No se puede determinar la temperatura mas baja para el dia viernes")
elif vieT >= 21 and vieT < 32:
    print("\nEl dia es: viernes")
    print("La temperatura promedio del dia viernes es: {}".format(vieT))
    print("El tipo de dia es: {}".format(AG))
    if vie1 > vie2 and vie1 > vie3:
        print("La temperatura mas alta del dia viernes fue: {}".format(vie1))
    elif vie2 > vie1 and vie2 > vie3:
        print("La temperatura mas alta del dia viernes fue: {}".format(vie2))
    elif vie3 > vie1 and vie3 > vie2:
        print("La temperatura mas alta del dia viernes fue: {}".format(vie3))
    else:
        print("No se puede determinar la temperatura mas alta para el dia viernes")
    if vie1 < vie2 and vie1 < vie3:
            print("La temperatura mas baja del dia viernes fue: {}".format(vie1))
    elif vie2 < vie1 and vie2 < vie3:
                print("La temperatura mas baja del dia viernes fue: {}".format(vie2))
    elif vie3 < vie1 and vie3 < vie2:
            print("La temperatura mas baja del dia viernes fue: {}".format(vie3))
    else:
        print("No se puede determinar la temperatura mas baja para el dia viernes")
elif vieT >= 32 and vieT < 101:
    print("\nEl dia es: viernes")
    print("La temperatura promedio del dia viernes es: {}".format(vieT))
    print("El tipo de dia es: {}".format(CA))
    if vie1 > vie2 and vie1 > vie3:
        print("La temperatura mas alta del dia viernes fue: {}".format(vie1))
    elif vie2 > vie1 and vie2 > vie3:
        print("La temperatura mas alta del dia viernes fue: {}".format(vie2))
    elif vie3 > vie1 and vie3 > vie2:
        print("La temperatura mas alta del dia viernes fue: {}".format(vie3))
    else:
        print("No se puede determinar la temperatura mas alta para el dia viernes")
    if vie1 < vie2 and vie1 < vie3:
            print("La temperatura mas baja del dia viernes fue: {}".format(vie1))
    elif vie2 < vie1 and vie2 < vie3:
                print("La temperatura mas baja del dia viernes fue: {}".format(vie2))
    elif vie3 < vie1 and vie3 < vie2:
            print("La temperatura mas baja del dia viernes fue: {}".format(vie3))
    else:
        print("No se puede determinar la temperatura mas baja para el dia viernes")
else:
    print("La temperatura esta fuera de rango para el dia viernes")