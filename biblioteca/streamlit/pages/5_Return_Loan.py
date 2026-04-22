import streamlit as st
import requests

API_URL = "http://fastapi:8000"

st.title("Devolver Préstamo 🔄")

users_response = requests.get(f"{API_URL}/users/")
users = users_response.json() if users_response.status_code == 200 else []

if len(users) == 0:
    st.info("No hay usuarios registrados.")
else:
    user_id = st.selectbox(
        "Selecciona usuario",
        options=[u["id"] for u in users],
        format_func=lambda x: next(u["nombre"] for u in users if u["id"] == x)
    )

    history_response = requests.get(f"{API_URL}/loans/user/{user_id}")

    if history_response.status_code == 200:
        loans = history_response.json()
        prestamos_activos = [l for l in loans if l["activo"]]

        if len(prestamos_activos) == 0:
            st.info("Este usuario no tiene préstamos activos.")
        else:
            loan_id = st.selectbox(
                "Selecciona préstamo a devolver",
                options=[l["id"] for l in prestamos_activos],
                format_func=lambda x: next(
                    f'{l["titulo"]} (Préstamo {l["id"]})'
                    for l in prestamos_activos if l["id"] == x
                )
            )

            if st.button("Devolver libro"):
                response = requests.patch(f"{API_URL}/loans/{loan_id}/return")

                if response.status_code == 200:
                    st.success("Libro devuelto correctamente ✅")
                else:
                    try:
                        st.error(response.json()["detail"])
                    except Exception:
                        st.error("Error al devolver el libro")
    else:
        st.error("Error al obtener el historial del usuario")
