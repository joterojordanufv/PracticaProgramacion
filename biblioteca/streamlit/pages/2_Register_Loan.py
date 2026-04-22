import streamlit as st
import requests

API_URL = "http://fastapi:8000"

st.title("Registrar Préstamo 📖")

books_response = requests.get(f"{API_URL}/books/")
users_response = requests.get(f"{API_URL}/users/")

books = books_response.json() if books_response.status_code == 200 else []
users = users_response.json() if users_response.status_code == 200 else []

libros_disponibles = [b for b in books if b["disponible"]]

if len(users) == 0:
    st.info("No hay usuarios registrados. Debes crear uno antes de hacer un préstamo.")
elif len(libros_disponibles) == 0:
    st.info("No hay libros disponibles para préstamo.")
else:
    with st.form("form_prestamo"):
        user_id = st.selectbox(
            "Usuario",
            options=[u["id"] for u in users],
            format_func=lambda x: next(u["nombre"] for u in users if u["id"] == x)
        )

        book_id = st.selectbox(
            "Libro disponible",
            options=[b["id"] for b in libros_disponibles],
            format_func=lambda x: next(b["titulo"] for b in libros_disponibles if b["id"] == x)
        )

        submitted = st.form_submit_button("Realizar préstamo")

        if submitted:
            payload = {
                "user_id": user_id,
                "book_id": book_id
            }

            response = requests.post(f"{API_URL}/loans/", json=payload)

            if response.status_code == 200:
                st.success("Préstamo realizado correctamente ✅")
            else:
                try:
                    st.error(response.json()["detail"])
                except Exception:
                    st.error("Error al registrar el préstamo")
