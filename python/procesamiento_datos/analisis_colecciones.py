# ==============================================================================
# ARCHIVO: python/procesamiento_datos/analisis_colecciones.py
# DESCRIPCIÓN: Extracción de métricas, filtrado avanzado y agrupación de datos
# ==============================================================================

# Fuente de datos simulada (Lista de diccionarios / Estructura tipo JSON)
transacciones = [
    {"id": "TX101", "cliente": "Ana", "monto": 150.0, "categoria": "tecnologia", "estado": "completado"},
    {"id": "TX102", "cliente": "Gabriel", "monto": 45.5, "categoria": "hogar", "estado": "pendiente"},
    {"id": "TX103", "cliente": "Luis", "monto": 220.0, "categoria": "tecnologia", "estado": "completado"},
    {"id": "TX104", "cliente": "Pepe", "monto": 80.0, "categoria": "tecnologia", "estado": "cancelado"},
    {"id": "TX105", "cliente": "Maria", "monto": 310.0, "categoria": "hogar", "estado": "completado"}
]

# ------------------------------------------------------------------------------
# TAREA 1: Filtrado y Agregación con List Comprehension + sum()
# ------------------------------------------------------------------------------
# Extrae solo los montos que cumplen dos condiciones: categoría 'tecnologia' Y estado 'completado'
lista_montos = [i["monto"] for i in transacciones if i["categoria"] == "tecnologia" and i["estado"] == "completado"]

# Calculamos la suma total de los montos extraídos
total = sum(lista_montos)

# ------------------------------------------------------------------------------
# TAREA 2: Filtrado de Clientes VIP (List Comprehension)
# ------------------------------------------------------------------------------
# Obtiene los nombres de los clientes con transacciones 'completado' Y monto superior a 200.0
clientes_vip = [i["cliente"] for i in transacciones if i["estado"] == "completado" and i["monto"] > 200.0]

# ------------------------------------------------------------------------------
# TAREA 3: Reporte General de Resultados
# ------------------------------------------------------------------------------
print(f"Total de ventas en tecnologia completada: ${total}")
print(f"Clientes VIP identificados: {clientes_vip}")

# ------------------------------------------------------------------------------
# TAREA 4: Agrupación y Acumulación por Categoría
# ------------------------------------------------------------------------------
total_categoria = {}

# Opción A: Lógica tradicional mediante evaluación explícita (if/else)
for i in transacciones:
    if i["estado"] == "completado":
        # Verificamos si la categoría aún no existe como clave en el diccionario
        if i["categoria"] not in total_categoria:
            total_categoria[i["categoria"]] = i["monto"]
        else:
            # Si ya existe, acumulamos el monto sobre el valor previo
            total_categoria[i["categoria"]] += i["monto"]

# ------------------------------------------------------------------------------
# OPCIÓN B (MÉTODO PRO CON .get()):
# El método .get(clave, valor_por_defecto) busca la clave en el diccionario.
# Si no la encuentra, retorna 0 en lugar de lanzar un KeyError, permitiendo
# realizar la suma directa en una sola línea de código sin usar if/else.
# ------------------------------------------------------------------------------
# for i in transacciones:
#     if i["estado"] == "completado":
#         cat = i["categoria"]
#         total_categoria[cat] = total_categoria.get(cat, 0) + i["monto"]

print(f"Ventas totales por categoría (completadas): {total_categoria}")

