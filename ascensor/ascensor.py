
class Ascensor:
    def __init__(self, piso_minimo, piso_maximo, capacidad):
        if piso_minimo >= 0 or piso_maximo <= 0 or piso_minimo >= piso_maximo:
            raise ValueError("Rango de pisos inválido")
        if capacidad <= 0:
            raise ValueError("Capacidad debe ser mayor que 0")
        self.capacidad = capacidad
        self.piso_minimo = piso_minimo
        self.piso_maximo = piso_maximo
        self.piso_actual = 0
        self.personas = 0

    def __str__(self):
        return f"Ascensor en piso {self.piso_actual} con {self.personas}/{self.capacidad} personas"
    
    def ir_a_piso(self, piso):
        if self.piso_minimo <= piso <= self.piso_maximo:
            self.piso_actual = piso
            return True
        return False
    
    def piso_actual(self):
        return self.piso_actual
    
    def subir(self, cantidad):
        if cantidad <= 0:
            return -1
        espacio_disponible = self.capacidad - self.personas
        if espacio_disponible >= cantidad:
            self.personas += cantidad
            return cantidad
        elif espacio_disponible > 0:
            self.personas += espacio_disponible
            return espacio_disponible
        return espacio_disponible
    
    def bajar(self, cantidad):
        if cantidad <= 0:
            return -1
        if self.personas >= cantidad:
            self.personas -= cantidad
            return cantidad
        bajan_todos = self.personas
        self.personas = 0
        return bajan_todos