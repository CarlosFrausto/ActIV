from gestor import Gestor


def mostrar_menu():

    print("\n" + "=" * 40)
    print("   SISTEMA DE LOGÍSTICA DE ENTREGAS")
    print("=" * 40)
    print("1. Crear cliente")
    print("2. Registrar paquete")
    print("3. Crear repartidor")
    print("4. Buscar paquete")
    print("5. Cambiar estado de paquete")
    print("6. Asignar paquete a repartidor")
    print("7. Mostrar clientes")
    print("8. Mostrar paquetes")
    print("9. Mostrar repartidores")
    print("10. Buscar ruta")
    print("11. Ordenar paquetes por peso")
    print("12. Ordenar paquetes por distancia")
    print("0. Guardar y salir")


def main():

    gestor = Gestor()

    while True:

        mostrar_menu()

        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":

            gestor.crear_cliente()

        elif opcion == "2":

            gestor.registrar_paquete()

        elif opcion == "3":

            gestor.crear_repartidor()

        elif opcion == "4":

            gestor.buscar_paquete()

        elif opcion == "5":

            gestor.cambiar_estado()

        elif opcion == "6":

            gestor.asignar_paquete()

        elif opcion == "7":

            gestor.mostrar_clientes()

        elif opcion == "8":

            gestor.mostrar_paquetes()

        elif opcion == "9":

            gestor.mostrar_repartidores()

        elif opcion == "10":

            origen = input("Zona de origen: ")
            destino = input("Zona destino: ")

            resultado = gestor.ciudad.buscar_ruta(origen, destino)

            if resultado:

                ruta, distancia = resultado

                print("\nRuta encontrada:")
                print(" -> ".join(ruta))
                print(f"Distancia total: {distancia}")

            else:

                print("No existe una ruta entre esas zonas.")

        elif opcion == "11":

            gestor.ordenar_por_peso()

        elif opcion == "12":

            gestor.ordenar_por_distancia()

        elif opcion == "0":

            gestor.guardar_datos()

            print("\nDatos guardados correctamente.")
            print("Hasta luego.")

            break

        else:

            print("Opción inválida.")


if __name__ == "__main__":
    main()