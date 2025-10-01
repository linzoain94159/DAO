# Curso: 4k3
# Nombre: Linzoain, Ignacio
# Legajo: 94159

from __future__ import annotations
from abc import ABC, abstractmethod

class Hotel:
    def __init__(self, ruta: str):
        
        self.habitaciones: list[Habitacion] = []
        self._cargar_desde_archivo(ruta)

    def _cargar_desde_archivo(self, ruta: str) -> None:
        with open(ruta, encoding="utf-8") as archivo:
            for linea in archivo:
                linea = linea.strip()
                if not linea:
                    continue
                datos = [x.strip() for x in linea.split(",")]
                tipo_hab = int(datos[0])
                numero = int(datos[1])
                huesped = datos[2]
                costo_base = float(datos[3])
                noches = int(datos[4])

                if tipo_hab == 1:
                    hab = Estandar(numero, huesped, costo_base, noches)
                elif tipo_hab == 2:
                    vista_mar = datos[5].lower() == "true"
                    hab = Suite(numero, huesped, costo_base, noches, vista_mar)
                elif tipo_hab == 3:
                    jacuzzi = datos[5].lower() == "true"
                    hab = SuitePremium(numero, huesped, costo_base, noches, jacuzzi)
                else:
                    continue

                self.agregar_habitacion(hab)

    def agregar_habitacion(self, habitacion: "Habitacion") -> None:
        self.habitaciones.append(habitacion)

    def calcular_costo_total(self) -> float:
        return sum(h.costo_base * h.noches for h in self.habitaciones)

    def cantidad_habitaciones(self):
        # devolver la lista (los tests usan len() sobre esto)
        return self.habitaciones

    def calcular_ingresos(self) -> float:
        return sum(h.calcular_costo() for h in self.habitaciones)

    def calcular_ingreso_total(self) -> float:
        return self.calcular_ingresos()

    def obtener_suma_reservas(self) -> float:
        return self.calcular_ingresos()

    def obtener_reserva_mas_cara(self) -> "Habitacion | None":
        return max(self.habitaciones, key=lambda h: h.calcular_costo(), default=None)

    def suites_con_vista_al_mar(self) -> list["Suite"]:
        return [h for h in self.habitaciones if isinstance(h, Suite) and h.vista_mar]

    def suites_premium_con_jacuzzi(self) -> list["SuitePremium"]:
        return [h for h in self.habitaciones if isinstance(h, SuitePremium) and h.jacuzzi]

    def contar_suites_vista_mar(self) -> int:
        return sum(1 for h in self.habitaciones if isinstance(h, Suite) and h.vista_mar)

    def contar_suites_premium_jacuzzi(self) -> int:
        return sum(1 for h in self.habitaciones if isinstance(h, SuitePremium) and h.jacuzzi)

    def cantidad_por_tipo(self) -> dict[str, int]:
        resumen = {"Estandar": 0, "Suite": 0, "SuitePremium": 0}
        for h in self.habitaciones:
            if isinstance(h, Estandar):
                resumen["Estandar"] += 1
            elif isinstance(h, Suite):
                resumen["Suite"] += 1
            elif isinstance(h, SuitePremium):
                resumen["SuitePremium"] += 1
        return resumen


class Habitacion(ABC):
    def __init__(self, numero: int, huesped: str, costo_base: float, noches: int):
        self.numero = numero
        self.huesped = huesped
        self.costo_base = costo_base
        self.noches = noches

    @abstractmethod
    def calcular_costo(self) -> float:
        ...

    def calcular_costo_total(self) -> float:
        return self.calcular_costo()

    def __str__(self) -> str:
        return (
            f"Habitacion {self.numero} - Huesped: {self.huesped} - "
            f"Costo Base: {self.costo_base} - Costo Total: ${self.calcular_costo():.2f}"
        )


class Estandar(Habitacion):
    def __init__(self, numero: int, huesped: str, costo_base: float, noches: int, *_):
        super().__init__(numero, huesped, costo_base, noches)
        self.tipo = 1  # siempre 1

    def calcular_costo(self) -> float:
        return self.costo_base * self.noches

    def __str__(self) -> str:
        return (
            f"Habitacion {self.numero} - Tipo: {self.tipo} - "
            f"Huesped: {self.huesped} - Costo Base: {self.costo_base} - "
            f"Costo Total: ${self.calcular_costo():.2f}"
        )


class Suite(Habitacion):
    def __init__(self, numero: int, huesped: str, costo_base: float, noches: int, vista_mar: bool, *_):
        super().__init__(numero, huesped, costo_base, noches)
        self.vista_mar = vista_mar
        self.tipo = 2

    def calcular_costo(self) -> float:
        costo = self.costo_base * self.noches
        if self.vista_mar:
            costo *= 1.10
        return costo

    def __str__(self) -> str:
        return (
            f"Habitacion {self.numero} - Tipo: {self.tipo} "
            f"({'Vista al mar' if self.vista_mar else 'Sin vista'}) - "
            f"Huesped: {self.huesped} - Costo Base: {self.costo_base} - "
            f"Costo Total: ${self.calcular_costo():.2f}"
        )


class SuitePremium(Habitacion):
    def __init__(self, numero: int, huesped: str, costo_base: float, noches: int, jacuzzi: bool, *_):
        super().__init__(numero, huesped, costo_base, noches)
        self.jacuzzi = jacuzzi
        self.tipo = 3

    def calcular_costo(self) -> float:
        costo = self.costo_base * self.noches
        if self.jacuzzi:
            costo *= 1.20
        return costo

    def __str__(self) -> str:
        return (
            f"Habitacion {self.numero} - Tipo: {self.tipo} "
            f"({'Jacuzzi' if self.jacuzzi else 'Sin jacuzzi'}) - "
            f"Huesped: {self.huesped} - Costo Base: {self.costo_base} - "
            f"Costo Total: ${self.calcular_costo():.2f}"
        )
