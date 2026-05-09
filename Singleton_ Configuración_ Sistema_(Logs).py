#
# # # UNIDAD 2: PATRONES DE DISEÑO, INGENIERÍA DE SOFTWARE 
#  # CÓDIGO DE EJEMPLO PARA EL PATRÓN DE DISEÑO SINGLETON EN PYTHON
#

class LoggerSingleton:
    _instancia = None

    def __new__(cls):
        # El corazón del Singleton: solo se crea el objeto si _instancia es None
        if cls._instancia is None:
            print("\n[SISTEMA]: Creando nueva instancia ÚNICA del Logger en memoria...")
            cls._instancia = super(LoggerSingleton, cls).__new__(cls)
            cls._instancia.historial = []  # Lista para guardar mensajes
        return cls._instancia

    def escribir_log(self, mensaje):
        self.historial.append(mensaje)
        print(f"[LOG GUARDADO]: {mensaje}")

    def mostrar_historial(self):
        print(f"\n--- Historial del Logger (ID: {id(self)}) ---")
        for i, msg in enumerate(self.historial, 1):
            print(f"{i}. {msg}")

# --- Ejecución Interactiva ---
if __name__ == "__main__":
    print("--- Escenario Singleton: Sistema de Registro ---")
    
    # Intentamos crear el primer logger
    print("Intentando crear 'logger_A'...")
    logger_A = LoggerSingleton()
    
    # Pedimos un mensaje al usuario
    msj1 = input("Escribe un mensaje para logger_A: ")
    logger_A.escribir_log(msj1)

    print("-" * 30)

    # Intentamos crear un segundo logger
    print("Intentando crear 'logger_B'...")
    logger_B = LoggerSingleton()
    
    # Pedimos otro mensaje
    msj2 = input("Escribe un mensaje para logger_B: ")
    logger_B.escribir_log(msj2)

    print("-" * 30)

    # Verificación final
    print(f"ID en memoria de logger_A: {id(logger_A)}")
    print(f"ID en memoria de logger_B: {id(logger_B)}")

    if logger_A is logger_B:
        print("\n¡MAGIA! Ambos son el mismo objeto. logger_B no se creó de cero.")
    
    # Mostramos que logger_B tiene los mensajes que le enviamos a logger_A
    logger_B.mostrar_historial()
