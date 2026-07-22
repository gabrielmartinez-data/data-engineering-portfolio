transacciones = [
    {"id": "TX101", "cliente": "Ana", "monto": 150.0, "categoria": "tecnologia", "estado": "completado"},
    {"id": "TX102", "cliente": "Gabriel", "monto": 45.5, "categoria": "hogar", "estado": "pendiente"},
    {"id": "TX103", "cliente": "Luis", "monto": 220.0, "categoria": "tecnologia", "estado": "completado"},
    {"id": "TX104", "cliente": "Pepe", "monto": 80.0, "categoria": "tecnologia", "estado": "cancelado"},
    {"id": "TX105", "cliente": "Maria", "monto": 310.0, "categoria": "hogar", "estado": "completado"}
]

# Tarea 1: Filtrado y Suma (Tu opción con List Comprehension + sum)
lista_montos = [i["monto"] for i in transacciones if i["categoria"] == "tecnologia" and i["estado"] == "completado"]
total = sum(lista_montos)

# Tarea 2: Clientes VIP (completado Y monto > 200.0)
clientes_vip = [i["cliente"] for i in transacciones if i["estado"] == "completado" and i["monto"] > 200.0]

# Tarea 3: Reporte General
print(f"Total de ventas en tecnologia completada: ${total}")
print(f"Clientes VIP identificados: {clientes_vip}")

total_categoria = {}
for i in transacciones:
    if i["estado"] == "completado":
        if i["categoria"] not in total_categoria:
            total_categoria[i["categoria"]] = i["monto"]
        else:
            total_categoria[i["categoria"]] += i["monto"]

print(total_categoria)
   


