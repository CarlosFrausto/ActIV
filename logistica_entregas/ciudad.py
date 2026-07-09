class Ciudad:

    def __init__(self):

        self.grafo = {

            "Centro": {
                "Avenida1": 2,
                "Mercado": 4
            },

            "Avenida1": {
                "Centro": 2,
                "Zona Norte": 3,
                "Hospital": 5
            },

            "Mercado": {
                "Centro": 4,
                "Zona Sur": 6
            },

            "Hospital": {
                "Avenida1": 5,
                "Zona Este": 2
            },

            "Zona Norte": {
                "Avenida1": 3
            },

            "Zona Sur": {
                "Mercado": 6
            },

            "Zona Este": {
                "Hospital": 2
            }

        }

    def buscar_ruta(self, origen, destino):

        return self.__dfs(origen, destino, [], 0)

    def __dfs(self, actual, destino, visitados, distancia):

        visitados.append(actual)

        if actual == destino:
            return visitados, distancia

        for vecino, peso in self.grafo[actual].items():

            if vecino not in visitados:

                resultado = self.__dfs(
                    vecino,
                    destino,
                    visitados.copy(),
                    distancia + peso
                )

                if resultado:
                    return resultado

        return None