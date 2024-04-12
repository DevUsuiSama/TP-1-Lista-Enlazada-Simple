#
# Trabajo Práctico Nº 1
#
# Alumnos: José Fernando Usui, Luciana Rojas.
#

import os

# Tarea: Limpiar consola
clear = lambda: os.system('cls')

class Alumno:
    def __init__(self, nombre, apellido, DNI):
        self.nombre = nombre
        self.apellido = apellido
        self.DNI = DNI

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class LinkedList:
    def __init__(self):
        self.cabecera = None
    # Tarea: Introducir en la lista los nuevos nodos.
    def insertar(self, nodo):
        if self.cabecera:
            ultimo_nodo = self.cabecera
            while ultimo_nodo.siguiente != None:
                ultimo_nodo = ultimo_nodo.siguiente
            ultimo_nodo.siguiente = nodo
        else:
            self.cabecera = nodo
    # Tarea: Eliminar un nodo de la lista según el DNI del alumno introducido.
    def eliminar_por_DNI(self, DNI):
        if self.cabecera:
            anterior = None
            actual = self.cabecera
            while actual:
                if actual.dato.DNI == DNI:
                    if anterior:
                        anterior.siguiente = actual.siguiente
                        actual = None
                        print(f'El alumno con el DNI {DNI} fue eliminado con rotundo exito')
                        return
                    else:
                        self.cabecera = actual.siguiente
                        actual = None
                        print(f'El alumno con el DNI {DNI} fue eliminado con rotundo exito')
                        return
                anterior = actual
                actual = actual.siguiente
            print(f'El DNI {DNI} ingresado no se encontro')
    # Tarea: Recorrer e imprimir la lista según el DNI ingresado.
    def buscar_por_DNI(self, DNI):
        if self.cabecera:
            actual = self.cabecera
            while actual:
                if actual.dato.DNI == DNI:
                    print(actual.dato.nombre, actual.dato.apellido, actual.dato.DNI)
                    return
                actual = actual.siguiente
            print(f'El DNI {DNI} ingresado no se encontro')
    # Tarea: Mostrar toda la lista.
    def recorrer_e_imprimir(self):
        aux = self.cabecera
        while aux:
            print(aux.dato.nombre, aux.dato.apellido, aux.dato.DNI)
            aux = aux.siguiente
    # Tarea: Contar los nodos que hay en la lista.
    def cantidad_de_nodos(self):
        cantidad = 0
        aux = self.cabecera
        while aux:
            cantidad += 1
            aux = aux.siguiente
        return cantidad

# Tarea: Verifica que la opción introducido por el usuario este dentro de las opciones enumeradas en el menú.
def controlar_opcion(opcion):
  lista_de_opcion = [1, 2, 3, 4, 5, 6]
  for x in lista_de_opcion:
    if opcion == x:
      return True
  return False

def introducir_un_DNI():
  DNI = int(input('Ingrese el DNI de un alumno: '))
  return DNI

lista_alumnos = LinkedList()

while True:
    print('Menu:')
    print('1> Agregar un alumno')
    print('2> Buscar un alumno por su DNI')
    print('3> Eliminar un alumno por su DNI')
    print('4> Listar alumnos')
    print('5> Cantidad de nodos')
    print('6> Salir')
    print()
    opcion = int(input('Ingrese una opcion: '))
    print()
    if controlar_opcion(opcion):
        if opcion == 1:
            clear()
            print('Agregar alumno:')
            print()
            nombre = input('Ingresar el nombre del alumno: ')
            apellido = input('Ingresar el apellido del alumno: ')
            DNI = int(input('Ingresar el DNI del alumno: '))
            lista_alumnos.insertar(Nodo(Alumno(nombre, apellido, DNI)))
            clear()
        elif opcion == 2:
            clear()
            print('---------------------------------------------------------------')
            lista_alumnos.buscar_por_DNI(introducir_un_DNI())
            print('---------------------------------------------------------------')
            input('Presione cualquier tecla para continuar...')
            clear()
        elif opcion == 3:
            clear()
            print('---------------------------------------------------------------')
            lista_alumnos.eliminar_por_DNI(introducir_un_DNI())
            print('---------------------------------------------------------------')
            input('Presione cualquier tecla para continuar...')
            clear()
        elif opcion == 4:
            clear()
            print('---------------------------------------------------------------')
            print('Lista de alumnos:')
            print()
            lista_alumnos.recorrer_e_imprimir()
            print('---------------------------------------------------------------')
            input('Presione cualquier tecla para continuar...')
            clear()
        elif opcion == 5:
            clear()
            print('---------------------------------------------------------------')
            print()
            print(f'La cantidad de nodos es: {lista_alumnos.cantidad_de_nodos()}')
            print()
            print('---------------------------------------------------------------')
            input('Presione cualquier tecla para continuar...')
            clear()
        elif opcion == 6:
            break
    else:
        print('La opcion ingresada no existe')
        input('Presione cualquier tecla para continuar...')