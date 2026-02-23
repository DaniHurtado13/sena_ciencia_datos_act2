import streamlit as st
import pandas as pd

st.title("Método 2: Desde una Lista de Listas")

st.markdown("""
### Ejercicio
En este ejercicio debes crear un DataFrame partiendo de una **lista de listas** que represente el inventario de una tienda de tecnología.

1. Crea una lista de listas donde cada sub-lista contenga información de un producto: 
   `[Nombre del producto, Categoría, Precio, Cantidad en stock]`
   Agrega al menos 4 productos diferentes.
2. Crea un DataFrame llamado `df_inventario` a partir de esta lista y pásale el parámetro `columns=[]` definiendo cómo se llamarán tus columnas.
3. Muestra el DataFrame en la aplicación usando `st.dataframe()`.
""")

st.subheader("Tu resultado:")
# ESTUDIANTE: Escribe tu código a continuación

inv = [
    ['MacBook Pro 14', 'Hardware', 1999.99, 10],
    ['Monitor Samsung Odyssey', 'Hardware', 450.00, 15],
    ['Teclado Logitech MX Keys', 'Periféricos', 109.00, 25],
    ['Licencia Adobe Creative Cloud', 'Software', 52.99, 100],
    ['Disco Duro Externo 2TB', 'Almacenamiento', 85.00, 40]
]

df_inventario = pd.DataFrame(inv, columns=["Nombre", "Categoria", "Precio", "Stock"])
st.dataframe(df_inventario)

# st.dataframe(...)
