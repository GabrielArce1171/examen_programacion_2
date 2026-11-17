class Rectangulo(object): 
    def __init__(self, base, altura): 
        # COMPLETAR: guardar las propiedades 
        self.base = base
        self.altura = altura
        pass 
  
    def calcularArea(self): 
        # COMPLETAR: regresar el área 
        return self.base * self.altura
  
    def mostrarArea(self): 
        # COMPLETAR: mostrar el resultado 
        print(f"Base: {self.base}")
        print(f"Altura: {self.altura}")
        print(f"Área: {self.calcularArea()}")