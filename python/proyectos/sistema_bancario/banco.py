# ✅ Accede al saldo real y lo actualiza


class cuenta:
    def __init__(self, nombre, cuenta, tipo, saldo):
        self.nombre = nombre
        self.cuenta = cuenta
        self.tipo = tipo
        self.__saldo = saldo

    def get_saldo(self):
            return self.__saldo

    def depositar(cliente, monto):
        try:
            if monto <= 0:
                raise ValueError("el monto debe ser mayor a 0")
        
        except ValueError as e:
            return str(e)
        
        cliente["saldo"] += monto
        return cliente["saldo"]




    # ✅ Compara el monto contra el saldo real
    def retirar(cliente, monto):
        try:
            if monto <= 0:
                raise ValueError("el monto debe ser mayor a 0")
            if monto > cliente["saldo"]:
                raise ValueError("Saldo insuficiente")
        except ValueError as e:
            return str(e)
        
        cliente["saldo"] -= monto
        return cliente["saldo"]
    

    def descripcion(self):
        return f"Cliente: {self.nombre} - Cuenta: {self.cuenta} - Tipo: {self.tipo} - Saldo: {self.get_saldo()}"
cuentas = cuenta("Gabriel", 222, "corriente", 300340)






cuentass = [
    {"Gabriel", 222, "corriente", 300340},   
    {"pepe", 221, "ahorro", 8000000},
    {"lucas", 223, "ahorro", 2354545}   
]

