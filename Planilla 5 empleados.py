"""4.	Capturar nombre, año de nacimiento, cargo y salario de 5 empleados:
a)	Calcular el respectivo descuento de renta, AFP e ISSS por cada empleado 
b)	Mostrar nombre, edad, cargo, descuentos realizados y salario neto
c)	Realizar el ejercicio para una cantidad de empleados desconocida
d)	Mostrar la edad media
e)	Mostrar la cantidad de dinero que la empresa deberá destinar al pago de los empleados y detallar cantidad 
para prestaciones y neto"""

print("Calculo de planilla")

# Definicion de variables


no1 = 0 #no es nombre
ed1 = 0 #ed es edad
año1 = 0
g1= 0 #g es genero
salB1 = 0 #salB es salario bruto
car1 = 0 #car es cargo de empleado
emp1DesT = 0 #dest es Descuento total del primer empleado
salN1 = 0 #salN es Salario Neto

no2 = 0 #no es nombre
ed2 = 0 #ed es edad
año2 = 0
g2= 0 #g es genero
salB2 = 0 #salB es salario bruto
car2 = 0 #car es cargo de empleado
emp2DesT = 0 #dest es Descuento total
salN2 = 0 #salN es Salario Neto

no3 = 0 #no es nombre
ed3 = 0 #ed es edad
año3 = 0
g3= 0 #g es genero
salB3 = 0 #salB es salario bruto
car3 = 0 #car es cargo de empleado
emp3DesT= 0 #dest es Descuento total
salN3 = 0 #salN es Salario Neto

no4 = 0 #no es nombre
ed4 = 0 #ed es edad
año4 = 0
g4 = 0 #g es genero
salB4 = 0 #salB es salario bruto
car4 = 0 #car es cargo de empleado
emp4DesT= 0 #dest es Descuento total
salN4 = 0 #salN es Salario Neto

no5 = 0 #no es nombre
ed5 = 0 #ed es edad
año5 = 0
g5 = 0 #g es genero
salB5 = 0 #salB es salario bruto
car5 = 0 #car es cargo de empleado
empDe5sT= 0 #dest es Descuento total
salN5 = 0 #salN es Salario Neto


#Las siguientes variables son para los descuentos de ISSS, AFP
# En el caso de RENTA será una constante dada la mulitplicacion

ISSS = 0.03
des1Isss = 0 #Muestra solo cantidad de descuento del ISSS
des2Isss = 0
des3Isss = 0

AFP = 0.0725
des1Afp = 0 #Muestra solo cantidad de descuento del AFP
des2Afp = 0
des3Afp = 0


RENTA0= 0
RENTA1 = 0.10 # El 10% se mantiene dentro de un rango $472.01 - $895.24
RENTA2 = 0.20 # El 20% se mantiene dentro de un rango $895.25 - $2038.10
RENTA3 = 0.30 # El 30% se mantiene dentro de un rango $2038.11 - $99999

# ESTO ES PARA DECLARAR LAS CONSTANTES DEL DESCUENTO DE RENTA POR EMPLEADO
# CON BASE AL RANGO SALARIAL QUE TIENE

emp1DesRenta = 0
emp2DesRenta = 0
emp3DesRenta = 0
emp4DesRenta = 0
emp5DesRenta = 0

#Esto es para la edad media

edadT = 0 #Esto es la edad total de los empleados

#Esto es para la cantidad total a pagar por parte de la empresa

salNt = 0 #Esto es el salario total neto a pagar por parte de los empleados

# Captura de datos

#Primer empleado

print("\nGénero de los empleados: \nMujeres: f \nHombres: m")
print("\nCargo de los empleados: \nAsistente: a \nJefe: j \nGerente: g")

no1 = input("\nIngrese el nombre del primer empleado: ")
año1 = int(input("Ingrese el año en que nacio el primer empleado: "))

while año1 < 1900 or año1 > 2004:
    print("\nHa ingresado un valor fuera del rango para el año de nacimiento, intente otra vez")
    año1 = int(input("\nIngrese nuevamente el año de nacimiento para el primer empleado: "))
print("Valor de año de nacimiento aceptado para el primer empleado")

g1 = input("\nIngrese el genero del primer empleado: ")

