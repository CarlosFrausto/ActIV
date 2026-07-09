class Repartidor:

    def __init__(self, nombre, vehiculo, zona_actual):

        self.nombre = nombre
        self.vehiculo = vehiculo
        self.zona_actual = zona_actual
        self.paquetes_asignados = []

    def asignar(self, codigo):
        self.paquetes_asignados.append(codigo)