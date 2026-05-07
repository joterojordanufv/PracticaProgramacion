import streamlit as st
import requests
import pandas as pd
from ui import apply_global_styles, hero, section_title

API_URL = "http://fastapi:8000"

st.set_page_config(page_title="Catálogo", page_icon="📚", layout="wide")
apply_global_styles()

hero("📚 Catálogo de Libros", "Consulta el inventario completo, busca libros y revisa su disponibilidad.")

@st.cache_data
def load_books():
    response = requests.get(f"{API_URL}/books/")
    if response.status_code == 200:
        return response.json()
    return None


@st.cache_data
def search_books(query):
    response = requests.get(f"{API_URL}/books/search", params={"q": query})
    if response.status_code == 200:
        return response.json()
    return None


col_search, col_button = st.columns([4, 1])

with col_search:
    busqueda = st.text_input("Buscar por título o autor", placeholder="Ej: Orwell, 1984, Tolkien...")

with col_button:
    st.write("")
    st.write("")
    if st.button("Actualizar"):
        st.cache_data.clear()
        st.rerun()

if busqueda.strip():
    data = search_books(busqueda.strip())
else:
    data = load_books()

if data is None:
    st.error("Error al obtener libros.")
elif len(data) == 0:
    st.info("No se encontraron libros.")
else:
    df = pd.DataFrame(data)

    total = len(df)
    disponibles = len(df[df["disponible"] == True])
    prestados = total - disponibles

    m1, m2, m3 = st.columns(3)
    m1.metric("Libros encontrados", total)
    m2.metric("Disponibles", disponibles)
    m3.metric("Prestados", prestados)

    section_title("Listado de libros")

    df = df[["titulo", "autor", "genero", "disponible"]]
    df["disponible"] = df["disponible"].apply(
        lambda x: "🟢 Disponible" if x else "🔴 Prestado"
    )
    df = df.rename(columns={
        "titulo": "Título",
        "autor": "Autor",
        "genero": "Género",
        "disponible": "Estado"
    })

    st.dataframe(df, use_container_width=True, hide_index=True)