while g1 != "f" and g1 !=  "m":
    print("\nHa ingresado un valor incorrecto para el genero, intente otra vez")
    g1 = input("\nIngrese nuevamente el genero para el primer empleado: ")
print("Valor de genero aceptado para el primer empleado")

salB1 = float(input("\nIngrese el salario base del primer empleado: "))

while salB1 < 365 or salB1 > 4999:
    print("\nHa ingresado un valor fuera del rango para el salario, intente otra vez")
    salB1 = int(input("\nIngrese nuevamente eel salario para el primer empleado: "))
print("Valor de salario aceptado para el primer empleado")

car1 = input("\nIngrese el cargo del primer empleado: ")

while car1 != "a" and car1 != "j" and car1 != "g":
    print("\nHa ingresado un valor incorrecto para el cargo, intente otra vez")
    car1 = input("\nIngrese nuevamente el cargo para el primer empleado: ")
print("Valor de cargo aceptado para el primer empleado")

#Segundo empleado

no2 = input("\nIngrese el nombre del segundo empleado: ")
año2 = int(input("Ingrese el año en que nacio el segundo empleado: "))

while año2 < 1900 or año2 > 2004:
    print("\nHa ingresado un valor fuera del rango para el año de nacimiento, intente otra vez")
    año2 = int(input("\nIngrese nuevamente el año de nacimiento para el segundo empleado: "))
print("Valor de año de nacimiento aceptado para el segundo empleado")

g2 = input("\nIngrese el genero del segundo empleado: ")

while g2 != "f" and g2 !=  "m":
    print("\nHa ingresado un valor incorrecto para el genero, intente otra vez")
    g2 = input("\nIngrese nuevamente el genero para el segundo empleado: ")
print("Valor de genero aceptado para el segundo empleado")

salB2 = float(input("\nIngrese el salario base del segundo empleado: "))

while salB2 < 365 or salB2 > 4999:
    print("\nHa ingresado un valor fuera del rango para el salario, intente otra vez")
    salB2 = int(input("\nIngrese nuevamente el salario para el segundo empleado: "))
print("Valor de salario aceptado para el segundo empleado")

car2 = input("\nIngrese el cargo del segundo empleado: ")

while car2 != "a" and car2 != "j" and car2 != "g":
    print("\nHa ingresado un valor incorrecto para el cargo, intente otra vez")
    car2 = input("\nIngrese nuevamente el cargo para el segundo empleado: ")
print("Valor de cargo aceptado para el segundo empleado")

#Tercer empleado

no3 = input("\nIngrese el nombre del tercer empleado: ")
año3 = int(input("Ingrese el año en que nacio el tercer empleado: "))

while año3 < 1900 or año3 > 2004:
    print("\nHa ingresado un valor fuera del rango para el año de nacimiento, intente otra vez")
    año3 = int(input("\nIngrese nuevamente el año de nacimiento para el tercer empleado: "))
print("Valor de año de nacimiento aceptado para el tercer empleado")

g3 = input("\nIngrese el genero del tercer empleado: ")

while g3 != "f" and g3 !=  "m":
    print("\nHa ingresado un valor incorrecto para el genero, intente otra vez")
    g3 = input("\nIngrese nuevamente el genero para el tercer empleado: ")
print("Valor de genero aceptado para el tercer empleado")

salB3 = float(input("\nIngrese el salario base del tercer empleado: "))

while salB3 < 365 or salB3 > 4999:
    print("\nHa ingresado un valor fuera del rango para el salario, intente otra vez")
    salB3 = int(input("\nIngrese nuevamente el salario para el tercer empleado: "))
print("Valor de salario aceptado para el tercer empleado")

car3 = input("\nIngrese el cargo del tercer empleado: ")

while car3 != "a" and car3 != "j" and car3 != "g":
    print("\nHa ingresado un valor incorrecto para el cargo, intente otra vez")
    car3 = input("\nIngrese nuevamente el cargo para el tercer empleado: ")
print("Valor de cargo aceptado para el tercer empleado")

#Cuarto empleado

no4 = input("\nIngrese el nombre del cuarto empleado: ")
año4 = int(input("Ingrese el año en que nacio el cuarto empleado: "))

while año4 < 1900 or año4 > 2004:
    print("\nHa ingresado un valor fuera del rango para el año de nacimiento, intente otra vez")
    año4 = int(input("\nIngrese nuevamente el año de nacimiento para el cuarto empleado: "))
