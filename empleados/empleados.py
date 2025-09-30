from abc import abstractmethod


class Empelado():
    def __init__(self, tipo, legajo, nombre, apellido, basico):
        self.tipo = tipo
        self.legajo = legajo
        self.nombre = nombre
        self.apellido = apellido
        self.basico = basico

    @abstractmethod
    def calcular_sueldo(self):
        pass

    def __str__(self):
        return f"Legajo: {self.legajo} - Nombre: {self.nombre} {self.apellido} - Tipo: {self.tipo} - Basico: {self.basico}"


class Obrero(Empelado):
    def __init__(self, tipo, legajo, nombre, apellido, basico, dias):
        super().__init__(tipo, legajo, nombre, apellido, basico)
        self.dias = dias

    def calcular_sueldo(self):
        sueldo = (self.basico / 20) * self.dias
        return sueldo
    
    def __str__(self):
        return super().__str__() + f" - Dias trabajados: {self.dias} - Sueldo: {self.calcular_sueldo()}"

class Administrativo(Empelado):
    def __init__(self, tipo, legajo, nombre, apellido, basico, presentismo):
        super().__init__(tipo, legajo, nombre, apellido, basico)
        self.presentismo = presentismo

    def calcular_sueldo(self):
        if self.presentismo:
            sueldo = self.basico * 1.13
        else:
            sueldo = self.basico
        return sueldo
    
    def __str__(self):
        return super().__str__() + f" - Presentismo: {self.presentismo} - Sueldo: {self.calcular_sueldo()}"
    
    
    

class Vendedor(Empelado):
    def __init__(self, tipo, legajo, nombre, apellido, basico, ventas):
        super().__init__(tipo, legajo, nombre, apellido, basico)
        self.ventas = ventas

    def calcular_sueldo(self):
        sueldo = self.basico + (self.ventas * 0.01)
        return sueldo
    
    def __str__(self):
        return super().__str__() + f" - Ventas: {self.ventas} - Sueldo: {self.calcular_sueldo()}"



