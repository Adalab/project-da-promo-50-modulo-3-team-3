# función para el análisis de valores únicos

def valores_unicos(df, nombre= 'DataFrame'):
    print(f'Buscando valores únicos en {nombre}')
    for col in df.columns:
        num_unicos = df[col].nunique()
        print(f"{col}: {num_unicos} valores únicos")
        tipo = df[col].dtype
        print(f"{col}: {tipo}")
        print('Estos valores unicos son')
        print(df[col].unique())
        print("----------------------------")


def conteo_valores(df, nombre= 'DataFrame'):
    print(f'Contando valores únicos en {nombre}')
    for col in df.columns:
        num_unicos = df[col].nunique()
        print(f"{col}: {num_unicos} valores únicos")
        print('Estos valores unicos son')
        print(df[col].value_counts())
        print("----------------------------")


def revisar_nulos(df):
    print("Valores nulos por columna:")
    nulos = df.isnull().sum()
    print(nulos[nulos > 0])
    print("Porcentaje de nulos por columna:")
    porcentaje_nulos = (nulos[nulos > 0] / df.shape[0]) * 100
    print(porcentaje_nulos.round(2).astype(str) + '%')
    print("Número de filas duplicadas:")
    print(df.duplicated().sum())


def transformacion_datos(df, columna, tipo, nombre= 'DataFrame'):
    # Ver tipos actuales
    print(f'Los tipos de datos en {nombre} son')
    print(df.dtypes)
    # Cambio el tipo de dato
    print(f"Transformando columna '{columna}' a tipo {tipo}")
    df[columna] = df[columna].astype(tipo)
    print(df.dtypes)
    # Retornar el  df para más adelante
    return df