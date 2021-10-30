import os

# Variable por cada tipo de billete
b5, b10, b20, b50 = 0, 0, 0, 0
b100, b200, b500 = 0, 0, 0

total = 0

# menuPlatos = list()
# preciosPlatos = list()

platos = dict()
platosConsumidos = list()

def anadirPlatos(nombre, precio, dicc):
    if not nombre in dicc:
        dicc[nombre] = precio
    else:
        print(f'El plato ya existe')

def seguirBucle(mensaje):
    continuar = None
    while continuar == None:
        respuesta = input(f'¿{mensaje}? Si(1) / No (0): ')
        respuesta = respuesta.lower()
        if respuesta in ['s', 'si', '1']:
            continuar = True
        elif respuesta in ['n', 'no', '0']:
            continuar = False
        else:
            print('No he entendido su respuesta')
    return continuar

def mostrarMenu(dicc):
    print(f'{"* * * * * * * * * * MENU DEL DÍA - RESTAURANTE DEL TIO MANOLO * * * * * * * * * *":^60}')
    for key in dicc:
        print(f'{key:<64} : {dicc[key]:>7.2f}€')

def crearMenu(dicc):
    continuar = True
    while continuar:
        nombre = input('Nombre del plato: ')
        precio = int(input('Precio del plato: '))
        anadirPlatos(nombre, precio, dicc)
        continuar = seguirBucle('Introducir un plato más al menú')

def pedirMenu(dicc):
    continuar = True
    platosPedidos = list()
    while continuar:
        mostrarMenu(dicc)
        print()
        nombre = input('¿Qué desea tomar?: ')
        platosPedidos.append(nombre)
        continuar = seguirBucle('Algo más')
    return platosPedidos

def borrarPantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    global platos
    global platosConsumidos

    crearMenu(platos)
    borrarPantalla()
    platosConsumidos = pedirMenu(platos)
    borrarPantalla()
    print('Ústed ha pedido los siguientes platos:')
    for pc in platosConsumidos:
        print(pc)

if __name__ == '__main__':
    main()