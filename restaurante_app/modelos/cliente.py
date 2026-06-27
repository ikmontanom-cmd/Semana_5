class Cliente:
    
    def __init__(
        self, 
        nombre: str,
        correo_electronico: str, 
        telefono: str,
        edad: int,
        es_frecuente: bool
        ):
        self.nombre = nombre
        
        self.correo_electronico = correo_electronico
        
        self.telefono = telefono
        
        self.edad = edad
        
        self.es_frecuente = es_frecuente

    def mostrar_info(self) -> str:
        frecuencia = "Cliente frecuente" if self.es_frecuente else "Cliente ocasional"
        return (
              f" Nombre: {self.nombre}"
              f" Correo electrónico: {self.correo_electronico}"
              f" Teléfono: {self.telefono}"
              f" Edad: {self.edad}"
              f" Frecuencia: {frecuencia}"
         )
    
    


    def __str__(self):
        return f"Cliente: {self.nombre}, Correo: {self.correo_electronico}, Teléfono: {self.telefono}"