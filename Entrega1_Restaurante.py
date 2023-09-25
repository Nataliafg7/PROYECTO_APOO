class Usuario:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class Mesero:
    def __init__(self, username):
        self.username = username

class Mesa:
    def __init__(self, numero):
        self.numero = numero
        self.mesero = None
        self.pedido = []
        self.reservada = False
        self.reserva = None

    def asignar_mesero(self, mesero):
        self.mesero = mesero

    def agregar_pedido(self, platos):
        self.pedido.extend(platos )

    def consultar_cuenta(self):
        total = sum(item.precio for item in self.pedido)
        return total

    def hacer_reserva(self, hora, dia, nombre_reserva):
        self.reserva = {
            'hora': hora,
            'dia': dia,
            'nombre_reserva': nombre_reserva
        }
        self.reservada = True

class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

# Base de datos simulada de usuarios
usuarios = []

# Base de datos simulada de meseros
meseros = []

# Base de datos simulada de mesas
mesas = [Mesa(numero) for numero in range(1, 20)]

# Base de datos simulada de platos
platos = [
    Producto("Pizza", 10),
    Producto("Pasta", 12),
    Producto("Ensalada", 6),
    Producto("Hamburguesa", 8),
    Producto("Sopa", 5),
    Producto("Pollo a la Parrilla", 15),
    Producto("Pescado", 14),
    Producto("Sushi", 18),
    Producto("Tacos", 9),
    Producto("Helado", 4),
    Producto("Agua", 2),
    Producto("Refresco", 3),
    Producto("Jugo", 4),
    Producto("Cerveza", 5),
    Producto("Vino", 10),
    Producto("Café", 2),
    Producto("Té", 2),
    Producto("Licor", 8),
    Producto("Coctel", 7),
    Producto("Limonada", 3)
]



# Función para crear usuario
def crear_usuario():
    username = input("Ingrese un nombre de usuario: ")
    password = input("Ingrese una contraseña: ")
    usuarios.append(Usuario(username, password))
    print("Usuario creado con éxito.")

# Función para iniciar sesión
def iniciar_sesion():
    username = input("Ingrese su nombre de usuario: ")
    password = input("Ingrese una contraseña: ")

    for usuario in usuarios:
        if usuario.username == username and usuario.password == password:
            mesero = Mesero(username)
            meseros.append(mesero)
            return mesero

    print("Nombre de usuario o contraseña incorrectos.")
    return None

# Función para mostrar el menú de platos 
def mostrar_menu():
    print("\nMenú de Platos:")
    for i, plato in enumerate(platos, 1):
        print(f"{i}. {plato.nombre} - ${plato.precio}")

   

# Función para realizar un pedido
def realizar_pedido(mesa):
    platos_seleccionados = []


    while True:
        mostrar_menu()
        opcion = input("Seleccione un plato o bebida (número) o '0' para finalizar el pedido: ")

        if opcion == "0":
            break
        elif opcion.isdigit() and 1 <= int(opcion) <= len(platos):
            plato_elegido = platos[int(opcion) - 1]
            platos_seleccionados.append(plato_elegido)
            print(f"Plato {plato_elegido.nombre} agregado al pedido.")
     

        else:
            print("Opción no válida. Intente nuevamente.")

    mesa.agregar_pedido(platos_seleccionados)

# Función para gestionar reservas de mesas
def gestionar_reserva():
    hora = input("Ingrese la hora de la reserva (hh:mm): ")
    dia = input("Ingrese el día de la reserva (dd/mm/aaaa): ")
    nombre_reserva = input("Ingrese el nombre del cliente que reserva: ")

    mesas_disponibles = [mesa for mesa in mesas if not mesa.reservada]
    if len(mesas_disponibles) == 0:
        print("No hay mesas disponibles en el horario solicitado.")
    else:
        print("\nMesas disponibles:")
        for mesa in mesas_disponibles:
            print(f"Mesa {mesa.numero}")
        
        numero_mesa = int(input("Seleccione el número de la mesa para la reserva: "))
        mesa = mesas[numero_mesa - 1]
        mesa.hacer_reserva(hora, dia, nombre_reserva)
        print(f"Mesa {mesa.numero} reservada para el {dia} a las {hora} por {nombre_reserva}.")

