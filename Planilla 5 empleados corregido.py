"""4.	Capturar nombre, año de nacimiento, cargo y salario de 5 empleados:
a)	Calcular el respectivo descuento de renta, AFP e ISSS por cada empleado 
b)	Mostrar nombre, edad, cargo, descuentos realizados y salario neto
c)	Realizar el ejercicio para una cantidad de empleados desconocida
d)	Mostrar la edad media
e)	Mostrar la cantidad de dinero que la empresa deberá destinar al pago de los empleados y detallar cantidad 
para prestaciones y neto"""

print("Calculo de planilla")

print("\nGénero de los empleados: \nMujeres: f \nHombres: m")
print("\nCargo de los empleados: \nAsistente: a \nJefe: j \nGerente: g")

# Definicion de variables

no = 0 #no es nombre
ed = 0 #ed es edad
año = 0
g= 0 #g es genero
salB = 0 #salB es salario bruto
car = 0 #car es cargo de empleado
empDesT = 0 #dest es Descuento total del primer empleado
salN = 0 #salN es Salario Neto

gT = "" #gT es Genero temporal
carT = "" #carT es Cargo temporal
#------------------------------------------#
i = 0 #Iterador
acuEd = 0 # Acumulador de edades
acuSal = 0 # Acumulador de salarios
# Constantes

AÑOA = 2023

#Las siguientes variables son para los descuentos de ISSS, AFP
# En el caso de RENTA será una constante dada la mulitplicacion

ISSS = 0.03
des1Isss = 0 #Muestra solo cantidad de descuento del ISSS


AFP = 0.0725
des1Afp = 0 #Muestra solo cantidad de descuento del AFP



RENTA0= 0
RENTA1 = 0.10 # El 10% se mantiene dentro de un rango $472.01 - $895.24
RENTA2 = 0.20 # El 20% se mantiene dentro de un rango $895.25 - $2038.10
RENTA3 = 0.30 # El 30% se mantiene dentro de un rango $2038.11 - $99999

# ESTO ES PARA DECLARAR LAS CONSTANTES DEL DESCUENTO DE RENTA POR EMPLEADO
# CON BASE AL RANGO SALARIAL QUE TIENE

emp1DesRenta = 0

#Esto es para la edad media

edadM = 0 #Esto es la edad media de los empleados

#Esto es para la cantidad total a pagar por parte de la empresa

salNm = 0 #Esto es el salario total neto a pagar por parte de los empleados


while i < 5:
    #Lectura y validacion de datos
    no = input("\nEmpleado numero {} Favor ingresar el nombre: ".format(i + 1))

    año = int(input("Empleado numero {} Favor ingresar el año en que nacio : ".format(i + 1)))
    while año < 1900 or año > 2004:
        print("\nHa ingresado un valor fuera del rango para el año de nacimiento, intente otra vez")
        año = int(input("\nEmpleado numero {} Ingrese nuevamente el año de nacimiento: ".format(i + 1)))
    print("Valor de año de nacimiento nuevo aceptado ") 

    g = input("\nEmpleado numero {} Favor ingresar el genero : ".format(i + 1))
    while g != "f" and g !=  "m":
        print("\nHa ingresado un valor incorrecto para el genero, intente otra vez")
        g = input("\nEmpleado numero {} Favor ingresar nuevamente el genero : ".format(i + 1))
    print("Valor de genero nuevo aceptado ") 
    
    salB = float(input("\nEmpleado numero {} Favor ingresar el salario base : ".format(i + 1)))
    while salB < 365 or salB > 4999:
        print("\nHa ingresado un valor fuera del rango para el salario, intente otra vez")
        salB = int(input("\nEmpleado numero {} Favor ingresar nuevamente el salario base : ".format(i + 1)))
    print("Valor de salario nuevo aceptado ") 

    car = input("\nEmpleado numero {} Favor ingresar el cargo : ".format(i + 1))
    while car != "a" and car != "j" and car != "g":
        print("\nHa ingresado un valor incorrecto para el cargo, intente otra vez")
        car = input("\nEmpleado numero {}Favor ingresar nuevamente el cargo : ".format(i + 1))
    print("Valor de cargo nuevo aceptado ") 

    #Asignacion de valores

    #Calculo de edad
    
    ed = (AÑOA - año)
    # acuEd = acuEd + ed /// Esto es lo mismo que /// acuEd += ed
    acuEd += ed

    #Calculo de genero

    if g == "f":
        gT= "Hombre"
    elif g == "m":
        gT= "Mujer"
   
    #Validacion de cargo

    if car == "a":
        carT = "Asistente"
    elif car == "j":
        carT = "Jefe"
    elif car == "g":
        carT = "Gerente"
    
    #Procesamiento de datos

    if salB > 364 and salB < 472.01:
        emp1DesRenta = RENTA0
    elif salB >= 472.01 and salB < 895.25:
        emp1DesRenta = salB * RENTA1
    elif salB >= 895.25 and salB < 2038.11:
        emp1DesRenta = salB * RENTA2
    elif salB >= 2038.11 and salB < 9999:
        emp1DesRenta = salB * RENTA3

    des1Isss = salB * ISSS
    des1Afp = salB * AFP

    emp1DesT = des1Isss + des1Afp + emp1DesRenta
    salN1 = salB - emp1DesT 

    # acuSal = acuSal + salN1 /// es lo mismo que /// acuSal += salN1
    acuSal += salN1

    # Muestra de datos

    print("------------------------------------------------------------")

    print("Impresion de planilla del empleado numero {}".format(i+1))

    print("\nLa edad de {} es: {}".format(no,ed))

    print("\nEl genero de {} es: {}".format(no,gT))

    print("\nEl cargo de {} es: {}".format(no,carT))

    print("\nDescuentos del empleado {}:".format(no))
    print("\nEl descuento de ISSS es: {}, \nEl descuento de AFP es: {} \nEl descuento de renta es: {}".format (des1Isss,des1Afp,emp1DesRenta))
    print("\n El descuento total es: {} \nEl salario neto es: {}".format(emp1DesT,salN1))


    i += 1

#Edad media total

edadM = acuEd / 5

print("\nLa edad media de los 5 empleados es : {}".format(edadM))

# Salario neto total a pagar por parte de la empresa


print("\nLa cantidad a total a pagar por parte de la empresa en concepto de salarios es: {} ".format(acuSal))
