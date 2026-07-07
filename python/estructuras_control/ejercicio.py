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

    def ver_stock(self):
        if self.__stock > 0:
            return "disponible"
        else:
            return "no disponible"

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
        

        
productos = [
    Producto("arroz", 50, 100),
    ProductoPerecible("leche", 75, 50, 10),
    Producto("pan", 95, 0),
    ProductoPerecible("queso", 120, 20, 3)
]

for producto in productos:
    print(producto.descripcion())