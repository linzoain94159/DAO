class Persona:
    def __init__(self, documento, nombre, apellido, edad):
        self.documento = documento
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
    
    def __str__(self):
        return f"Documento: {self.documento}, Nombre: {self.nombre}, Apellido: {self.apellido}, Edad: {self.edad}"
 

def carga_persona():
    m = open("DAO\persona2\personas.csv", "r")
    personas = {}
    for linea in m:
        documento, nombre, apellido, edad = linea.strip().split(",")
        persona = Persona(documento, nombre, apellido, int(edad))
        personas[documento] = persona
    m.close()
    return personas

def principal():
    personas = carga_persona()

    print(f"Total de personas cargadas: {len(personas)}")

    mayores = [p for p in personas.values() if p.edad >= 18]
    print(f"Personas mayores de edad: {len(mayores)}")

    vocales = 'aeiouAEIOU'
    print("Personas cuyo apellido comienza con vocal:")
    for p in personas.values():
        if p.apellido and p.apellido[0] in vocales:
            print(f"{p.nombre} {p.apellido}")

    apellidos = {}
    for p in personas.values():
        apellidos[p.apellido] = apellidos.get(p.apellido, 0) + 1
    print("Cantidad de personas por apellido:")
    for apellido, count in apellidos.items():
        print(f"{apellido}: {count}")


if __name__ == "__main__":
    principal()
