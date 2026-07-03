class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def ver_stock(self):
        if self.stock > 0:
            return "disponible"
        else:
            return "no disponible"

    def calcular_precio_final(self, cantidad, impuestos=0.12):
        return (self.precio * cantidad) + (self.precio * cantidad * impuestos)

class ProductoPerecible(Producto):
    def __init__(self, nombre, precio, stock, dias_vencimiento):
        super().__init__(nombre, precio, stock)
        self.dias_vencimiento = dias_vencimiento
    def verificar_vencimiento(self):
         if self.dias_vencimiento > 0:
          return f"Vence en {self.dias_vencimiento} dias"
         else:
               return "Producto vencido"            




cafe = ProductoPerecible("Cafe",23, 4, 5)
queso = ProductoPerecible("Queso",23, 4, 0)

print(cafe.ver_stock(), cafe.calcular_precio_final(1), cafe.verificar_vencimiento())
print(queso.ver_stock(), queso.calcular_precio_final(2), queso.verificar_vencimiento())
