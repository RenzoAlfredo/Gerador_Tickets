def generador_n():
    x = 1
    while x > 0:
        yield x
        x += 1

def decorador_saludo_n(funcion):
    def otra_funcion(a,b):
        print('\n' + '*' * 23 )
        print('Su turno es')
        funcion(a,b)
        print('Aguarde y\nserà atendido')
        print('*' * 23 + '\n')
    return otra_funcion
