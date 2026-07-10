# ✅ Accede al saldo real y lo actualiza


class Cuenta:
    def __init__(self, nombre, cuenta, tipo, saldo):
        self.nombre = nombre
        self.cuenta = cuenta
        self.tipo = tipo
        self.__saldo = saldo

    def get_saldo(self):
            return self.__saldo

    def depositar(self, monto):
        try:
            if monto <= 0:
                raise ValueError("el monto debe ser mayor a 0")
        
        except ValueError as e:
            return str(e)
        
        self.__saldo += monto
        return self.__saldo




    # ✅ Compara el monto contra el saldo real
    def retirar(self, monto):
        try:
            if monto <= 0:
                raise ValueError("el monto debe ser mayor a 0")
            if monto > self.__saldo:
                raise ValueError("Saldo insuficiente")
        except ValueError as e:
            return str(e)
        
        self.__saldo -= monto
        return self.__saldo
    

    def descripcion(self):
        return f"Cliente: {self.nombre} - Cuenta: {self.cuenta} - Tipo: {self.tipo} - Saldo: {self.get_saldo()}"

clientes = [
    Cuenta("Gabriel", 222, "corriente", 300340),
    Cuenta("pepe", 221, "ahorro", 8000000)
]

for cliente in clientes:
    print(cliente.depositar(0))
    print(cliente.descripcion())
    print(cliente.retirar(45))