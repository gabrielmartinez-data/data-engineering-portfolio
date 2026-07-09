# ✅ Accede al saldo real y lo actualiza
def depositar(cliente, monto):
    cliente["saldo"] += monto
    return cliente["saldo"]


# ✅ Compara el monto contra el saldo real
def retirar(cliente, monto):
    if cliente["saldo"] >= monto:
        cliente["saldo"] -= monto
        return cliente["saldo"]
    else:
        return "Saldo insuficiente"

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
    aumentar_saldo = cliente["saldo"]
    resultado = depositar(cliente,3444)
    print(f"Nombre: {nombre_cliente} nuevo saldo: {resultado}")

print(f"---Prueba de reduccion de saldo---")
for cliente in cuentas_clientes:
    nombre_cliente = cliente["nombre"]
    aumentar_saldo = cliente["saldo"]
    resultado = retirar(cliente,34343)
    print(f"Nombre: {nombre_cliente} nuevo saldo: {resultado}")