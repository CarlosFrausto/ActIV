class Cliente:

    def __init__(self, id, nombre, direccion):
        self.id = id
        self.nombre = nombre
        self.direccion = direccion
        self.historial_pedidos = []

    def agregar_pedido(self, codigo):
        self.historial_pedidos.append(codigo)