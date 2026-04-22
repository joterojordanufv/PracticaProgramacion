import streamlit as st
import requests
import pandas as pd

API_URL = "http://fastapi:8000"

st.title("Catálogo de Libros 📚")

busqueda = st.text_input("Buscar por título o autor")

if busqueda.strip():
    response = requests.get(f"{API_URL}/books/search", params={"q": busqueda})
else:
    response = requests.get(f"{API_URL}/books/")

if response.status_code == 200:
    data = response.json()

    if len(data) == 0:
        if busqueda.strip():
            st.info("No se han encontrado libros con esa búsqueda.")
        else:
            st.info("No hay libros en el catálogo.")
    else:
        df = pd.DataFrame(data)

        columnas = ["titulo", "autor", "genero", "disponible"]
        df = df[columnas]

        st.dataframe(df, use_container_width=True)
else:
    st.error(f"Error al obtener libros: {response.status_code}")
