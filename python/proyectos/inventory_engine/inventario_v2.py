# ==============================================================================
# PROYECTO: InventoryEngine - Módulo de Gestión de Almacén con POO
# OBJETIVO: Implementar Encapsulamiento Estricto para proteger métricas financieras
# ==============================================================================

class Producto:
    def __init__(self, nombre: str, precio_inicial: float, stock: int):
        self.nombre = nombre
        # Validamos en el constructor
        if precio_inicial < 0:
            raise ValueError("El precio inicial no puede ser negativo.")
        
        # El doble guion bajo (__) vuelve la variable PRIVADA (Encapsulada en memoria)
        self.__precio = precio_inicial
        self.stock = stock

    # 🔑 EL GETTER: Método formal que PERMITE LEER el precio desde afuera
    @property
    def precio(self):
        return self.__precio

    # 🔒 EL SETTER: Método formal que CONTROLA la modificación del precio
    @precio.setter
    def precio(self, nuevo_precio: float):
        if nuevo_precio < 0:
            print("🛑 ERROR DE VALIDACIÓN: Intento de asignar un precio negativo rechazado.")
        else:
            self.__precio = nuevo_precio
            print(f"✅ Precio de '{self.nombre}' actualizado correctamente a ${self.__precio}")


# === DEMOSTRACIÓN DE CONTROL EN PRODUCCIÓN ===
if __name__ == "__main__":
    print("=== INVENTORY ENGINE: Validando Seguridad de Memoria ===")
    
    # 1. Instanciar el producto base
    item = Producto("Arroz", 50.0, 100)
    
    # 2. Lectura autorizada a través del Getter
    print(f"Producto: {item.nombre} | Precio actual: ${item.precio}")
    
    # 3. Intento de sabotaje directo a la variable privada
    # Esto creará una variable superficial, pero NO alterará el verdadero valor protegido en memoria
    item.__precio = -999.0 
    print(f"🛡️ Intento de alteración directa -> El precio real sigue siendo: ${item.precio}")
    
    # 4. Intento de modificación inválida a través del Setter (Bloqueado por la lógica)
    item.precio = -10.0
    
    # 5. Modificación válida a través del Setter (Aceptado)
    item.precio = 55.5