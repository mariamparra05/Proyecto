import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Ajuste la estética general de las gráficas para que todas tengan tonalidades armoniosas.
sns.set_theme(style="whitegrid", palette="muted")

# Filtra los datos por el municipio seleccionado, permitiendo centrarse en el área específica.
def filtrar_por_municipio(df, municipio):
    return df[df["Municipio"] == municipio]

# 1. Gráfica de barras: Tipos de establecimientos, Aquí muestro cuántos restaurantes hay de cada tipo (por ejemplo, cafeterías, fast food).
def graficar_tipo_restaurantes(df, municipio):
    df_municipio = filtrar_por_municipio(df, municipio)
    tipo_restaurantes = df_municipio["Tipo de Establecimiento"].value_counts()
    plt.figure(figsize=(8, 6))
    sns.barplot(x=tipo_restaurantes.values, y=tipo_restaurantes.index, palette="copper")
    plt.title(f"Tipos de Establecimientos en {municipio}", fontsize=14, color="black")
    plt.xlabel("Cantidad", fontsize=12)
    plt.ylabel("Tipo de Establecimiento", fontsize=12)
    plt.show()

# 2. Gráfica circular: Moda de categorías. Aquí muestro la categoría más frecuente y la comparo con el resto.
def graficar_moda_general(df, municipio):
    df_municipio = filtrar_por_municipio(df, municipio)
    moda_categoria = df_municipio["Categoría"].mode()[0]
    total_moda = df_municipio[df_municipio["Categoría"] == moda_categoria]["Nombre"].nunique()
    total_restaurantes = df_municipio["Nombre"].nunique()
    otros = total_restaurantes - total_moda
    
    valores = [total_moda, otros]
    etiquetas = [f"Moda: {moda_categoria}", "Otros"]
    colores = ["#F4A460", "#D2B48C"]
    
    plt.figure(figsize=(7, 7))
    plt.pie(valores, labels=etiquetas, autopct="%1.1f%%", startangle=140, colors=colores)
    plt.title(f"Moda de Categorías en {municipio}", fontsize=14, color="black")
    plt.show()

# 3. Gráfica circular: Proporciones generales de categorías.  Aquí visualizo el porcentaje de cada categoría en el municipio.
def graficar_proporciones_generales(df, municipio):
    df_municipio = filtrar_por_municipio(df, municipio)
    categorias = df_municipio["Categoría"].value_counts()
    plt.figure(figsize=(16, 16))
    categorias.plot(kind="pie", autopct="%1.1f%%", startangle=140, colors=sns.color_palette("pastel"))
    plt.title(f"Distribución General de Categorías en {municipio}", fontsize=14, color="black")
    plt.ylabel("")  # Para evitar texto superpuesto
    plt.show()

# 4. Gráfica de dispersión: Relación entre precio y categorías. Aquí muestro cómo se relacionan los precios de los platos con los diferentes tipos de cocina disponibles.
def graficar_precio_vs_categoria(df, municipio):
    df_municipio = filtrar_por_municipio(df, municipio)
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df_municipio, x="Precio", y="Categoría", hue="Categoría", palette="flare", s=100)
    plt.title(f"Relación entre Precio y Categorías en {municipio}", fontsize=14, color="black")
    plt.xlabel("Precio", fontsize=12)
    plt.ylabel("Categoría", fontsize=12)
    plt.legend(title="Categorías", bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.show()
