class Producto: 
    def __init__(self,
        nombre: str,
        categoria: str,
        precio: float,
        calorias: int,
        disponible: bool = True):
        
        
        self.nombre = nombre
        
        self.categoria = categoria
        
        self.precio = precio
        
        self.calorias = calorias
        
        self.disponible = disponible
        
    def mostrar_info(self) -> str:
        disponibilidad = "Disponible" if self.disponible else "No disponible"
        return (
            f" Producto: {self.nombre}"
            f" Categoria: {self.categoria}"
            f" Precio: ${self.precio}"
            f" Calorías: {self.calorias}"
            f" Disponibilidad: {disponibilidad}"
        )

    def __str__(self):
        return f"{self.nombre} - ${self.precio}: {self.categoria}"