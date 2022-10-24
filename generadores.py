def generadora():
    yield(range(1,6))

def mi_funcion():
    lista = []
    for x in range(1,5):
        lista.append(x*10)
    return lista

def mi_funcion_generadora():
    for x in range(1,5):
        yield x*10 #no va a reproducir todos los resultados, SINO que a medida q se lo vaya pidiendo, los irá recordando.

print(mi_funcion())
print(mi_funcion_generadora())

g= mi_funcion_generadora()

print(next(g))
print(next(g))

def otra_generadora():
    x=1
    yield x

    x += 1
    yield x

    x += 10
    yield x

    x += 2
    yield x

    x += 1
    yield x

gen = otra_generadora()

print(next(gen))
print(next(gen))
print('Texto para interrumpir')
print(next(gen))
print(next(gen))
print(next(gen))
print('Chau mundo')
print(next(gen))

