# =====================
# DATOS DEL ALMACÉN
# =====================
almacen = [
    {"nombre": "arroz", "precio": 50, "stock": 100},
    {"nombre": "pollo", "precio": 95, "stock": 98},
    {"nombre": "huevo", "precio": 210, "stock": 1003},
    {"nombre": "leche", "precio": 75, "stock": 50},
    {"nombre": "pan", "precio": 95, "stock": 0},
    {"nombre": "aceite", "precio": 75, "stock": 0},
    {"nombre": "lechuga", "precio": 95, "stock": 0}
]

# Productos con datos incompletos para prueba de manejo de errores
productos_incompletos = [
    {"nombre": "café", "precio": 120, "stock": 10},
    {"nombre": "té", "stock": 5},
    {"nombre": "azúcar", "precio": 80},
    {"nombre": "sal", "precio": 30, "stock": 0}
]

# =====================
# FUNCIONES
# =====================

class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.__precio = precio
        self.__stock = stock

    def descripcion(self):
        return f"{self.nombre} - precio: {self.__precio} disponibilidad: {self.ver_stock()}"
    
    def ver_stock(self):
        if self.__stock > 0:
             return "disponible"
        else:
             return "no disponible"

    def calcular_precio_final(self, cantidad, impuestos=0.12):
        return (self.__precio * cantidad) + (self.__precio * cantidad * impuestos)

    def get_precio(self):
        return self.__precio
    
    def set_precio(self, nuevo_precio):
        if nuevo_precio > 0:
            self.__precio = nuevo_precio
        else:
            print("El precio debe ser mayor a cero")

    def get_stock(self):
        return self.__stock
    
    def set_stock(self, nuevo_stock):
        if nuevo_stock >= 0:
            self.__stock = nuevo_stock
        else:
             print("El stock no puede ser negativo")


class ProductoPerecible(Producto):
    def __init__(self, nombre, precio, stock, dias_vencimiento):
        super().__init__(nombre, precio, stock)
        self.dias_vencimiento = dias_vencimiento
    
    def descripcion(self):
        return f"{self.nombre} - precio: {self.get_precio()} disponibilidad: {self.ver_stock()} {self.verificar_vencimiento()}"
    

    def verificar_vencimiento(self):
        if self.dias_vencimiento > 0:
            return f"Vence en {self.dias_vencimiento} dias"
        else:
            return "Producto vencido"  
        


# Filtra productos cuyo precio esté por debajo del máximo indicado
def filtrar_por_precio(inventario, precio_maximo):
    return [producto for producto in inventario if producto["precio"] < precio_maximo]

# Calcula el precio final de un producto según cantidad e impuestos
def calcular_precio_final(stock, precio, cantidad, impuestos=0.12):
    if stock > 0:
        return (precio * cantidad) + (precio * cantidad * impuestos)
    else:
        return "No hay inventario de este producto"

# Retorna el precio de un producto con impuesto incluido, maneja datos faltantes
def obtener_precio(producto):
    try:
        precio = producto["precio"]
        return precio * 1.12
    except KeyError:
        return "Este producto no tiene precio registrado"

# Genera un reporte de un producto manejando campos faltantes
def reporte_producto(producto):
    try:
        precio = producto["precio"]
    except KeyError:
        precio = "precio no registrado"

    try:
        stock = producto["stock"]
    except KeyError:
        stock = "stock no registrado"

    return f"{producto['nombre']} — precio: ${precio}, stock: {stock}"

# Verifica si un producto tiene stock disponible
def ver_stock(producto):
    if producto["stock"] > 0:
        return "disponible"
    else:
        return "no disponible"
# PROCESAMIENTO
# =====================

# Actualizar precio del arroz
for producto in almacen:
    if producto["nombre"] == "arroz":
        producto["precio"] = 60

# Filtrar productos fuera del rango de precio
almacen = filtrar_por_precio(almacen, 100)

# =====================
# REPORTE FINAL
# =====================

# Disponibilidad de productos en el almacén
print("=== DISPONIBILIDAD DE PRODUCTOS ===")
for producto in almacen:
    resultado = ver_stock(producto)
    print(f"{producto['nombre']}: {resultado}")

# Precio final por producto según stock e impuestos
print("\n=== PRECIO FINAL POR PRODUCTO ===")
for producto in almacen:
    resultado = calcular_precio_final(producto["stock"], producto["precio"], 1)
    print(f"{producto['nombre']}: {resultado}")

# Reporte de productos con posibles datos incompletos
print("\n=== REPORTE DE PRODUCTOS INCOMPLETOS ===")
for producto in productos_incompletos:
    print(reporte_producto(producto))



# Prueba de objetos con clase Producto
print("=== REPORTE CON CLASE PRODUCTO ===")
leche = Producto("Leche", 100, 8)
pan = Producto("Pan", 10, 5)
huevo = Producto("Huevo", 100, 0)

print(leche.ver_stock(), leche.calcular_precio_final(1))
print(pan.ver_stock(), pan.calcular_precio_final(1))
print(huevo.ver_stock(), huevo.calcular_precio_final(1))

# Prueba de objetos de herencia con la clase hija ProductoPerecible
cafe = ProductoPerecible("Cafe",23, 4, 5)
queso = ProductoPerecible("Queso",23, 4, 0)

print(cafe.ver_stock(), cafe.calcular_precio_final(1), cafe.verificar_vencimiento())
print(queso.ver_stock(), queso.calcular_precio_final(2), queso.verificar_vencimiento())


# Prueba de encapsulamiento con getters y setters
print("\n=== PRUEBA DE ENCAPSULAMIENTO ===")
pan = Producto("pan", 20, 5)
pan.set_precio(0)
pan.set_stock(-1)
print(pan.get_precio(), pan.get_stock())


productos = [
    Producto("arroz", 50, 100),
    ProductoPerecible("leche", 75, 50, 10),
    Producto("pan", 95, 0),
    ProductoPerecible("queso", 120, 20, 3)
]

for producto in productos:
    print(producto.descripcion())