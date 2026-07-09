# ✅ Accede al saldo real y lo actualiza
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
    
    

cuentas_clientes = [
    {"nombre": "Gabriel", "cuenta": 222, "saldo": 300340, "tipo": "corriente"},   
    {"nombre": "pepe", "cuenta": 221, "saldo": 33000, "tipo": "ahorro"},
    {"nombre": "lucas", "cuenta": 223, "saldo": 302100, "tipo": "ahorro"}   
  

]

for cliente in cuentas_clientes:
    print(f"Cliente: {cliente["nombre"]} -Cuenta: {cliente["cuenta"]} - Saldo: {cliente["saldo"]} - Tipo: {cliente["tipo"]}")


print(f"---Prueba de aumento de saldo---")
for cliente in cuentas_clientes:
    nombre_cliente = cliente["nombre"]
    resultado = depositar(cliente, 1122110)
    print(f"Nombre: {nombre_cliente} nuevo saldo: {resultado}")

print(f"---Prueba de reduccion de saldo---")
for cliente in cuentas_clientes:
    nombre_cliente = cliente["nombre"]
    resultado = retirar(cliente,1111111110)
    print(f"Nombre: {nombre_cliente} nuevo saldo: {resultado}")