import streamlit as st
import requests
import pandas as pd

API_URL = "http://fastapi:8000"

st.title("Devolver Préstamo 🔄")

response = requests.get(f"{API_URL}/loans/user/1")

if response.status_code == 200:
    loans = response.json()

    prestamos_activos = [l for l in loans if l["activo"]]

    if len(prestamos_activos) == 0:
        st.info("No hay préstamos activos.")
    else:
        ids = [l["id"] for l in prestamos_activos]

        loan_id = st.selectbox(
            "Selecciona préstamo a devolver",
            options=ids,
            format_func=lambda x: f"Préstamo {x}"
        )

        if st.button("Devolver libro"):
            response = requests.patch(f"{API_URL}/loans/{loan_id}/return")

            if response.status_code == 200:
                st.success("Libro devuelto correctamente ✅")
            else:
                try:
                    st.error(response.json()["detail"])
                except:
                    st.error("Error al devolver el libro")
else:
    st.error("Error al obtener préstamos")
