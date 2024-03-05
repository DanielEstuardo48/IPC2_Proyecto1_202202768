class Patron:
    def __init__(self, nombre, R, C, F, S, codigo, patron):
        self.nombre = nombre
        self.R = R
        self.C = C
        self.F = F
        self.S = S
        self.codigo = codigo
        self.patron = patron
        self.cambio = 0

    #def editar_nombre(self):
    #    self.nombre = input("Ingrese el nuevo nombre: ")

    #def editar_R(self):
    #    self.R = int(input("Ingrese el nuevo valor de R: "))

    #def editar_C(self):
    #    self.C = int(input("Ingrese el nuevo valor de C: "))

    #def editar_F(self):
    #    self.F = int(input("Ingrese el nuevo valor de F: "))

    #def editar_S(self):
    #    self.S = int(input("Ingrese el nuevo valor de S: "))

    #def editar_codigo(self):
    #    self.codigo = input("Ingrese el nuevo código de nuevo: ")

    def editar_patron(self, new_patron):
        self.patron = new_patron
    
    def comparar_patron(self, new_patron):
        if self.patron != new_patron:
            self.cambio += 1 
    
    def editar_patron(self, new_patron):
        if new_patron != self.patron:
            x = 0
            for old, new in zip(self.patron, new_patron):
                if old != new:
                    x += 1
            self.cambio = x
        self.patron = new_patron
        #self.patron = new_patron
        #self.comparar_patron(new_patron)
        #self.patron = new_patron

    def __str__(self):
        return f"{self.nombre} - {self.R} - {self.C} - {self.F} - {self.S} - {self.codigo} - {self.patron}"

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar(self, dato):
        if not self.cabeza:
            self.cabeza = Nodo(dato)
        else:
            nodo_actual = self.cabeza
            while nodo_actual.siguiente:
                nodo_actual = nodo_actual.siguiente
            nodo_actual.siguiente = Nodo(dato)

    def mostrar(self):
        nodo_actual = self.cabeza
        while nodo_actual:
            print("\nNombre: ",nodo_actual.dato.nombre)
            print("R: ",nodo_actual.dato.R)
            print("C: ",nodo_actual.dato.C)
            print("F: ",nodo_actual.dato.F)
            print("S: ",nodo_actual.dato.S)
            print("Codigo: ",nodo_actual.dato.codigo)
            print("Patron: ",nodo_actual.dato.patron)
            nodo_actual = nodo_actual.siguiente
    
    def buscar(self, codigo):
        actual = self.cabeza
        while actual:
            if actual.dato.codigo == codigo:
                return actual
            actual = actual.siguiente
        return None

    def seleccionar_editar(self,codigo):
        seleccion_patron = self.buscar(codigo)
        if seleccion_patron:
            print("\nPatrón seleccionado:")
            print("Nombre: ",seleccion_patron.dato.nombre)
            print("R: ",seleccion_patron.dato.R)
            print("C: ",seleccion_patron.dato.C)
            print("F: ",seleccion_patron.dato.F)
            print("S: ",seleccion_patron.dato.S)
            print("Codigo: ",seleccion_patron.dato.codigo)
            print("Patron: ",seleccion_patron.dato.patron)

            new_patron = input("Ingrese el nuevo patrón: ")
            if len(new_patron) != int(seleccion_patron.dato.R) * int(seleccion_patron.dato.C):
                    print("\n Error: No se puede editar el patrón, ya que el número de elementos ingresados es diferente al resultado de la multiplicación de R por C.")
            else:
                    seleccion_patron.dato.editar_patron(new_patron)

                    print("\nPatrón actualizado:")
                    print("Patron: ", seleccion_patron.dato.patron)
                    print("Cambios: ", seleccion_patron.dato.cambio * seleccion_patron.dato.S)
        else:
            print("Patron no encontrado")

class Patrones:
    def agregar_patron(self):
        patron_nuevo = Patron('Ejemplo1', 3, 3, 7, 8, 'S2204', 'BNBNBNBNB')
        patron_nuevo2 = Patron('Ejemplo2', 2, 2, 7, 8, 'S2205', 'BBNN')
        lista_enlazada.agregar(patron_nuevo)
        lista_enlazada.agregar(patron_nuevo2)

    def mostrar_patrones(self):
        lista_enlazada.mostrar()
    
    def seleccionar_patrones(self):
        codigo = input("\nIngrese el codigo a editar: ")
        lista_enlazada.seleccionar_editar(codigo)


def menu():
    print("\n ================= Menu Inicial =====================")
    print("1. Agregar archivo XML con patrones")
    print("2. Mostrar patrones")
    print("3. Editar patron")
    print("4. Salir")
    opcion = int(input("Seleccione una opción: "))
    return opcion

def main():
    patrones = Patrones()
    while True:
        opcion = menu()
        if opcion == 1:
            patrones.agregar_patron()
        elif opcion == 2:
            patrones.mostrar_patrones()
        elif opcion == 3:
            patrones.seleccionar_patrones()
        elif opcion == 4:
            print("Saliendo...")
            break
        else:
            print("Opción no válida")

lista_enlazada = ListaEnlazada()
main()

# #!ESto iba en agregar
'''nombre = input("Ingrese el nombre del patron: ")
        R = int(input("Ingrese el valor de R: "))
        C = int(input("Ingrese el valor de C: "))
        F = int(input("Ingrese el valor de F: "))
        S = int(input("Ingrese el valor de S: "))
        codigo = input("Ingrese el codigo del patron: ")
        patron = input("Ingrese el patron: ")'''

# #!Esto estaba en editar patrones
'''#lista = ListaEnlazada()
        codigo = input("\nIngrese el codigo a editar: ")
        seleccion_patron = lista_enlazada.seleccionar(codigo)
        if seleccion_patron:
            print(f"Patron seleccionado: {seleccion_patron}")
        else:
            print("Patron no encontrado")'''