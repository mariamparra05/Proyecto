import pandas as pd
# Aquí filtro los datos del DataFrame por el municipio que estoy analizando. Para asegurarme de que todas las funciones trabajen solo con los datos adecuados
def filtrar_por_municipio(df, municipio):
    if 'Municipio' not in df.columns:
        print("Error: La columna 'Municipio' no está en el DataFrame.")
        return pd.DataFrame()
    return df[df['Municipio'] == municipio]

# Calculo cuántos restaurantes hay en total en el municipio. Sirve para conocer la cantidad de negocios que estamos analizando
def total_establecimientos(df, municipio):
    municipio_df = filtrar_por_municipio(df, municipio)
    if 'Nombre' not in municipio_df.columns:
        print("Error: La columna 'Nombre' no está en el DataFrame.")
        return 0
    return municipio_df['Nombre'].nunique()

# Cuento cuántos platos diferentes hay en total en el municipio. Esto ayuda a ver la diversidad de opciones disponibles
def total_platos(df, municipio):
    municipio_df = filtrar_por_municipio(df, municipio)
    if 'Nombre Plato' not in municipio_df.columns:
        print("Error: La columna 'Nombre Plato' no está en el DataFrame.")
        return 0
    return municipio_df['Nombre Plato'].nunique()

# Calculo cuántas categorías diferentes de platos hay. Para mostrar la variedad de tipos de comida disponibles
def total_categorias(df, municipio):
    municipio_df = filtrar_por_municipio(df, municipio)
    if 'Categoría' not in municipio_df.columns:
        print("Error: La columna 'Categoría' no está en el DataFrame.")
        return 0
    return municipio_df['Categoría'].nunique()


# Busco cuál es el plato más pedido o más común en el municipio. Esto da una idea de las preferencias de los clientes
def plato_mas_comun(df, municipio):
    municipio_df = filtrar_por_municipio(df, municipio)
    if 'Nombre Plato' not in municipio_df.columns:
        print("Error: La columna 'Nombre Plato' no está en el DataFrame.")
        return None
    plato = municipio_df['Nombre Plato'].mode()
    return plato.iloc[0] if not plato.empty else None

# Identifico la categoría más popular en el municipio. Para reflejar las tendencias culinarias de la zona
def categoria_mas_comun(df, municipio):
    municipio_df = filtrar_por_municipio(df, municipio)
    if 'Categoría' not in municipio_df.columns:
        print("Error: La columna 'Categoría' no está en el DataFrame.")
        return None
    categoria = municipio_df['Categoría'].mode()
    return categoria.iloc[0] if not categoria.empty else None

# Identifico los ingredientes más comunes en los platos. Para entender las preferencias de los sabores en el municipio
def ingredientes_mas_comunes(df, municipio):
    try:
        municipio_df = filtrar_por_municipio(df, municipio)
        ingredientes = municipio_df['Ingredientes Principales'].str.split(', ', expand=True).stack()
        return ingredientes.mode().iloc[0]
    except (KeyError, IndexError):
        print("No se pudieron identificar los ingredientes más comunes.")
        return None

# Obtengo la moda de los precios de los platos en el municipio. Para tener una idea del precio más común en los menús
def moda_precio(df, municipio):
    try:
        municipio_df = filtrar_por_municipio(df, municipio)
        return municipio_df['Precio'].mode().iloc[0]
    except (KeyError, IndexError):
        print("No se pudo calcular la moda del precio.")
        return None
