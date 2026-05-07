kimport streamlit as st
import requests
import pandas as pd

API_URL = "http://fastapi:8000"

st.title("Catálogo de Libros 📚")


@st.cache_data
def load_books():
    response = requests.get(f"{API_URL}/books/")

    if response.status_code == 200:
        return response.json()

    return None


@st.cache_data
def search_books(query):
    response = requests.get(
        f"{API_URL}/books/search",
        params={"q": query}
    )

    if response.status_code == 200:
        return response.json()

    return None


busqueda = st.text_input("Buscar por título o autor")

if st.button("Actualizar catálogo"):
    st.cache_data.clear()
    st.rerun()


if busqueda.strip():
    data = search_books(busqueda.strip())
else:
    data = load_books()


if data is None:
    st.error("Error al obtener libros")

elif len(data) == 0:

    if busqueda.strip():
        st.info("No se encontraron libros.")
    else:
        st.info("No hay libros registrados.")

else:
    df = pd.DataFrame(data)

    columnas = [
        "titulo",
        "autor",
        "genero",
        "disponible"
    ]

    df = df[columnas]

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )
