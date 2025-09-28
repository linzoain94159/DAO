class Equipo:
    def __init__(self, id_equipo, nombre, ciudad, estadio):
        self.id_equipo = id_equipo
        self.nombre = nombre
        self.ciudad = ciudad
        self.estadio = estadio
        self.partidos_jugados = 0
        self.partidos_local = 0
        self.partidos_visitante = 0
        self.goles_realizados = 0
        self.goles_recibidos = 0
        self.partidos_ganados = 0
        self.partidos_empatados = 0
        self.partidos_perdidos = 0
        self.puntos = 0

    def registrar_partido(self, partido, es_local):
        self.partidos_jugados += 1
        if es_local:
            self.partidos_local += 1
            goles_favor = partido.goles_local
            goles_contra = partido.goles_visitante
        else:
            self.partidos_visitante += 1
            goles_favor = partido.goles_visitante
            goles_contra = partido.goles_local

        self.goles_realizados += goles_favor
        self.goles_recibidos += goles_contra

        if goles_favor > goles_contra:
            self.partidos_ganados += 1
            self.puntos += 3
        elif goles_favor == goles_contra:
            self.partidos_empatados += 1
            self.puntos += 1
        else:
            self.partidos_perdidos += 1

    def diferencia_goles(self):
        return self.goles_realizados - self.goles_recibidos

    def __str__(self):
        return (f"{self.nombre} | PJ: {self.partidos_jugados} | Local: {self.partidos_local} | "
                f"Visitante: {self.partidos_visitante} | GF: {self.goles_realizados} | "
                f"GC: {self.goles_recibidos} | DG: {self.diferencia_goles()} | "
                f"G: {self.partidos_ganados} | E: {self.partidos_empatados} | "
                f"P: {self.partidos_perdidos} | Pts: {self.puntos}")
    
    def cargarEquipos(lista_equipos):
        equipos = lista_equipos
        cant = int(input("Ingrese la cantidad de equipos a cargar: "))
        for i in range(cant):
            id_equipo = len (equipos) + 1
            nombre = input(f"Ingrese el nombre del equipo {id_equipo}: ")
            ciudad = input(f"Ingrese la ciudad del equipo {id_equipo}: ")
            estadio = input(f"Ingrese el estadio del equipo {id_equipo}: ")
            equipo = Equipo(id_equipo, nombre, ciudad, estadio)
            equipos.append(equipo)
            print(equipo)
        return equipos

    def equiposCargados(Equipos):
        print("Equipos cargados:")
        for equipo in Equipos:
            print(f"{equipo.id_equipo}. {equipo.nombre}")

    def cantidadPartidos(Equipos):
        Equipo.equiposCargados(Equipos)
        id = int(input("Ingrese el ID del equipo para ver la cantidad de partidos jugados: ")) - 1
        print(f"El equipo {Equipos[id].nombre} ha jugado {Equipos[id].partidos_jugados} partidos.")

    def cantidadPartidosLocal(Equipos):
        Equipo.equiposCargados(Equipos)
        id = int(input("Ingrese el ID del equipo para ver la cantidad de partidos jugados como local: ")) - 1
        print(f"El equipo {Equipos[id].nombre} ha jugado {Equipos[id].partidos_local} partidos como local.")

    def cantidadPartidosVisitante(Equipos):
        Equipo.equiposCargados(Equipos)
        id = int(input("Ingrese el ID del equipo para ver la cantidad de partidos jugados como visitante: ")) - 1
        print(f"El equipo {Equipos[id].nombre} ha jugado {Equipos[id].partidos_visitante} partidos como visitante.")

    def cantidadGolesRealizados(Equipos):
        Equipo.equiposCargados(Equipos)
        id = int(input("Ingrese el ID del equipo para ver la cantidad de goles realizados: ")) - 1
        print(f"El equipo {Equipos[id].nombre} ha realizado {Equipos[id].goles_realizados} goles.")
    
    def cantidadGolesRecibidos(Equipos):
        Equipo.equiposCargados(Equipos)
        id = int(input("Ingrese el ID del equipo para ver la cantidad de goles recibidos: ")) - 1
        print(f"El equipo {Equipos[id].nombre} ha recibido {Equipos[id].goles_recibidos} goles.")

    def diferenciaGoles(Equipos):
        Equipo.equiposCargados(Equipos)
        id = int(input("Ingrese el ID del equipo para ver la diferencia de goles: ")) - 1
        print(f"El equipo {Equipos[id].nombre} tiene una diferencia de goles de {Equipos[id].diferencia_goles()}.")

    def cantidadPartidosGanados(Equipos):
        Equipo.equiposCargados(Equipos)
        id = int(input("Ingrese el ID del equipo para ver la cantidad de partidos ganados: ")) - 1
        print(f"El equipo {Equipos[id].nombre} ha ganado {Equipos[id].partidos_ganados} partidos.")

    def cantidadPartidosEmpatados(Equipos):
        Equipo.equiposCargados(Equipos)
        id = int(input("Ingrese el ID del equipo para ver la cantidad de partidos empatados: ")) - 1
        print(f"El equipo {Equipos[id].nombre} ha empatado {Equipos[id].partidos_empatados} partidos.")

    def cantidadPartidosPerdidos(Equipos):
        Equipo.equiposCargados(Equipos)
        id = int(input("Ingrese el ID del equipo para ver la cantidad de partidos perdidos: ")) - 1
        print(f"El equipo {Equipos[id].nombre} ha perdido {Equipos[id].partidos_perdidos} partidos.")
    
    def puntosObtenidos(Equipos):
        Equipo.equiposCargados(Equipos)
        id = int(input("Ingrese el ID del equipo para ver los puntos obtenidos: ")) - 1
        print(f"El equipo {Equipos[id].nombre} ha obtenido {Equipos[id].puntos} puntos.")


