import pandas as pd
import numpy as np


# FUNCIÓN 1: Resumen rápido sobre la calidad de los datos de un DF. El resultado es otro DF llamado resumen donde 
#            muestra los tipos de datos, los nulos totales, porcentaje de nulos y los valores únicos del DF que 
#            introduzcamos en la función.

def calidad_datos(df):
    resumen = pd.DataFrame({
        'dtype': df.dtypes,
        'nulos': df.isnull().sum(),
        'pct_nulos': (df.isnull().sum() / len(df) * 100).round(2),
        'unicos': df.nunique()
    })
    return resumen



# FUNCIÓN 2: Busca los valores que empiecen por determinado string para cambiarlo por otro más corto.

def shorten_education(value):
    if pd.isna(value):
        return np.nan
    if value.startswith("Primary"):
        return "Primary"
    if value.startswith("Secondary"):
        return "Secondary"
    if value.startswith("Some college"):
        return "University without title"
    if value.startswith("Associate"):
        return "Associate"
    if value.startswith("Bachelor"):
        return "Bachelor"
    if value.startswith("Master"):
        return "Master"
    if value.startswith("Professional"):
        return "Professional"
    return "Other"



# FUNCIÓN 3: Busca los valores que empiecen por cierto string para modificarlo por un numero concreto.
#            Pasar la tabla a formato largo y abreviar etiquetas para que los graficos sean legibles
#            Se usa una funcion para evitar problemas con apostrofes o caracteres especiales.

def score_ed_level(value):
    if pd.isna(value):
        return np.nan
    if value.startswith("Primary"):
        return 1
    if value.startswith("Secondary"):
        return 2
    if value.startswith("Some college"):
        return 3
    if value.startswith("Associate"):
        return 4
    if value.startswith("Bachelor"):
        return 5
    if value.startswith("Master"):
        return 6
    if value.startswith("Professional"):
        return 7
    return np.nan