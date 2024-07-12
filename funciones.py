from csv import writer,reader
from json import dump,load
from Lib import *


trabajadores = ["Juan Pérez","María García","Carlos López","Ana Martínez","Pedro Rodríguez","Laura Hernández","Miguel Sánchez","Isabel Gómez","Francisco Díaz","Elena Fernández"]






def opcion_inicial():
    while True:
        try:
            opcion_1 = int(input("1) Asignar sueldos aleatorios\n2) Clasificar sueldos\n3) Ver estadísticas\n4) Reporte de sueldos\n5) Salir del programa\n:"))
            if opcion_1 > 0 and opcion_1 < 6:

                if opcion_1 == 1:
                    print(asignar_sueldos())
                    
            

                if opcion_1 == 2:
                    clasificar_sueldos()

                if opcion_1 == 3:
                    ver_estadísticas()

                if opcion_1 == 4:
                    reporte_de_sueldos()

                if opcion_1 == 5:
                    print("Finalizando programa…\nDesarrollado por Nicolas Sanchez\nRUT 20.183.798-7")
                    break
            elif opcion_1 < 1 or opcion_1 > 5:
                print("Tiene que ser un número del 1 al 5")
        except:
            print("Tiene que ser un número del 1 al 5, no letras")




#1#

def asignar_sueldos():
    #Lista nueva#
    trabajadores_sueldo = []
    #Aplicando sueldo no tan aleatorio#
    sueldo = int(300000)
    #contador#
    contador = int(0)
                
    for i in trabajadores:
        trabajadores_sueldo.append([i,sueldo])
        sueldo = sueldo + 200000
        contador = contador + 1
        if contador == 3:
            sueldo = sueldo + 700000
            contador = int(0)

    return(trabajadores_sueldo)






#2#

def clasificar_sueldos():
    lista_pequena = []
    lista_mediana = []
    lista_grande = []

    
    for o in asignar_sueldos():
        if o[1] < 800000:
            lista_pequena.append(o)
        elif o[1] >= 800000 and o[1] <= 2000000:
            lista_mediana.append(o)
        elif o[1] > 2000000:
            lista_grande.append(o)

    print(f"Sueldos menores a $800.000  Total: {len(lista_pequena)}")
    print()
    print("Nombre empleado  Sueldo")
    print()
    contador = int(0)
    for q in lista_pequena:
        for w in q:
            print(w, end=" ")
            contador = contador +1

            if contador == 1:
                print("$", end="")

            if contador == 2:
                print()
                contador = int(0)




    
    print()
    print(f"Sueldos entre $800.000 y $2.000.000  Total: {len(lista_mediana)}")
    print()
    print("Nombre empleado  Sueldo")
    print()
    contador = int(0)
    for q in lista_mediana:
        for w in q:
            print(w, end=" ")
            contador = contador +1

            if contador == 1:
                print("$", end="")

            if contador == 2:
                print()
                contador = int(0)
                
    print()
    print(f"Sueldos superiores a $2.000.000  Total: {len(lista_grande)}")
    print()
    print("Nombre empleado  Sueldo")
    print()
    contador = int(0)
    for q in lista_grande:
        for w in q:
            print(w, end=" ")
            contador = contador +1

            if contador == 1:
                print("$", end="")

            if contador == 2:
                print()
                contador = int(0)





#3#
def ver_estadísticas():
    try:
        opcion_2 = int(input("1) Sueldo mas alto\n2) Sueldo más bajo\n3) Promedio de sueldos\n4) Generar archivo (CSV)\n:"))
        if opcion_2 > 0 and opcion_2 < 5:
        
            if opcion_2 == 1:
                sueldo_completo_mayor = []
                sueldos = []
                for z in asignar_sueldos():
                    sueldos.append(z[1])

                sueldo_mayor = max(sueldos)

                    
                for z in asignar_sueldos():
                    if z[1] == sueldo_mayor:
                        sueldo_completo_mayor.append(z)

                contador = int(0)
                for x in sueldo_completo_mayor:
                    for c in x:
                        print(c,end=" ")
                        contador = contador + 1
                        if contador == 1:
                            print("$",end="")
                    print()
                



            if opcion_2 == 2:
                sueldo_completo_menor = []
                sueldos = []
                for z in asignar_sueldos():
                    sueldos.append(z[1])

                sueldo_menor = min(sueldos)

                    
                for z in asignar_sueldos():
                    if z[1] == sueldo_menor:
                        sueldo_completo_menor.append(z)

                contador = int(0)
                for x in sueldo_completo_menor:
                    for c in x:
                        print(c,end=" ")
                        contador = contador + 1
                        if contador == 1:
                            print("$",end="")
                    print()


            if opcion_2 == 3:
                sueldos = int(0)
                for z in asignar_sueldos():
                    sueldos = sueldos + z[1]

                promedio_sueldos = sueldos // 10

                print("El promedio de sueldos es: ")
                print(f"${promedio_sueldos}")


            if opcion_2 == 4:
                lista_espaciadora = []
                #Crear CSV#
                try:
                    open("archivo.csv","x")
                except:
                    print("archivo.csv sobrescrito")

                #Escribir CSV#
                escribir_base_csv = open("archivo.csv","w",newline="")
                escribir_avanzado_csv = writer(escribir_base_csv)
                #asignar sueldos, 1#
                escribir_avanzado_csv.writerow(["Sueldos asignados"])
                escribir_avanzado_csv.writerows(asignar_sueldos())
                escribir_base_csv.close()
        elif opcion_2 < 1 or opcion_2 > 4:
            print("Tiene que ser un número del 1 al 4")
    except:
        print("Tiene que ser un número del 1 al 4, no letras")







#4#
def reporte_de_sueldos():
    print("Nombre empleado   Sueldo Base  Descuento Salud  Descuento AFP  Sueldo liquido")
    print()
    for n in asignar_sueldos():
        descuento_salud = round((n[1]* 0.07))
        descuento_afp = round((n[1]* 0.12))
        liquido = round(n[1] - descuento_salud - descuento_afp)
        
        print(n[0], end="          $")

        print(n[1], end="        $")
        
        print(descuento_salud, end="         $")
        
        print(descuento_afp, end="        $")

        print(liquido)
        
            
            
        
