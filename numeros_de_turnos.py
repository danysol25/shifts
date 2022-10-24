#defino una función por cada opción disponible
def turno_farmacia():
    for n in range(1,9999):
        yield f'F-{n}'

def turno_perfumeria():
    for n in range(1,9999):
        yield f'P-{n}'

def turno_cosmetica():
    for n in range(1,9999):
        yield f'C-{n}'

#asigno una variable a cada función
f = turno_farmacia()
c = turno_cosmetica()
p = turno_perfumeria()

#decoracor
def decorar_saludo(opcion):
    
    print('\nSu turno es: \n')

    if opcion == 'F':
        print(next(f))

    elif opcion == 'C':
        print(next(c))

    elif opcion == 'P':
        print(next(p))

    else:
        print('La opción seleccionada es incorrecta.')

    print('\nAguarde y será atendido.')

