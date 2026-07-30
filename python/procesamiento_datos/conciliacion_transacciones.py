# ==============================================================================
# AUDITORÍA FINANCIERA: CONCILIACIÓN DE TRANSACCIONES BANCARIAS
# Conceptos aplicados: Listas, Diccionarios (.keys, .values, .items) y Conjuntos
# ==============================================================================

# 1. Definición de Datos Iniciales
transacciones_banco = ["TX101", "TX102", "TX104", "TX102", "TX105"]
detalle_tx = {
    "TX101": 500.0,
    "TX102": 1200.5,
    "TX103": 300.0,
    "TX104": 1500.0,
    "TX105": 800.0,
}
transacciones_visa = ["TX101", "TX102", "TX104", "TX106"]

# 2. Manejo de Conjuntos (Sets) y Operaciones de Conciliación
set_banco = set(transacciones_banco)
set_visa = set(transacciones_visa)

conciliadas = set_banco & set_visa
no_en_visa = set_banco - set_visa

# 3. Métodos de Diccionarios (.keys, .values)
lista_claves = list(detalle_tx.keys())
montos_total = sum(detalle_tx.values())

# 4. Reporte Final e Iteración con .items()
print("=" * 50)
print("          DETALLE DE TRANSACCIONES AUDITADAS          ")
print("=" * 50)

for id_tx, monto in detalle_tx.items():
    print(f"ID: {id_tx} | Monto: ${monto:,.2f}")

print("\n" + "=" * 50)
print("                 RESUMEN DE CONCILIACIÓN              ")
print("=" * 50)
print(f"Transacciones Conciliadas   : {conciliadas}")
print(f"Faltantes en Visa (Revisar) : {no_en_visa}")
print(f"Monto Total Auditado        : ${montos_total:,.2f}")
print("=" * 50)