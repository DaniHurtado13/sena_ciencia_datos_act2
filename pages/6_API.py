import streamlit as st
import pandas as pd
import requests

st.title("Conexiones Avanzadas: API REST")

st.markdown("""
### Ejercicio
A veces los datos están "vivos" y debes consultarlos a través de una API en internet.

1. Vamos a usar la PokéAPI para obtener algunos datos de Pokémon de forma sencilla. 
2. Realiza una petición `GET` a la siguiente URL: `https://pokeapi.co/api/v2/pokemon?limit=10`
3. Verifica que la petición fue exitosa (`status_code == 200`).
4. Convierte la respuesta a formato JSON.
5. Extrae la lista que viene dentro de la llave `"results"`.
6. Convierte esa lista extraída en un DataFrame llamado `df_pokemon` y muéstralo con Streamlit mediante `st.dataframe()`.
""")

st.subheader("Tu resultado:")
# ESTUDIANTE: Escribe tu código a continuación
# Recuerda usar la librería requests que ya está importada arriba


url_api = "https://pokeapi.co/api/v2/pokemon?limit=10"
respuesta = requests.get(url_api)

if respuesta.status_code == 200:
    datos_json = respuesta.json()
    lista_pokemon = datos_json.get("results", [])
    df_pokemon = pd.DataFrame(lista_pokemon)
    st.dataframe(df_pokemon)
else:
    st.error(f"La petición falló con código: {respuesta.status_code}")
