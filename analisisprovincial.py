import pandas as pd

# Aquí filtro los datos del DataFrame por la provincia que estoy analizando. Esto asegura que solo se trabaje con datos relevantes
def filtrar_por_provincia(df, provincia):
    return df[df['Provincia'] == provincia]

# Calculo cuántos municipios hay en total en la provincia. Esto da una idea del alcance geográfico del análisis
def total_municipios(df, provincia):
    provincia_df = filtrar_por_provincia(df, provincia)
    return provincia_df['Municipio'].nunique()

# Aquí cuento cuántos platos diferentes hay en total en la provincia. Esto muestra la diversidad de opciones disponibles
def total_platos_provincia(df, provincia):
    provincia_df = filtrar_por_provincia(df, provincia)
    return provincia_df['Nombre Plato'].nunique()

# Calculo la moda de los precios en la provincia (si hay empate, elijo el menor). Esto nos da una idea del precio más común en los menús
def moda_precio_provincia(df, provincia):
    provincia_df = filtrar_por_provincia(df, provincia)
    if not provincia_df.empty:
        modas = provincia_df['Precio'].mode()
        return modas.min()  # Elegir el menor en caso de empate
    return "No disponible"

# Identifico la categoría más común en la provincia. Esto muestra las tendencias culinarias más populares
def categoria_mas_comun_provincia(df, provincia):
    provincia_df = filtrar_por_provincia(df, provincia)
    if not provincia_df.empty:
        return provincia_df['Categoría'].mode().iloc[0]
    return "No disponible"

## Identifico el plato más caro en la provincia. Esto muestra cuál es la opcion más costosa disponible
def plato_mas_caro(df, provincia):
    provincia_df = filtrar_por_provincia(df, provincia)
    if not provincia_df.empty:
        plato_caro = provincia_df.loc[provincia_df['Precio'].idxmax()]
        return plato_caro['Nombre Plato'], plato_caro['Precio'], plato_caro['Municipio']
    return "No disponible"

# Aquí miro cuáles son los ingredientes más comunes en la provincia. Esto da una idea de las tendencias de sabor en la región
def ingredientes_mas_comunes_provincia(df, provincia):
    provincia_df = filtrar_por_provincia(df, provincia)
    ingredientes = []
    for lista in provincia_df['Ingredientes Principales']:
        if pd.notna(lista):
            ingredientes.extend(lista.split(', '))
    if ingredientes:
        return max(set(ingredientes), key=ingredientes.count)
    return "No disponible"

# Investigo las alergias más frecuentes en la provincia. Esto es importante para entender las precauciones que deben tomar los establecimientos
def alergias_mas_frecuentes_provincia(df, provincia):
    provincia_df = filtrar_por_provincia(df, provincia)
    alergias = []
    for lista in provincia_df['Alergias']:
        if pd.notna(lista):
            alergias.extend(lista.split(', '))
    if alergias:
        return max(set(alergias), key=alergias.count)
    return "No disponible"

# Comparo la proporción de platos entre municipios. Esto muestra cómo se distribuye la oferta gastronómica en la provincia
def proporcion_platos_por_municipio(df, provincia):
    provincia_df = filtrar_por_provincia(df, provincia)
    total_platos = provincia_df['Nombre Plato'].nunique()
    if total_platos > 0:
        platos_por_municipio = provincia_df.groupby('Municipio')['Nombre Plato'].nunique()
        return (platos_por_municipio / total_platos).to_dict()
    return {}

# Comparo las categorías más frecuentes entre municipios. Esto refiere a las tendencias culinarias específicas de cada área
def categorias_mas_comunes_por_municipio(df, provincia):
    provincia_df = filtrar_por_provincia(df, provincia)
    categorias_por_municipio = {}
    for municipio in provincia_df['Municipio'].unique():
        municipio_df = provincia_df[provincia_df['Municipio'] == municipio]
        if not municipio_df.empty:
            categorias_por_municipio[municipio] = municipio_df['Categoría'].mode().iloc[0]
    return categorias_por_municipio
