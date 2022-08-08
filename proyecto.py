## Proyecto para generar tickets secuenciales segùn al area que se dirija un cliente en una farmacia
import proyecto_numeros

genera_nticket_p = proyecto_numeros.generador_n()
genera_nticket_f = proyecto_numeros.generador_n()
genera_nticket_c = proyecto_numeros.generador_n()

@proyecto_numeros.decorador_saludo_n
def imprimir(area,tipo_gen):
    print(f'{area}-{next(tipo_gen)}')

def crear_ticket():
    opcion = ''
    while opcion != 'S':
        print('Seleccione a donde se dirige')
        print('OPCION NOMBRE')
        try:
            opcion = input('1   Perfumeria\n2   Farmacia\n3   Cosmetica\nS   Salir\n').upper()
            ['1','2','3','S'].index(opcion)
            if opcion == '1':
                imprimir('P',genera_nticket_p)
            elif opcion == '2':
                imprimir('F',genera_nticket_f)
            elif opcion == '3':
                imprimir('C',genera_nticket_c)
        except ValueError:
            print('Ha ingresado una opcion incorrecta')
        except:
            print('Error desconocido')
        else:
            break

def inicio():
    crear_ticket()
    while True:
        try:
            otro_turno = input('¿Desea sacar otro turno? [S] [N]').upper()
            ['S','N'].index(otro_turno)
            if otro_turno == 'S':
                crear_ticket()
            elif otro_turno == 'N':
                print('Gracias, hasta pronto')
                break
        except:
            print('No entiendo')

inicio()
