# ==============================================================================
# ARCHIVO: python/estructuras_control/sistema_bancario_poo.py
# DESCRIPCIÓN: Práctica avanzada de POO (Herencia, Encapsulamiento y Polimorfismo)
# ==============================================================================

class Cuenta:
    def __init__(self, nombre, cuenta, tipo, saldo):
        self.nombre = nombre
        self.cuenta = cuenta
        self.tipo = tipo
        self.__saldo = saldo  # Atributo privado
    
    def get_saldo(self):
        """Getter para acceder al saldo de forma segura."""
        return self.__saldo

    def depositar(self, monto):
        """Permite depositar dinero validando que el monto sea positivo."""
        try:
            if monto <= 0:
                raise ValueError("el monto debe ser mayor a 0")
        except ValueError as e:
            return str(e)
        
        self.__saldo += monto
        return self.__saldo

    def retirar(self, monto):
        """Permite retirar dinero validando fondos suficientes y montos positivos."""
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
        """Retorna una cadena con la información básica de la cuenta."""
        return f"Cliente: {self.nombre} - Cuenta: {self.cuenta} - Tipo: {self.tipo} - Saldo: {self.get_saldo()}"


class CuentaAhorro(Cuenta):
    def __init__(self, nombre, cuenta, tipo, saldo, tasa_interes=0.05):
        # Invocamos al constructor de la clase padre (Cuenta)
        super().__init__(nombre, cuenta, tipo, saldo)
        self.tasa_interes = tasa_interes

    def aplicar_interes(self):
        """Calcula el interés y lo deposita directamente en el saldo privado."""
        interes_generado = self.get_saldo() * self.tasa_interes
        # Usamos depositar() de la clase padre para actualizar de forma segura el __saldo
        nuevo_saldo = self.depositar(interes_generado)
        return nuevo_saldo
        
    def descripcion(self):
        """Sobrescribe la descripción (Polimorfismo) para añadir la tasa de interés."""
        return f"Cliente: {self.nombre} - Cuenta: {self.cuenta} - Tipo: {self.tipo} - Saldo: {self.get_saldo()} - Interés: {self.tasa_interes}"


# ==============================================================================
# EJECUCIÓN Y PRUEBAS
# ==============================================================================
if __name__ == "__main__":
    clientes = [
        Cuenta("Gabriel", 222, "corriente", 300340),
        CuentaAhorro("pepe", 221, "ahorro", 8000000),
        CuentaAhorro("Raul", 220, "ahorro", 33456000)
    ]

    print("--- PROCESANDO CUENTAS BANCARIAS ---")
    for cliente in clientes:
        print(cliente.descripcion())
        
        # Validación polimórfica: Solo aplicamos interés si el método existe en el objeto
        if hasattr(cliente, 'aplicar_interes'):
            print(f"  -> Saldo después de aplicar interés: {cliente.aplicar_interes()}")
        else:
            print("  -> Esta cuenta no genera intereses.")