from modelos.cliente import Cliente
from modelos.producto import Producto
from servicios.restaurante import Restaurante

def main():
    producto1 = Producto("Lomo Saltado", "Plato fuerte", 12.50, 650, True)
    producto2 = Producto("Ensalada César", "Entrada", 7.00, 320, True)
    producto3 = Producto("Jugo de Maracuyá", "Bebida", 3.50, 120, False)


    cliente1 = Cliente("María Rodríguez", "maria@correo.com", "0991234567", 34, True)
    cliente2 = Cliente("Andrés Mora", "andres@correo.com", "0987654321", 27, False)

   
    restaurante = Restaurante("El Buen Sabor", "Av. Principal 123", "072345678")

   
    restaurante.agregar_plato(producto1)
    restaurante.agregar_plato(producto2)
    restaurante.agregar_plato(producto3)
    restaurante.agregar_cliente(cliente1)
    restaurante.agregar_cliente(cliente2)


    print(f"=== {restaurante.nombre} ===\n")
    print(producto1)
    print(cliente1)
    print("--- MENÚ ---")
    restaurante.mostrar_menu()
    print("\n--- CLIENTES ---")
    restaurante.mostrar_clientes()

if __name__ == "__main__":
    main()