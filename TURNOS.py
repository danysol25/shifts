import numeros_de_turnos

def preguntar():
    print('Bienvenido.')

    while True:
        print("Seleccione 'C' para turno en Costmética")
        print("Seleccione 'F' para turno en Farmacia")
        print("Seleccione 'P' para turno en Perfumeria")

        try:
            #genero MI variable, que después usaré de parámetro en la función creada en numeros_de_turnos
            mi_opcion = input('Elija su rubro: \n').upper()
            ['P','F','C'].index(mi_opcion)
        except: 
            print('La opción seleccionada no es válida. Intentelo nuevamente.')
        else:
            break

    #llamamos al decorador
    numeros_de_turnos.decorar_saludo(mi_opcion)

#función para darle inicio al programa

def inicio():
    while True:
        preguntar()
        try:
            sacar_otro_turno= input('Desea un nuevo turno? Y/N : ').upper()
            ['Y', 'N'].index(sacar_otro_turno)
        except ValueError:
            print('La opción seleccionada no es válida. Intentelo nuevamente.')
        else:
            if sacar_otro_turno == 'N':
                print('Gracias por su consulta.')
                break

inicio()