import streamlit as st
import requests

API_URL = "http://fastapi:8000"

st.title("Registrar Nuevo Libro 📚")

with st.form("form_libro"):
    titulo = st.text_input("Título")
    autor = st.text_input("Autor")
    genero = st.text_input("Género")

    submitted = st.form_submit_button("Guardar libro")

    if submitted:
        payload = {
            "titulo": titulo,
            "autor": autor,
            "genero": genero
        }

        response = requests.post(f"{API_URL}/books/", json=payload)

        if response.status_code == 200:
            st.success("Libro añadido correctamente ✅")
        else:
            st.error(response.json()["detail"])