class Partido:
    def __init__(self, id_partido, equipo_local, equipo_visitante, fecha, goles_local, goles_visitante):
        self.id_partido = id_partido
        self.equipo_local = equipo_local
        self.equipo_visitante = equipo_visitante
        self.fecha = fecha
        self.goles_local = goles_local
        self.goles_visitante = goles_visitante

    def ganador(self):
        if self.goles_local > self.goles_visitante:
            return self.equipo_local
        elif self.goles_local < self.goles_visitante:
            return self.equipo_visitante
        else:
            return None

    def es_empate(self):
        return self.goles_local == self.goles_visitante

    def __str__(self):
        return (f"{self.equipo_local.nombre} {self.goles_local} - {self.goles_visitante} {self.equipo_visitante.nombre} ({self.fecha})")
    
    def cargarPartidos(Partidos, Equipos):
        partidos = Partidos
        cant = int(input("Ingrese la cantidad de partidos a cargar: "))
        for i in range(cant):
            id_partido = len(partidos) + 1
            for equipo in Equipos:
                print(f"{equipo.id_equipo}. {equipo.nombre}")
            id_local = int(input("Ingrese el ID del equipo local: ")) - 1
            id_visitante = int(input("Ingrese el ID del equipo visitante: ")) - 1
            fecha = input("Ingrese la fecha del partido (DD/MM/AAAA): ")
            goles_local = int(input("Ingrese la cantidad de goles del equipo local: "))
            goles_visitante = int(input("Ingrese la cantidad de goles del equipo visitante: "))
            partido = Partido(id_partido, Equipos[id_local], Equipos[id_visitante], fecha, goles_local, goles_visitante)
            partidos.append(partido)
            Equipos[id_local].registrar_partido(partido, True)
            Equipos[id_visitante].registrar_partido(partido, False)
        print("Partidos cargados:")
        for partido in partidos:
            print(partido)

def principal():
    Equipos = []
    opcion = 0
    Partidos = []
    while opcion != 14:
        print(
        "Bienvenido al sistema de gestión de partidos y equipos.\n"
        "Seleccione una opción:\n"
        "1. Cargar Equipos\n"
        "2. Cargar Partidos\n"
        "3. Cantidad de Partidos\n"
        "4. Cantidad de partidos jugados como local\n"
        "5. Cantidad de partidos jugados como visitante\n"
        "6. Cantidad de goles realizados\n"
        "7. Cantidad de goles recibidos\n"
        "8. Diferencia de goles\n"
        "9. Cantidad de partidos ganados\n"
        "10. Cantidad de partidos empatados\n"
        "11. Cantidad de partidos perdidos\n"
        "12. Puntos obtenidos\n"
        "13. Mostrar equipos de la liga\n"
        "14. Cancelar")

        opcion = int(input("Ingrese una opción: "))
        if opcion == 1:
            Equipos = Equipo.cargarEquipos(Equipos)
        elif opcion == 2:
            Partidos = Partido.cargarPartidos(Partidos, Equipos)
        elif opcion == 3:
            Equipo.cantidadPartidos(Equipos)
        elif opcion == 4:
            Equipo.cantidadPartidosLocal(Equipos)
        elif opcion == 5:
            Equipo.cantidadPartidosVisitante(Equipos)
        elif opcion == 6:
            Equipo.cantidadGolesRealizados(Equipos)
        elif opcion == 7:
            Equipo.cantidadGolesRecibidos(Equipos)
        elif opcion == 8:
            Equipo.diferenciaGoles(Equipos)
        elif opcion == 9:
            Equipo.cantidadPartidosGanados(Equipos)
        elif opcion == 10:
            Equipo.cantidadPartidosEmpatados(Equipos)
        elif opcion == 11:
            Equipo.cantidadPartidosPerdidos(Equipos)
        elif opcion == 12:
            Equipo.puntosObtenidos(Equipos)
        elif opcion == 13:
            Equipo.equiposCargados(Equipos)
        elif opcion == 14:
            print("Saliendo del sistema. ¡Hasta luego!")



if __name__ == "__main__":
    principal()