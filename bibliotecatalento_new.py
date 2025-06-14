
# importamos las librerías que necesitamos

# Tratamiento de datos
# -----------------------------------------------------------------------
import pandas as pd
import numpy as np

# Visualización
# ------------------------------------------------------------------------------
import matplotlib.pyplot as plt
import seaborn as sns

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

def eliminar_columnas (df, columnas):
    for col in columnas:
        if col in df.columns:
            df.drop(col, axis=1, inplace=True)
        # Por si no existe ya esa columna
        else:
            print(f" La columna '{col}' no existe.")
    return df

def revisar_nulos(df):
    print("Valores nulos por columna:")
    nulos = df.isnull().sum()
    print(nulos[nulos > 0])
    print("Porcentaje de nulos por columna:")
    porcentaje_nulos = (nulos[nulos > 0] / df.shape[0]) * 100
    print(porcentaje_nulos.round(2).astype(str) + '%')
    print("Número de filas duplicadas:")
    print(df.duplicated().sum())

def nulos_objeto(df):
  # Columnas con tipo object tienen al menos un nulo
  print("Las columnas objeto con nulos")
  columnas_obj = [col for col in df.select_dtypes(include=['object','category']).columns if df[col].isna().sum() > 0]
  print(columnas_obj)
  # Proporción de valores entre cada categoría de las variables categóricas
  for col in columnas_obj:
    print(f"Distribución de '{col}':")
    display(df[col].value_counts() / df.shape[0]) # display es una función utilizada para mostrar objetos de manera más legible en Jupyter Notebooks o entornos similares.
def nulos_numericos(df):
  # Columnas con tipo object tienen al menos un nulo
  print("Las columnas numéricas con nulos")
  columnas_num = [col for col in df.select_dtypes(include=['float64', 'int64','Int64']).columns if df[col].isna().sum() > 0]
  print(columnas_num)
  print('La distribución de las categorías para cada una de ellas')
  for col in list(columnas_num):
    plt.figure(figsize=(8, 5))
    plt.hist(df[col].dropna(), bins=30, color='skyblue', edgecolor='black')
    plt.title(f'Histograma de {col}')
    plt.xlabel(col)
    plt.ylabel('Frecuencia')
    plt.show()
def nulos_bool(df):
  # Columnas con tipo bool tienen al menos un nulo
  print("Las columnas booleanas con nulos")
  columnas_bool = [col for col in df.select_dtypes(include=['bool']).columns if df[col].isna().sum() > 0]
  print(columnas_bool)
  # Proporción de valores entre cada categoría de las variables bool
  for col in columnas_bool:
    print(f"Distribución de '{col}':")
    display(df[col].value_counts() / df.shape[0]) # display es una función utilizada para mostrar bool de manera más legible en Jupyter Notebooks o entornos similares.
    print("----------------------------")   

def imputar_nulos_objetos(df, columnas, metodo='moda', nueva_categoria='Unknown'):
    # Cubro los errores que puedan generarse si no extisten o no son del tipo adecuado
    for col in columnas:
        if col not in df.columns:
            print(f"La columna '{col}' no existe en el DataFrame.")
            continue
        if df[col].dtype !='category' and df[col].dtype !='object':
            print(f"'{col}' no es de tipo object. Se omite.")
            continue
        # Según el método de imputqación que haya decidido y cubro los errores que se peudan generar
        if metodo == 'moda':
            try:
                moda_col = df[col].mode(dropna=True)[0]
                df[col] = df[col].fillna(moda_col)
                print(f"'{col}': imputada con la moda → '{moda_col}'")
            except IndexError:
                print(f"'{col}': no se pudo calcular la moda (columna vacía).")
        elif metodo == 'nueva_categoria':
            df[col] = df[col].fillna(nueva_categoria)
            print(f"'{col}': imputada con nueva categoría → '{nueva_categoria}'")
        else:
            print(f"Método no reconocido: '{metodo}' (usa 'moda' o 'nueva_categoria')")
    return df
def imputar_nulos_numericos(df, columnas, metodo='mediana'):
    # Cubro los errores que puedan generarse si no extisten o no son del tipo adecuado
    for col in columnas:
        if col not in df.columns:
            print(f" La columna '{col}' no existe en el DataFrame.")
            continue
        if not pd.api.types.is_numeric_dtype(df[col]):
            print(f"'{col}' no es numérica. Se omite.")
            continue
        # Según el método de imputación que haya decidido y cubro los errores que se puedan generar
        if metodo == 'media':
            media_col =  round(df[col].mean(), 1)
            df[col] = df[col].fillna(media_col)
            print(f"'{col}': imputada con la media → {media_col}")
        elif metodo == 'mediana':
            mediana_col = round(df[col].median(), 1)
            df[col] = df[col].fillna(mediana_col)
            print(f"'{col}': imputada con la mediana → {mediana_col}")
        else:
            print(f"'{metodo}' (usa 'media' o 'mediana')")
    return df

def imputar_nulos_objetos_nueva_categoria(df, columnas, metodo='moda', nueva_categoria='Unknown'):
    for col in columnas:
        if col not in df.columns:
            print(f"La columna '{col}' no existe en el DataFrame.")
            continue
        if df[col].dtype != 'category' and df[col].dtype != 'object':
            print(f"'{col}' no es de tipo object ni category. Se omite.")
            continue

        if metodo == 'moda':
            try:
                moda_col = df[col].mode(dropna=True)[0]
                df[col] = df[col].fillna(moda_col)
                print(f"'{col}': imputada con la moda → '{moda_col}'")
            except IndexError:
                print(f"'{col}': no se pudo calcular la moda (columna vacía).")

        elif metodo == 'nueva_categoria':
            # Si es tipo category, asegurarse de que la nueva categoría exista
            if pd.api.types.is_categorical_dtype(df[col]):
                if nueva_categoria not in df[col].cat.categories:
                    df[col] = df[col].cat.add_categories(nueva_categoria)
            df[col] = df[col].fillna(nueva_categoria)
            print(f"'{col}': imputada con nueva categoría → '{nueva_categoria}'")
        else:
            print(f"Método no reconocido: '{metodo}' (usa 'moda' o 'nueva_categoria')")

    return df

from sqlalchemy import create_engine  # sqlalchemy es una librería que permite conectarse y trabajar con bases de datos de manera más abstracta y flexible. 'create_engine' permite crear una conexión a bases de datos SQL de diferentes tipos, como MySQL, PostgreSQL, SQLite, etc.
import pymysql

def create_db(database= 'database', host= 'host', user='user', password= 'password'):
    # Conectar a MySQL usando pymysql
    connection = pymysql.connect(
        host= host,
        user=user,
        password= password
    )
    # Crear un cursor
    cursor = connection.cursor()
    # Crear una base de datos si no existe
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database}")
    print("Base de Datos creada exitosamente.")
    # Cerrar la conexión
    connection.close()
def load_data(table_name, data, user, password, host, database):
    print(f"Cargando datos en la tabla {table_name}...")
    # Crear conexión a MySQL usando SQLAlchemy
    engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database}')
    # Insertar datos desde el DataFrame en MySQL
    data.to_sql(table_name, con=engine, if_exists='append', index=False)
    print(f"Datos insertados en la tabla {table_name} exitosamente.")