import streamlit as st
import pandas as pd

st.title("Método 1: Juntando varias Series")

st.markdown("""
### Ejercicio
En este ejercicio debes crear un DataFrame agrupando información sobre **películas favoritas**.

1. Crea tres Series de Pandas diferentes:
    - Una serie llamada `titulos` con al menos 4 nombres de películas.
    - Una serie llamada `directores` con los directores de esas películas.
    - Una serie llamada `años` con el año de estreno.
2. Une estas tres series en un único DataFrame llamado `df_peliculas`, asignando nombres descriptivos a las columnas (por ejemplo: `Título`, `Director`, `Año de Estreno`).
3. Muestra el DataFrame en la aplicación usando `st.dataframe()`.
""")

st.subheader("Tu resultado:")
# ESTUDIANTE: Escribe tu código a continuación

titulos = pd.Series(['Batman the darkest night', 'La isla siniestra', 'Scary movie', 'Kill Bill', 'Pacific rim'])
directores = pd.Series(['Christopher Nolan', 'Martin Scorsese', 'Marlon Wayans', 'Quentin Tarantino', 'Guillermo del Toro'])
anios = pd.Series(['2008', '2010', '2000', '2003', '2013'])

df_peliculas = pd.DataFrame({
    'Peliculas': titulos,
    'Directores': directores,
    "Año": anios
})

st.dataframe(df_peliculas)

# st.dataframe(...)
