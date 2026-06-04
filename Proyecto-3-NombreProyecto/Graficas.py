import os
import pandas as pd
import matplotlib.pyplot as plt


def cargar_datos():
    carpeta = os.path.dirname(__file__)
    archivo = os.path.join(carpeta, "ventas_tecnologia.csv")
    return pd.read_csv(archivo, encoding='latin-1')


def generar_graficos(df):
    df["ingresos"] = df["cantidad"] * df["precio_unitario"]

    ventas_producto = df.groupby("producto")["cantidad"].sum().sort_values(ascending=False)
    ventas_mes = df.groupby("mes")["cantidad"].sum()
    orden_meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    ventas_mes = ventas_mes.reindex([m for m in orden_meses if m in ventas_mes.index])
    ingresos_producto = df.groupby("producto")["ingresos"].sum().sort_values(ascending=False)

    carpeta = os.path.dirname(__file__)

    plt.figure(figsize=(8, 5))
    ventas_producto.plot(kind='bar', color='#4c72b0')
    plt.title('Ventas por producto')
    plt.xlabel('Producto')
    plt.ylabel('Cantidad')
    plt.tight_layout()
    plt.savefig(os.path.join(carpeta, 'ventas_producto.png'))
    plt.close()

    plt.figure(figsize=(8, 5))
    ventas_mes.plot(kind='line', marker='o', color='#4c72b0')
    plt.title('Evolución mensual de ventas')
    plt.xlabel('Mes')
    plt.ylabel('Cantidad')
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.savefig(os.path.join(carpeta, 'ventas_mes.png'))
    plt.close()

    plt.figure(figsize=(6, 6))
    ingresos_producto.plot(kind='pie', autopct='%1.1f%%', startangle=90)
    plt.title('Porcentaje de ventas por producto')
    plt.ylabel('')
    plt.tight_layout()
    plt.savefig(os.path.join(carpeta, 'porcentaje_producto.png'))
    plt.close()

    print('Gráficas generadas:')
    print('- ventas_producto.png')
    print('- ventas_mes.png')
    print('- porcentaje_producto.png')


if __name__ == '__main__':
    df = cargar_datos()
    generar_graficos(df)
