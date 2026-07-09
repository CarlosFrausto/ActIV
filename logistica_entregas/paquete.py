class Paquete:

    def __init__(
        self,
        codigo,
        peso,
        destino,
        cliente,
        estado="Pendiente"
    ):

        self.codigo = codigo
        self.peso = float(peso)
        self.destino = destino
        self.estado = estado
        self.cliente = cliente