# Función para mostrar información de reserva de mesa
def mostrar_info_reserva():
    numero_mesa = int(input("Ingrese el número de mesa para ver la información de reserva: "))
    mesa = mesas[numero_mesa - 1]
    if mesa.reservada:
        print(f"Información de Reserva de Mesa {mesa.numero}:")
        print(f"Día: {mesa.reserva['dia']}")
        print(f"Hora: {mesa.reserva['hora']}")
        print(f"Nombre de Reserva: {mesa.reserva['nombre_reserva']}")
    else:
        print(f"La Mesa {mesa.numero} no está reservada.")

# Función principal
def main():
    mesero = None

    while True:
        print("\nMenú Principal:")
        print("1. Crear Usuario")
        print("2. Iniciar Sesión")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            crear_usuario()
        
        elif opcion == "2":
            mesero = iniciar_sesion()
            if mesero:
                while True:
                    print(f"\nBienvenido, {mesero.username}")
                    print("Menú Mesero:")
                    print("1. Mesas")
                    print("2. Ventas")
                    print("3. Cerrar Sesión")
                    opcion_menu_mesero = input("Seleccione una opción: ")

                    if opcion_menu_mesero == "1":
                        while True:
                            print("\nMenú Mesas:")
                            print("1. Asignar Mesa")
                            print("2. Agregar Pedido a Mesa")
                            print("3. Consultar Cuenta de Mesa")
                            print("4. Hacer Reserva de Mesa")
                            print("5. Información de Reserva de Mesa")
                            print("6. Volver al Menú Mesero")
                            opcion_mesas = input("Seleccione una opción: ")

                            if opcion_mesas == "1":
                                numero_mesa = int(input("Ingrese el número de mesa: "))
                                mesas[numero_mesa - 1].asignar_mesero(mesero)
                                print(f"Mesa {numero_mesa} asignada a {mesero.username}")

                            elif opcion_mesas == "2":
                                numero_mesa = int(input("Ingrese el número de mesa: "))
                                realizar_pedido(mesas[numero_mesa - 1])

                            elif opcion_mesas == "3":
                                numero_mesa = int(input("Ingrese el número de mesa: "))
                                cuenta = mesas[numero_mesa - 1].consultar_cuenta()
                                print(f"La cuenta de la mesa {numero_mesa} es: ${cuenta}")

                            elif opcion_mesas == "4":
                                gestionar_reserva()

                            elif opcion_mesas == "5":
                                mostrar_info_reserva()

                            elif opcion_mesas == "6":
                                break

                            else:
                                print("Opción no válida. Intente nuevamente.")

                    elif opcion_menu_mesero == "2":
                        while True:
                            print("\nMenú Ventas:")
                            print("1. Informe de la Mesa más consumida")
                            print("2. Informe del Mesero que más vendió")
                            print("3. Volver al Menú Mesero")
                            opcion_ventas = input("Seleccione una opción: ")

                            if opcion_ventas == "1":
                                mesa_mas_consumida = max(mesas, key=lambda mesa: mesa.consultar_cuenta())
                                print(f"La mesa más consumida es la mesa {mesa_mas_consumida.numero}")

                            elif opcion_ventas == "2":
                                ventas_meseros = {}
                                for mesa in mesas:
                                    if mesa.mesero is not None:
                                        if mesa.mesero.username not in ventas_meseros:
                                            ventas_meseros[mesa.mesero.username] = 0
                                        ventas_meseros[mesa.mesero.username] += mesa.consultar_cuenta()

                                if ventas_meseros:
                                    mesero_mas_vendio = max(ventas_meseros, key=ventas_meseros.get)
                                    print(f"El mesero que más vendió es {mesero_mas_vendio}")
                                else:
                                    print("No hay ventas registradas.")

                            elif opcion_ventas == "3":
                                break

                            else:
                                print("Opción no válida. Intente nuevamente.")

                    elif opcion_menu_mesero == "3":
                        meseros.remove(mesero)
                        print("Sesión cerrada.")
                        break

                    else:
                        print("Opción no válida. Intente nuevamente.")

        elif opcion == "3":
            print("Hasta luego.")
            return

        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()
