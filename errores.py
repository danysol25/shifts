def abrir_archivo(nombre_archivo):
    try:
        archivo = open(nombre_archivo)
    except FileNotFoundError:
        print("El archivo no fue encontrado")
    except: 
        print("Error desconocido")
    else:
        print("Abriendo exitosamente")
    finally:
        print("Finalizando ejecución")

#ERRORES EN LOOP:
def pedir_numero():
    while True:
        try:
            numero= int(input('dame un número:'))
        except:
            print('Ese no es un número')
        else: 
            print(f'Ingresaste el número {numero}.')
            break #para salir del loop
    print('Gracias')