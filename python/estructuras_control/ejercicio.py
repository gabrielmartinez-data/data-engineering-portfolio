class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.__precio = precio
        self.__stock = stock

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
        

pan = Producto("pan", 20, 5)
pan.set_precio(0)
pan.set_stock(-1)

print(pan.get_precio(), pan.get_stock())