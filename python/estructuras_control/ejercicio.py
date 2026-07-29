# ==========================================
# PROCESAMIENTO Y LIMPIEZA DE DATOS CON PYTHON
# Proyecto: Gestión Dinámica de Nómina de Salarios
# ==========================================

# 1. Definición de la lista inicial de salarios (USD)
salarios = [1200, 850, 3100, 950]
print(f"1. Lista Inicial: {salarios}")

# 2. Unir datos de otra sucursal (.extend)
# A diferencia de append(), extend() añade múltiples elementos uno a uno
sucursal_norte = [1500, 2200]
salarios.extend(sucursal_norte)
print(f"2. Después de extend() [Sucursal Norte]: {salarios}")

# 3. Insertar un dato en un índice específico (.insert)
# Agregamos el salario del Gerente ($4500) en el índice 0 (inicio)
salarios.insert(0, 4500)
print(f"3. Después de insert() [Gerente en pos 0]: {salarios}")

# 4. Eliminar un elemento por su VALOR (.remove)
# Un empleado renunció; eliminamos la primera aparición del salario $850
salarios.remove(850)
print(f"4. Después de remove(850): {salarios}")

# 5. Extraer y eliminar un elemento por su ÍNDICE (.pop)
# Eliminamos y capturamos el último registro ingresado por error
salario_eliminado = salarios.pop()
print(f"5. Después de pop() [Se extrajo {salario_eliminado}]: {salarios}")

# 6. Ordenar la lista in-place (.sort)
salarios.sort()
print(f"6. Lista ordenada de menor a mayor con sort(): {salarios}")

# 7. Cálculo de métricas agregadas con funciones nativas
salario_min = min(salarios)
salario_max = max(salarios)
total_nomina = sum(salarios)
total_empleados = len(salarios)
promedio_salarios = total_nomina / total_empleados

# 8. Reporte Final
print("\n" + "="*40)
print("       MÉTRICAS DE LA NÓMINA FINAL      ")
print("="*40)
print(f" - Salario Mínimo  : ${salario_min:.2f}")
print(f" - Salario Máximo  : ${salario_max:.2f}")
print(f" - Nómina Total    : ${total_nomina:.2f}")
print(f" - Cantidad Staff  : {total_empleados}")
print(f" - Salario Promedio: ${promedio_salarios:.2f}")
print("="*40)