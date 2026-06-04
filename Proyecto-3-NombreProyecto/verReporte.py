import pandas as pd

# Leer el archivo CSV
df = pd.read_csv("ventas_tecnologia.csv")

# Mostrar los primeros registros
print(df.head())

# Calcular ingresos
df["ingresos"] = df["cantidad"] * df["precio_unitario"]

print(df)