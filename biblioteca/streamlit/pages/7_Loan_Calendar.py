import streamlit as st
import requests
import pandas as pd

API_URL = "http://fastapi:8000"

st.title("Calendario de Préstamos 📅")

# Obtener usuarios
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
        st.error("Error al obtener préstamos.")
    else:
        loans = response.json()

        if not loans:
            st.info("Este usuario no tiene préstamos registrados.")
        else:
            df = pd.DataFrame(loans)

            # Convertir fechas
            df["fecha_prestamo"] = pd.to_datetime(df["fecha_prestamo"])
            df["fecha_devolucion"] = pd.to_datetime(df["fecha_devolucion"], errors="coerce")

            # Crear columna fecha simple
            df["Fecha"] = df["fecha_prestamo"].dt.date

            # Estado simple para gráfico
            df["Estado_simple"] = df["activo"].apply(
                lambda x: "Activo" if x else "Devuelto"
            )

            # 🔹 RESUMEN
            resumen = df.groupby(["Fecha", "Estado_simple"]).size().reset_index(name="Cantidad")

            st.subheader("Resumen de préstamos por fecha")
            st.dataframe(resumen, use_container_width=True, hide_index=True)

            # 🔹 GRÁFICO
            st.subheader("Visualización temporal")
            chart_data = resumen.pivot(index="Fecha", columns="Estado_simple", values="Cantidad").fillna(0)
            st.bar_chart(chart_data)

            # 🔹 DETALLE
            st.subheader("Detalle de eventos")

            df_detalle = df.copy()

            df_detalle = df_detalle.rename(columns={
                "titulo": "Libro",
                "fecha_prestamo": "Fecha préstamo",
                "fecha_devolucion": "Fecha devolución"
            })

            # Formatear fechas
            df_detalle["Fecha préstamo"] = df_detalle["Fecha préstamo"].dt.strftime("%d-%m-%Y %H:%M")

            df_detalle["Fecha devolución"] = df_detalle["Fecha devolución"].apply(
                lambda x: x.strftime("%d-%m-%Y %H:%M") if pd.notnull(x) else "-"
            )

            # Estado visual
            df_detalle["Estado"] = df_detalle["activo"].apply(
                lambda x: "🟢 Activo" if x else "🔴 Devuelto"
            )

            df_detalle = df_detalle[["Libro", "Fecha préstamo", "Fecha devolución", "Estado"]]

            st.dataframe(df_detalle, use_container_width=True, hide_index=True)
