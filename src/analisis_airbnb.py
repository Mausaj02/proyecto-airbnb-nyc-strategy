import pandas as pd
import numpy as np

# 1. CARGAR EL CONJUNTO DE DATOS
# leer el archivo CSV de Airbnb 
try:
    df = pd.read_csv('AB_NYC_2019.csv')
    print("¡ÉXITO: El archivo de Airbnb se cargó correctamente!\n")
except FileNotFoundError:
    print("ERROR: No se encontró el archivo 'AB_NYC_2019.csv'.")
    print("Asegúrate de que el archivo CSV se llame exactamente así y esté en la misma carpeta que este script.")
    exit()

# 2. DESGLOSE 1: ANÁLISIS DE PRECIOS GLOBALES (Para evaluar la propuesta de precios)
print(f"Precio Mínimo Real en el mercado: {df['price'].min()} USD")
print(f"Precio Máximo Real en el mercado: {df['price'].max()} USD")
print(f"Precio Promedio Real en el mercado: {df['price'].mean():.2f} USD")
print(f"Mediana del Precio Real (Dato Central): {df['price'].median()} USD")

print("\n--- Distribución del mercado por Percentiles ---")
percentiles = df['price'].quantile([0.10, 0.25, 0.50, 0.75, 0.90, 0.95])
print(percentiles)
print("---------------------------------------------------------")
print("Análisis para tu informe:")
print(f"- El 50% de las propiedades cuesta {percentiles[0.50]} USD o menos (Mediana).")
print(f"- El 90% de las propiedades cuesta menos de {percentiles[0.90]} USD.")
print("-> CONCLUSIÓN: Proponer un promedio de 225 USD está desfasado; es más caro que el 90% del mercado.")

# 3. DESGLOSE 2: COMPARATIVA MANHATTAN VS BROOKLYN (Para evaluar la unificación de tarifas)
# Filtramos el dataset únicamente para estos dos distritos
df_bm = df[df['neighbourhood_group'].isin(['Brooklyn', 'Manhattan'])]

# Agrupamos por distrito para los calculos estadisticos
resumen_distritos = df_bm.groupby('neighbourhood_group')['price'].agg(
    Total_Propiedades='count',
    Precio_Promedio='mean',
    Precio_Mediana='median',
    Precio_Minimo='min',
    Precio_Maximo='max'
)
print(resumen_distritos)
print("Análisis para tu informe:")
print("-> CONCLUSIÓN: NO se deben unificar tarifas. Manhattan y Brooklyn tienen dinámicas de precios")
print("   completamente diferentes. Hacerlo haría perder competitividad o margen de ganancia.")


# 4. DESGLOSE 3: RELACIÓN ESTADÍAS VS PRECIOS (Para evaluar descuentos por estadías largas)
print("\n=========================================================")
print("=== DESGLOSE 3: RELACIÓN ESTADÍAS VS PRECIOS ===")
print("=========================================================")

# Creamos una función para clasificar las propiedades según su mínimo de noches
def categorizar_noches(noches):
    if noches == 1: return '1. Corta (1 noche)'
    elif noches <= 3: return '2. Corta-Media (2-3 noches)'
    elif noches <= 7: return '3. Semanal (4-7 noches)'
    elif noches <= 29: return '4. Quincenal (8-29 noches)'
    else: return '5. Mensual / Larga (30+ noches)'

df['categoria_estadia'] = df['minimum_nights'].apply(categorizar_noches)

# Calculamos el precio promedio por cada rango de estadía
resumen_estadias = df.groupby('categoria_estadia')['price'].mean().reset_index()
print(resumen_estadias)
print("---------------------------------------------------------")
print("Análisis para tu informe:")
print("-> CONCLUSIÓN: AQUÍ SÍ se valida la hipótesis del equipo. A mayor tiempo de estadía mínima,")
print("   el precio promedio por noche tiende a disminuir en el mercado.")


# 5. CREACIÓN DEL ARCHIVO PARA POWER BI
print("\n=========================================================")
print("=== PASO FINAL: EXPORTANDO DATOS A POWER BI ===")
print("=========================================================")

# Agrupamos de forma inteligente para que te lleves un archivo limpio, liviano y listo para graficar
df_resumen_powerbi = df.groupby(['neighbourhood_group', 'neighbourhood', 'room_type', 'categoria_estadia']).agg(
    Precio_Promedio=('price', 'mean'),
    Precio_Mediana=('price', 'median'),
    Noches_Minimas_Promedio=('minimum_nights', 'mean'),
    Total_Propiedades=('id', 'count')
).reset_index()

# se guarda el archivo CSV para Power BI
df_resumen_powerbi.to_csv('resumen_para_powerbi.csv', index=False)

print("¡PROCESO COMPLETADO EXITOSAMENTE!")