print("Valor de año de nacimiento aceptado para el cuarto empleado")

g4 = input("\nIngrese el genero del cuarto empleado: ")

while g4 != "f" and g4 !=  "m":
    print("\nHa ingresado un valor incorrecto para el genero, intente otra vez")
    g4 = input("\nIngrese nuevamente el genero para el cuarto empleado: ")
print("Valor de genero aceptado para el cuarto empleado")

salB4 = float(input("\nIngrese el salario base del cuarto empleado: "))

while salB4 < 365 or salB4 > 4999:
    print("\nHa ingresado un valor fuera del rango para el salario, intente otra vez")
    salB4 = int(input("\nIngrese nuevamente el salario para el cuarto empleado: "))
print("Valor de salario aceptado para el cuarto empleado")

car4 = input("\nIngrese el cargo del cuarto empleado: ")

while car4 != "a" and car4 != "j" and car4 != "g":
    print("\nHa ingresado un valor incorrecto para el cargo, intente otra vez")
    car4 = input("\nIngrese nuevamente el cargo para el cuarto empleado: ")
print("Valor de cargo aceptado para el cuarto empleado")

#Quinto empleado

no5 = input("\nIngrese el nombre del quinto empleado: ")
año5 = int(input("Ingrese el año en que nacio el quinto empleado: "))

while año5 < 1900 or año5 > 2004:
    print("\nHa ingresado un valor fuera del rango para el año de nacimiento, intente otra vez")
    año5 = int(input("\nIngrese nuevamente el año de nacimiento para el quinto empleado: "))
print("Valor de año de nacimiento aceptado para el quinto empleado")

g5 = input("\nIngrese el genero del quinto empleado: ")

while g5 != "f" and g5 !=  "m":
    print("\nHa ingresado un valor incorrecto para el genero, intente otra vez")
    g5 = input("\nIngrese nuevamente el genero para el quinto empleado: ")
print("Valor de genero aceptado para el quinto empleado")

salB5 = float(input("\nIngrese el salario base del quinto empleado: "))

while salB5 < 365 or salB5 > 4999:
    print("\nHa ingresado un valor fuera del rango para el salario, intente otra vez")
    salB5 = int(input("\nIngrese nuevamente el salario para el quinto empleado: "))
print("Valor de salario aceptado para el quinto empleado")

car5 = input("\nIngrese el cargo del quinto empleado: ")

while car5 != "a" and car5 != "j" and car5 != "g":
    print("\nHa ingresado un valor incorrecto para el cargo, intente otra vez")
    car5 = input("\nIngrese nuevamente el cargo para el quinto empleado: ")
print("Valor de cargo aceptado para el quinto empleado")


# Procesamiento de datos

#Calculo de edad

ed1 = (2023 - año1)

print("\nLa edad de {} es: {}".format(no1,ed1))

ed2 = (2023 - año2)

print("\nLa edad de {} es: {}".format(no2,ed2))

ed3 = (2023 - año3)

print("\nLa edad de {} es: {}".format(no3,ed3))

ed4 = (2023 - año4)

print("\nLa edad de {} es: {}".format(no4,ed4))

ed5 = (2023 - año5)

print("\nLa edad de {} es: {}".format(no5,ed5))

print("--------------------------------------------------------------------------")

#Validacion de genero

if g1 == "f":
    print("\nEl empleado {} es mujer".format(no1))
elif g1 == "m":
    print("\nEl empleado {} es hombre".format(no1))
else:
    print("\nEl genero es invalido para la primera persona, favor intentar de nuevo")

if g2 == "f":
    print("\nEl empleado {} es mujer".format(no2))
elif g2 == "m":
    print("\nEl empleado {} es hombre".format(no2))
else:
    print("\nEl genero es invalido para la segunda persona, favor intentar de nuevo")

if g3 == "f":
    print("\nEl empleado {} es mujer".format(no3))
elif g3 == "m":
    print("\nEl empleado {} es hombre".format(no3))
else:
    print("\nEl genero es invalido para la tercera persona, favor intentar de nuevo")

if g4 == "f":
    print("\nEl empleado {} es mujer".format(no4))
elif g4 == "m":
    print("\nEl empleado {} es hombre".format(no4))
