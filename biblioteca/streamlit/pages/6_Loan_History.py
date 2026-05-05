import streamlit as st
import requests
import pandas as pd

API_URL = "http://fastapi:8000"

st.title("Historial de Préstamos 📊")

users_response = requests.get(f"{API_URL}/users/")
users = users_response.json() if users_response.status_code == 200 else []

if not users:
    st.info("No hay usuarios registrados.")
else:
    user_id = st.selectbox(
        "Selecciona usuario",
        options=[u["id"] for u in users],
        format_func=lambda x: next(u["nombre"] for u in users if u["id"] == x)
    )

    response = requests.get(f"{API_URL}/loans/user/{user_id}")

    if response.status_code != 200:
        st.error("Error al obtener el historial.")
    else:
        loans = response.json()

        if not loans:
            st.info("Este usuario no tiene historial de préstamos.")
        else:
            df = pd.DataFrame(loans)

            df = df.rename(columns={
                "titulo": "Libro",
                "fecha_prestamo": "Fecha préstamo",
                "fecha_devolucion": "Fecha devolución",
                "activo": "Estado"
            })

            df["Fecha préstamo"] = pd.to_datetime(df["Fecha préstamo"]).dt.strftime("%d-%m-%Y %H:%M")

            df["Fecha devolución"] = df["Fecha devolución"].apply(
                lambda x: pd.to_datetime(x).strftime("%d-%m-%Y %H:%M") if x else "-"
            )

            df["Estado"] = df["Estado"].apply(
                lambda x: "🟢 Activo" if x else "🔴 Devuelto"
            )

            df = df[["Libro", "Fecha préstamo", "Fecha devolución", "Estado"]]

            st.dataframe(df, use_container_width=True)

