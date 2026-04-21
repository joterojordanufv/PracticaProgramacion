import streamlit as st
import requests
import pandas as pd

API_URL = "http://fastapi:8000"

st.title("Catálogo de Libros 📚")

response = requests.get(f"{API_URL}/books/")

if response.status_code == 200:
    data = response.json()

    if len(data) == 0:
        st.info("No hay libros en el catálogo.")
    else:
        df = pd.DataFrame(data)
        st.dataframe(df)
else:
    st.error("Error al obtener los libros")