else:
    print("\nEl genero es invalido para la cuarta persona, favor intentar de nuevo")

if g5 == "f":
    print("\nEl empleado {} es mujer".format(no5))
elif g5 == "m":
    print("\nEl empleado {} es hombre".format(no5))
else:
    print("\nEl genero es invalido para la quinta persona, favor intentar de nuevo")

print("--------------------------------------------------------------------------")

#Validacion de cargo

if car1 == "a":
    print("\nEl cargo del primer empleado es Asistente")
elif car1 == "j":
    print("\nEl cargo del primer empleado es Jefe")
elif car1 == "g":
    print("\nEl cargo del primer empleado es Gerente")
else:
    print("\nEl cargo es invalido para la primera persona, favor intentar de nuevo")

if car2 == "a":
    print("\nEl cargo del segundo empleado es Asistente")
elif car2 == "j":
    print("\nEl cargo del segundo empleado es Jefe")
elif car2 == "g":
    print("\nEl cargo del segundo empleado es Gerente")
else:
    print("\nEl cargo es invalido para la segunda persona, favor intentar de nuevo")

if car3 == "a":
    print("\nEl cargo del tercer empleado es Asistente")
elif car3 == "j":
    print("\nEl cargo del tercer empleado es Jefe")
elif car3 == "g":
    print("\nEl cargo del tercer empleado es Gerente")
else:
    print("\nEl cargo es invalido para la tercera persona, favor intentar de nuevo")

if car4 == "a":
    print("\nEl cargo del cuarto empleado es Asistente")
elif car4 == "j":
    print("\nEl cargo del cuarto empleado es Jefe")
elif car4 == "g":
    print("\nEl cargo del cuarto empleado es Gerente")
else:
    print("\nEl cargo es invalido para la cuarta persona, favor intentar de nuevo")

if car5 == "a":
    print("\nEl cargo del quinto empleado es Asistente")
elif car5 == "j":
    print("\nEl cargo del quinto empleado es Jefe")
elif car5 == "g":
    print("\nEl cargo del quinto empleado es Gerente")
else:
    print("\nEl cargo es invalido para la quinta persona, favor intentar de nuevo")

print("--------------------------------------------------------------------------")

#Calculo de descuento de renta por rango salarial, por empleado

#Empleado numero 1
if salB1 >364:
    if salB1 > 364 and salB1 < 472.01:
        emp1DesRenta = RENTA0
    elif salB1 >= 472.01 and salB1 < 895.25:
        emp1DesRenta = salB1 * RENTA1
    elif salB1 >= 895.25 and salB1 < 2038.11:
        emp1DesRenta = salB1 * RENTA2
    elif salB1 >= 2038.11 and salB1 < 9999:
        emp1DesRenta = salB1 * RENTA3

    des1Isss = salB1 * ISSS
    des1Afp = salB1 * AFP

    emp1DesT = des1Isss + des1Afp + emp1DesRenta
    salN1 = salB1 - emp1DesT 

    print("\nDescuentos y bonos Primer empleado:")
    print("\nEl descuento de ISSS es: {}, \nEl descuento de AFP es: {} \nEl descuento de renta es: {}".format (des1Isss,des1Afp,emp1DesRenta))
    print("\n El descuento total es: {} \nEl salario neto es: {}".format(emp1DesT,salN1))

else:
    print("\nEl salario del primer empleado es demasiado bajo")

print("--------------------------------------------------------------------------")

#Empleado numero 2
if salB2 >364:
    if salB2 > 364 and salB2 < 472.01:
        emp2DesRenta = RENTA0
    elif salB2 >= 472.01 and salB2 < 895.25:
        emp2DesRenta = salB2 * RENTA1
    elif salB2 >= 895.25 and salB2 < 2038.11:
        emp2DesRenta = salB2 * RENTA2
    elif salB2 >= 2038.11 and salB2 < 9999:
        emp2DesRenta = salB2 * RENTA3

    des2Isss = salB2 * ISSS
    des2Afp = salB2 * AFP

    emp2DesT = des2Isss + des2Afp + emp2DesRenta
    salN2 = salB2 - emp2DesT 

    print("\nDescuentos y bonos Segundo empleado:")
    print("\nEl descuento de ISSS es: {}, \nEl descuento de AFP es: {} \nEl descuento de renta es: {}".format (des2Isss,des2Afp,emp2DesRenta))
    print("\n El descuento total es: {} \nEl salario neto es: {}".format(emp2DesT,salN2))

