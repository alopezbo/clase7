#Ejercicio 5

# Ingrese objeto:

# Seleccione: multiplicar
#             resta
#             sumar


# objeto
# resultado
# caracteristicas:
#     xxxxxx
#     xxxxxx
#     xxxxxx


# Ingrese valor:
# Quiere ingresar otro: si o no
# Ingrese valor:
# Quiere ingresar otro: si o no

import funcion
import objeto
objeto=input('Ingrese nombre del objeto:')
while True: 
    select=input('Seleccione /n Resta /n Multiplicacion /n Suma /n Division n/ Ingrese su seleccion: ')
    if select=="Resta": 
        valor=int(input("Ingrese primer valor: "))
        valor2=int(input("Ingrese segundo valor: ")) 
        print(funcion.resta(valor,valor2))

    elif select=="Multiplicacion": 
        valor=int(input("Ingrese primer valor: "))
        valor2=int(input("Ingrese segundo valor: "))
        print(funcion.multiplicar(valor,valor2))

    elif select=="Suma": 
        valor=int(input("Ingrese primer valor: "))
        valor2=int(input("Ingrese segundo valor: "))
        print(funcion.suma(valor,valor2))

    elif select=="Division": 
        valor=int(input("Ingrese primer valor: "))
        valor2=int(input("Ingrese segundo valor: "))
        print(funcion.dividir(valor,valor2))
    break 



