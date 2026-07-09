from cliente import Cliente
from paquete import Paquete
from repartidor import Repartidor
from ciudad import Ciudad
from persistencia import guardar, cargar


class Gestor:

    def __init__(self):

        self.clientes = {}
        self.paquetes = {}
        self.repartidores = {}

        self.ciudad = Ciudad()

        self.cargar_datos()

    # ==========================
    # CARGAR DATOS
    # ==========================

    def cargar_datos(self):

        # Clientes
        clientes = cargar("datos/clientes.csv")

        for c in clientes:

            cliente = Cliente(
                c["id"],
                c["nombre"],
                c["direccion"]
            )

            historial = c["historial_pedidos"]

            if historial != "":
                cliente.historial_pedidos = historial.split(",")

            self.clientes[cliente.id] = cliente

        # Paquetes
        paquetes = cargar("datos/paquetes.csv")

        for p in paquetes:

            paquete = Paquete(
                p["codigo"],
                p["peso"],
                p["destino"],
                p["cliente"],
                p["estado"]
            )

            self.paquetes[paquete.codigo] = paquete

        # Repartidores
        repartidores = cargar("datos/repartidores.csv")

        for r in repartidores:

            repartidor = Repartidor(
                r["nombre"],
                r["vehiculo"],
                r["zona_actual"]
            )

            asignados = r["paquetes_asignados"]

            if asignados != "":
                repartidor.paquetes_asignados = asignados.split(",")

            self.repartidores[repartidor.nombre] = repartidor

    # ==========================
    # GUARDAR DATOS
    # ==========================

    def guardar_datos(self):

        guardar(
            "datos/clientes.csv",

            [
                {
                    "id": c.id,
                    "nombre": c.nombre,
                    "direccion": c.direccion,
                    "historial_pedidos": ",".join(c.historial_pedidos)
                }

                for c in self.clientes.values()
            ],

            [
                "id",
                "nombre",
                "direccion",
                "historial_pedidos"
            ]
        )

        guardar(
            "datos/paquetes.csv",

            [
                {
                    "codigo": p.codigo,
                    "peso": p.peso,
                    "destino": p.destino,
                    "estado": p.estado,
                    "cliente": p.cliente
                }

                for p in self.paquetes.values()
            ],

            [
                "codigo",
                "peso",
                "destino",
                "estado",
                "cliente"
            ]
        )

        guardar(
            "datos/repartidores.csv",

            [
                {
                    "nombre": r.nombre,
                    "vehiculo": r.vehiculo,
                    "zona_actual": r.zona_actual,
                    "paquetes_asignados": ",".join(r.paquetes_asignados)
                }

                for r in self.repartidores.values()
            ],

            [
                "nombre",
                "vehiculo",
                "zona_actual",
                "paquetes_asignados"
            ]
        )

    # ==========================
    # CLIENTES
    # ==========================

    def crear_cliente(self):

        id = input("ID: ")

        if id in self.clientes:
            print("Ese cliente ya existe.")
            return

        nombre = input("Nombre: ")
        direccion = input("Dirección: ")

        self.clientes[id] = Cliente(
            id,
            nombre,
            direccion
        )

        print("Cliente registrado.")

    # ==========================
    # REPARTIDORES
    # ==========================

    def crear_repartidor(self):

        nombre = input("Nombre: ")

        if nombre in self.repartidores:
            print("Ya existe.")
            return

        vehiculo = input("Vehículo: ")
        zona = input("Zona actual: ")

        self.repartidores[nombre] = Repartidor(
            nombre,
            vehiculo,
            zona
        )

        print("Repartidor registrado.")

    # ==========================
    # PAQUETES
    # ==========================

    def registrar_paquete(self):

        codigo = input("Código: ")

        if codigo in self.paquetes:
            print("Ese código ya existe.")
            return

        cliente = input("ID Cliente: ")

        if cliente not in self.clientes:
            print("Cliente inexistente.")
            return

        peso = float(input("Peso: "))
        destino = input("Destino: ")

        paquete = Paquete(
            codigo,
            peso,
            destino,
            cliente
        )

        self.paquetes[codigo] = paquete

        self.clientes[cliente].agregar_pedido(codigo)

        print("Paquete registrado.")

    # ==========================
    # BUSCAR
    # ==========================

    def buscar_paquete(self):

        codigo = input("Código: ")

        if codigo not in self.paquetes:
            print("No encontrado.")
            return

        paquete = self.paquetes[codigo]
        cliente = self.clientes[paquete.cliente]

        print("---------------------")
        print("Cliente :", cliente.nombre)
        print("Destino :", paquete.destino)
        print("Estado  :", paquete.estado)
        print("Peso    :", paquete.peso)

    # ==========================
    # ESTADO
    # ==========================

    def cambiar_estado(self):

        codigo = input("Código: ")

        if codigo not in self.paquetes:
            print("No existe.")
            return

        print("1 Pendiente")
        print("2 En ruta")
        print("3 Entregado")
        print("4 Cancelado")

        op = input("Nuevo estado: ")

        estados = {
            "1": "Pendiente",
            "2": "En ruta",
            "3": "Entregado",
            "4": "Cancelado"
        }

        if op not in estados:
            print("Estado inválido.")
            return

        self.paquetes[codigo].estado = estados[op]

        print("Estado actualizado.")

    # ==========================
    # ASIGNAR
    # ==========================

    def asignar_paquete(self):

        codigo = input("Código del paquete: ")

        if codigo not in self.paquetes:
            print("No existe.")
            return

        nombre = input("Nombre del repartidor: ")

        if nombre not in self.repartidores:
            print("No existe.")
            return

        paquete = self.paquetes[codigo]
        repartidor = self.repartidores[nombre]

        resultado = self.ciudad.buscar_ruta(
            repartidor.zona_actual,
            paquete.destino
        )

        if resultado is None:
            print("No existe ruta.")
            return

        ruta, distancia = resultado

        repartidor.asignar(codigo)

        print("\nPaquete asignado")
        print("Ruta:", " -> ".join(ruta))
        print("Distancia:", distancia)

    # ==========================
    # MOSTRAR
    # ==========================

    def mostrar_clientes(self):

        for c in self.clientes.values():

            print(
                c.id,
                c.nombre,
                c.direccion,
                c.historial_pedidos
            )

    def mostrar_paquetes(self):

        for p in self.paquetes.values():

            print(
                p.codigo,
                p.destino,
                p.estado,
                p.peso
            )

    def mostrar_repartidores(self):

        for r in self.repartidores.values():

            print(
                r.nombre,
                r.vehiculo,
                r.zona_actual,
                r.paquetes_asignados
            )

    # ==========================
    # ORDENAMIENTOS
    # ==========================

    def ordenar_por_peso(self):

        lista = sorted(
            self.paquetes.values(),
            key=lambda p: p.peso
        )

        for p in lista:

            print(
                p.codigo,
                p.peso
            )

    def ordenar_por_distancia(self):

        lista = []

        for paquete in self.paquetes.values():

            resultado = self.ciudad.buscar_ruta(
                "Centro",
                paquete.destino
            )

            if resultado:

                ruta, distancia = resultado

                lista.append(
                    (
                        paquete,
                        distancia
                    )
                )

        lista.sort(
            key=lambda x: x[1]
        )

        for paquete, distancia in lista:

            print(
                paquete.codigo,
                paquete.destino,
                distancia
            )