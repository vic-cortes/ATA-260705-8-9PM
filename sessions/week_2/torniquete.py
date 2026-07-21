#!/usr/bin/env python3
"""
Máquina de Estados: Torniquete (Turnstile)

Emula un torniquete de acceso con dos estados:
- Estado 0: BLOQUEADO (no permite el paso)
- Estado 1: DESBLOQUEADO (permite el paso)

Eventos:
- 1: Insertar moneda
- 2: Empujar torniquete
- 0: Salir
"""

from enum import Enum


class Estado(Enum):
    """Estados del torniquete"""
    BLOQUEADO = 0
    DESBLOQUEADO = 1


class Evento(Enum):
    """Eventos que pueden ocurrir"""
    MONEDA = 1
    EMPUJAR = 2
    SALIR = 0



class Torniquete:
    """Máquina de estados del torniquete"""

    def __init__(self):
        """Inicializar torniquete"""
        self.estado = Estado.BLOQUEADO
        self.contador_pasos = 0
        self.activo = True

    @property
    def is_blocked(self) -> bool:
        """Retorna True si el torniquete está bloqueado"""
        return self.estado == Estado.BLOQUEADO
    
    @property
    def is_unblocked(self) -> bool:
        """Retorna True si el torniquete está desbloqueado"""
        return self.estado == Estado.DESBLOQUEADO

    def mostrar_estado(self) -> str:
        """Retornar representación del estado actual"""
        return "🔒 BLOQUEADO" if self.is_blocked else "🔓 DESBLOQUEADO"

    def procesar_evento(self, evento: Evento) -> str:
        """
        Procesar un evento según el estado actual.

        Tabla de transiciones:
        - BLOQUEADO + Moneda → DESBLOQUEADO (permitir paso)
        - BLOQUEADO + Empujar → BLOQUEADO (denegar paso)
        - DESBLOQUEADO + Empujar → BLOQUEADO (registrar paso)
        - DESBLOQUEADO + Moneda → DESBLOQUEADO (mantener desbloqueado)
        """
        mensajes = []

        # ESTADO BLOQUEADO
        if self.is_blocked:
            if evento == Evento.MONEDA:
                mensajes.append("💰 Moneda insertada")
                mensajes.append("✓ Torniquete DESBLOQUEADO - Puedes pasar")
                self.estado = Estado.DESBLOQUEADO

            elif evento == Evento.EMPUJAR:
                mensajes.append("❌ ACCESO DENEGADO")
                mensajes.append("⚠️  El torniquete está bloqueado")
                mensajes.append("⚠️  Inserta una moneda para desbloquear")

            elif evento == Evento.SALIR:
                self.activo = False
                mensajes.append("👋 Programa terminado")

        # ESTADO DESBLOQUEADO
        elif self.is_unblocked:
            if evento == Evento.EMPUJAR:
                mensajes.append("✅ Paso registrado")
                self.contador_pasos += 1
                mensajes.append(f"👤 Persona #{self.contador_pasos} pasó")
                mensajes.append("🔒 Torniquete BLOQUEADO nuevamente")
                self.estado = Estado.BLOQUEADO

            elif evento == Evento.MONEDA:
                mensajes.append("💰 Moneda insertada")
                mensajes.append("ℹ️  Ya está desbloqueado - Puedes pasar")

            elif evento == Evento.SALIR:
                self.activo = False
                mensajes.append("👋 Programa terminado")

        return "\n".join(mensajes)

    def mostrar_menu(self) -> None:
        """Mostrar menú de opciones"""
        print("\nEventos disponibles:")
        print("  1 = Insertar moneda")
        print("  2 = Empujar torniquete")
        print("  0 = Salir")

    def mostrar_resumen(self) -> None:
        """Mostrar resumen final"""
        print("\n" + "=" * 40)
        print("RESUMEN FINAL")
        print("=" * 40)
        print(f"Total de personas que pasaron: {self.contador_pasos}")
        estado_final = "BLOQUEADO" if self.is_blocked else "DESBLOQUEADO"
        print(f"Estado final: {estado_final}")
        print("=" * 40)

    def ejecutar(self) -> None:
        """Ejecutar máquina de estados interactiva"""
        print("=" * 40)
        print("MÁQUINA DE ESTADOS: TORNIQUETE")
        print("=" * 40)

        while self.activo:
            # Mostrar estado actual
            print(f"\nEstado actual: {self.mostrar_estado()}")
            print(f"Pasos registrados: {self.contador_pasos}")

            # Mostrar menú
            self.mostrar_menu()

            # Leer entrada
            try:
                entrada = input("\nIngresa evento: ").strip()
                evento_valor = int(entrada)

                # Convertir a enum
                if evento_valor == 0:
                    evento = Evento.SALIR
                elif evento_valor == 1:
                    evento = Evento.MONEDA
                elif evento_valor == 2:
                    evento = Evento.EMPUJAR
                else:
                    print("❌ Evento inválido")
                    continue

                # Procesar evento
                respuesta = self.procesar_evento(evento)
                print(f"\n{respuesta}")

            except ValueError:
                print("❌ Ingresa un número válido (0, 1 o 2)")

        # Mostrar resumen final
        self.mostrar_resumen()


def main():
    """Punto de entrada del programa"""
    torniquete = Torniquete()
    torniquete.ejecutar()


if __name__ == "__main__":
    main()
