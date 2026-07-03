import pandas as pd

# 1. La línea mágica: Python lee la pestaña 'Tienda' de tu archivo real de Excel
# Usamos openpyxl como el motor de lectura por debajo
archivo_excel = "Excel/financial-analysis-model.xlsx"
df = pd.read_excel(archivo_excel, sheet_name="Tienda", engine="openpyxl")
# 2. Operación masiva: Calculamos el ITBIS (18%) para CADA fila del archivo real
df['ITBIS_Calculado'] = df['Revenue'] * 0.18

# 3. Calculamos la Ganancia Neta para CADA fila
df['Ganancia_Neta'] = df['Revenue'] - df['ITBIS_Calculado']

# 4. Mostramos las primeras 10 filas en la terminal para auditar que todo esté correcto
print("\n--- ¡DATOS ABSORBIDOS Y PROCESADOS DESDE EXCEL COMPLETO! ---")
print(df[['Location', 'Revenue', 'ITBIS_Calculado', 'Ganancia_Neta']].head(10))

# 5. Opcional: Vamos a ver cuánto es el gran total de Ganancia Neta de la empresa
total_neto = df['Ganancia_Neta'].sum()
print(f"\n El Gran Total de Ganancia Neta es: RD$ {total_neto:,.2f}\n")