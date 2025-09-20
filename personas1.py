class Persona:
    def __init__(self, nombre, apellido, edad, documento):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.documento = documento
    
    def __str__(self):
        return f"Nombre: {self.nombre}, Apellido: {self.apellido}, Edad: {self.edad}, Documento: {self.documento}"


def cargarPersona():
    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")
    edad = int(input("Ingrese la edad: "))
    documento = int(input("Ingrese el documento: "))
    return Persona(nombre, apellido, edad, documento)


def principal():
    cantidad = int(input("Ingrese la cantidad de personas a cargar: "))
    menor = None
    for i in range (cantidad):
        persona = cargarPersona()
        print(persona)
        if menor is None or persona.edad < menor.edad:
            menor = persona

    print("La persona de menor edad es:")
    print(menor)

if __name__ == "__main__":
    principal()