else:
    print("\nEl salario del Segundo empleado es demasiado bajo")

print("--------------------------------------------------------------------------")


#Empleado numero 3
if salB3 >364:
    if salB3 > 364 and salB3 < 472.01:
        emp3DesRenta = RENTA0
    elif salB3 >= 472.01 and salB3 < 895.25:
        emp3DesRenta = salB3 * RENTA1
    elif salB3 >= 895.25 and salB3 < 2038.11:
        emp3DesRenta = salB3 * RENTA2
    elif salB3 >= 2038.11 and salB3 < 9999:
        emp3DesRenta = salB3 * RENTA3

    des3Isss = salB3 * ISSS
    des3Afp = salB3 * AFP

    emp3DesT = des3Isss + des3Afp + emp3DesRenta
    salN3 = salB3 - emp3DesT 

    print("\nDescuentos y bonos Tercer empleado:")
    print("\nEl descuento de ISSS es: {}, \nEl descuento de AFP es: {} \nEl descuento de renta es: {}".format (des3Isss,des3Afp,emp3DesRenta))
    print("\n El descuento total es: {} \nEl salario neto es: {}".format(emp3DesT,salN3))

else:
    print("\nEl salario del Tercer empleado es demasiado bajo")

print("--------------------------------------------------------------------------")

#Empleado numero 4
if salB4 >364:
    if salB4 > 364 and salB4 < 472.01:
        emp4DesRenta = RENTA0
    elif salB4 >= 472.01 and salB4 < 895.25:
        emp4DesRenta = salB4 * RENTA1
    elif salB4 >= 895.25 and salB4 < 2038.11:
        emp4DesRenta = salB4 * RENTA2
    elif salB4 >= 2038.11 and salB4 < 9999:
        emp4DesRenta = salB4 * RENTA3

    des4Isss = salB4 * ISSS
    des4Afp = salB4 * AFP

    emp4DesT = des4Isss + des4Afp + emp4DesRenta
    salN4 = salB4 - emp4DesT 

    print("\nDescuentos y bonos Cuarto empleado:")
    print("\nEl descuento de ISSS es: {}, \nEl descuento de AFP es: {} \nEl descuento de renta es: {}".format (des4Isss,des4Afp,emp4DesRenta))
    print("\n El descuento total es: {} \nEl salario neto es: {}".format(emp4DesT,salN4))

else:
    print("\nEl salario del Cuarto empleado es demasiado bajo")

print("--------------------------------------------------------------------------")


#Empleado numero 5
if salB5 >364:
    if salB5 > 364 and salB5 < 472.01:
        emp5DesRenta = RENTA0
    elif salB5 >= 472.01 and salB5 < 895.25:
        emp5DesRenta = salB5 * RENTA1
    elif salB5 >= 895.25 and salB5 < 2038.11:
        emp5DesRenta = salB5 * RENTA2
    elif salB5 >= 2038.11 and salB5 < 9999:
        emp5DesRenta = salB5 * RENTA3

    des5Isss = salB5 * ISSS
    des5Afp = salB5 * AFP

    emp5DesT = des5Isss + des5Afp + emp5DesRenta
    salN5 = salB5 - emp5DesT 

    print("\nDescuentos y bonos Quinto empleado:")
    print("\nEl descuento de ISSS es: {}, \nEl descuento de AFP es: {} \nEl descuento de renta es: {}".format (des5Isss,des5Afp,emp5DesRenta))
    print("\n El descuento total es: {} \nEl salario neto es: {}".format(emp5DesT,salN5))

else:
    print("\nEl salario del Quinto empleado es demasiado bajo")

print("--------------------------------------------------------------------------")

#Edad media total

edadT = (ed1 + ed2 + ed3 +ed4 + ed5) / 5

print("\nLa edad media de los 5 empleados es : {}".format(edadT))

# Salario neto total a pagar por parte de la empresa

salNt = salN1 + salN2 +salN3 + salN4 + salN5

print("\nLa cantidad a total a pagar por parte de la empresa en concepto de salarios es: {} ".format(salNt))



