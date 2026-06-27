class Restaurante:
    def __init__(
        self, nombre: str, direccion: str, telefono: str):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.menu = []
        self.clientes = []
        
        
    def agregar_plato(self, plato) -> None:
        self.menu.append(plato)
        

    def mostrar_menu(self) -> None:
        for plato in self.menu:
            print(plato.mostrar_info())
            
    def agregar_cliente(self, cliente) -> None:
        self.clientes.append(cliente)  
        
    def mostrar_clientes(self) -> None:
        for cliente in self.clientes:
            print(cliente.mostrar_info())      