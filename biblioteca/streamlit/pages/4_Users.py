import streamlit as st
import requests
import pandas as pd

API_URL = "http://fastapi:8000"

st.title("Gestión de Usuarios 👤")

st.subheader("Registrar usuario")

with st.form("form_usuario"):
    nombre = st.text_input("Nombre")
    email = st.text_input("Email")
    submitted = st.form_submit_button("Guardar usuario")

    if submitted:
        payload = {
            "nombre": nombre,
            "email": email
        }

        response = requests.post(f"{API_URL}/users/", json=payload)

        if response.status_code == 200:
            st.success("Usuario registrado correctamente ✅")
        else:
            try:
                st.error(response.json()["detail"])
            except Exception:
                st.error("Error al registrar usuario")

st.divider()

st.subheader("Listado de usuarios")

response = requests.get(f"{API_URL}/users/")

if response.status_code == 200:
    usuarios = response.json()

    if len(usuarios) == 0:
        st.info("No hay usuarios registrados.")
    else:
        df = pd.DataFrame(usuarios)
        st.dataframe(df, use_container_width=True)
else:
    st.error(f"Error al obtener usuarios: {response.status_code}")
