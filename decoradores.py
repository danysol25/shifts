def decorar_saludo(funcion):
    def otra_funcion(palabra):
        print('Hola')
        funcion(palabra)
        print('Chau')
    return otra_funcion

def mayusculas(texto):
    print(texto.upper())

mayusculas_decorada = decorar_saludo(mayusculas)

mayusculas_decorada('roberTHIno')