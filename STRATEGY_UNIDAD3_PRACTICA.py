
# UNIDAD 2: PATRONES DE DISEÑO, INGENIERÍA DE SOFTWARE 
# CÓDIGO DE EJEMPLO PARA EL PATRÓN DE DISEÑO STRATEGY EN PYTHON
from abc import ABC, abstractmethod

# 1.---- Interfaz Estrategia (Strategy)
class MetodoPago(ABC): #Actúa como un contrato.
    # Define que cualquier forma de pago debe tener el método procesar_pago
    @abstractmethod
    def procesar_pago(self, monto, usuario):
        pass

# 2.----- Estrategias Concretas, cada una sabe cómo manejar el pago a su manera
class PagoTarjeta(MetodoPago):
    def procesar_pago(self, monto, usuario):
        return f"Hola {usuario}. Procesando ${monto} con Tarjeta de Crédito (Validando CVV...)"

class PagoPayPal(MetodoPago):
    def procesar_pago(self, monto, usuario):
        return f"Hola {usuario}. Procesando ${monto} con PayPal (Redirigiendo a cuenta de correo...)"

class PagoEfectivo(MetodoPago): # Agregamos una opción extra para variedad
    def procesar_pago(self, monto, usuario):
        return f"Hola {usuario}. Procesando ${monto} en Efectivo (Generando ticket de pago...)"

# 3. ----- Contexto (El Carrito de Compras), objeto principal que usa el cliente
# No sabe cómo se paga, solo sabe que debe ejecutar la estrategia que tenga asignada en ese momento.
class CarritoCompras:
    def __init__(self, usuario):
        self.usuario = usuario
        self._estrategia_pago = None

    def establecer_estrategia(self, estrategia_pago: MetodoPago):
        self._estrategia_pago = estrategia_pago

    def realizar_checkout(self, monto):
        if self._estrategia_pago:
            resultado = self._estrategia_pago.procesar_pago(monto, self.usuario)
            print(resultado)
        else:
            print("Error: No se ha seleccionado un método de pago.")

# --- Ejecución Interactiva ---
if __name__ == "__main__":
    print("--- Sistema de Pagos Interactivos ---")
    
    # Captura de datos del usuario
    nombre = input("Por favor, ingresa tu nombre: ")
    monto_total = float(input("Ingresa el monto a pagar: "))
    
    # Inicializamos el carrito con el nombre del usuario
    carrito = CarritoCompras(nombre)
    
    print("\nMétodos de pago disponibles:")
    print("1. Tarjeta de Crédito")
    print("2. PayPal")
    print("3. Efectivo")
    
    opcion = input("Selecciona una opción (1-3): ")

    # Lógica para asignar la estrategia según la entrada
    if opcion == "1":
        carrito.establecer_estrategia(PagoTarjeta())
    elif opcion == "2":
        carrito.establecer_estrategia(PagoPayPal())
    elif opcion == "3":
        carrito.establecer_estrategia(PagoEfectivo())
    else:
        print("Opción no válida.")

    # Ejecución del proceso
    if carrito._estrategia_pago:
        print("\n--- Resumen de Transacción ---")
        carrito.realizar_checkout(monto_total)
