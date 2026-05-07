import streamlit as st
import requests
import pandas as pd

API_URL = "http://fastapi:8000"

st.set_page_config(
    page_title="Biblioteca Nexus",
    page_icon="📚",
    layout="wide"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background: linear-gradient(135deg, #020617 0%, #0F172A 45%, #1E293B 100%);
    color: white;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
}

[data-testid="stSidebar"] {
    background: rgba(15, 23, 42, 0.98);
    border-right: 1px solid rgba(148, 163, 184, 0.2);
}

[data-testid="stSidebar"] * {
    color: white;
}

.hero-wrapper {
    background: radial-gradient(circle at top left, rgba(59,130,246,0.55), transparent 35%),
                linear-gradient(135deg, rgba(30,64,175,0.95), rgba(15,23,42,0.95));
    border: 1px solid rgba(147, 197, 253, 0.25);
    border-radius: 32px;
    padding: 42px;
    margin-bottom: 30px;
    box-shadow: 0 25px 80px rgba(0,0,0,0.35);
}

.badge {
    display: inline-block;
    padding: 8px 14px;
    background: rgba(96,165,250,0.18);
    color: #BFDBFE;
    border: 1px solid rgba(147,197,253,0.35);
    border-radius: 999px;
    font-size: 13px;
    font-weight: 700;
    margin-bottom: 16px;
}

.hero-title {
    font-size: 56px;
    line-height: 1.05;
    font-weight: 900;
    color: white;
    margin: 0;
}

.hero-subtitle {
    font-size: 19px;
    color: #CBD5E1;
    max-width: 820px;
    margin-top: 18px;
}

.glass-card {
    background: rgba(255,255,255,0.08);
    border: 1px solid rgba(255,255,255,0.16);
    border-radius: 28px;
    padding: 26px;
    box-shadow: 0 20px 60px rgba(0,0,0,0.22);
    backdrop-filter: blur(16px);
}

.metric-card {
    background: linear-gradient(145deg, rgba(255,255,255,0.12), rgba(255,255,255,0.04));
    border: 1px solid rgba(255,255,255,0.16);
    border-radius: 26px;
    padding: 24px;
    min-height: 145px;
    box-shadow: 0 16px 40px rgba(0,0,0,0.22);
}

.metric-label {
    color: #CBD5E1;
    font-size: 14px;
    font-weight: 700;
    margin-bottom: 10px;
}

.metric-value {
    color: white;
    font-size: 42px;
    font-weight: 900;
}

.metric-note {
    color: #94A3B8;
    font-size: 13px;
    margin-top: 8px;
}

.section-title-dark {
    color: white;
    font-size: 28px;
    font-weight: 900;
    margin: 35px 0 15px 0;
}

.feature-card {
    background: rgba(255,255,255,0.07);
    border: 1px solid rgba(255,255,255,0.14);
    border-radius: 26px;
    padding: 26px;
    min-height: 190px;
    transition: transform .2s ease, border .2s ease;
}

.feature-card:hover {
    transform: translateY(-4px);
    border: 1px solid rgba(96,165,250,0.7);
}

.feature-icon {
    font-size: 36px;
    margin-bottom: 12px;
}

.feature-title {
    font-size: 22px;
    font-weight: 800;
    color: white;
    margin-bottom: 8px;
}

.feature-text {
    color: #CBD5E1;
    font-size: 15px;
}

.table-wrap {
    background: white;
    border-radius: 24px;
    padding: 18px;
    color: #0F172A;
}

div[data-testid="stMetric"] {
    background: rgba(255,255,255,0.08);
    border: 1px solid rgba(255,255,255,0.15);
    border-radius: 24px;
    padding: 18px;
}

.stButton > button {
    background: linear-gradient(135deg, #2563EB, #38BDF8);
    color: white;
    border: none;
    border-radius: 16px;
    padding: 0.75rem 1.1rem;
    font-weight: 800;
}

.stButton > button:hover {
    background: linear-gradient(135deg, #1D4ED8, #0EA5E9);
    color: white;
}
</style>
""", unsafe_allow_html=True)


@st.cache_data
def get_data(endpoint):
    try:
        response = requests.get(f"{API_URL}{endpoint}")
        if response.status_code == 200:
            return response.json()
    except Exception:
        return []
    return []


books = get_data("/books/")
users = get_data("/users/")

total_books = len(books)
available_books = len([b for b in books if b.get("disponible")])
borrowed_books = total_books - available_books
total_users = len(users)

st.sidebar.markdown("## 📚 Biblioteca Nexus")
st.sidebar.markdown("Panel avanzado de gestión bibliotecaria")
st.sidebar.divider()
st.sidebar.markdown("### Navegación")
st.sidebar.markdown("Usa las páginas laterales para gestionar libros, usuarios, préstamos e historial.")
st.sidebar.divider()
if st.sidebar.button("🔄 Refrescar datos"):
    st.cache_data.clear()
    st.rerun()

st.markdown("""
<div class="hero-wrapper">
    <div class="badge">Sistema profesional · FastAPI · Streamlit · PostgreSQL</div>
    <h1 class="hero-title">Biblioteca Nexus</h1>
    <p class="hero-subtitle">
        Plataforma moderna para gestionar catálogos, usuarios, préstamos, devoluciones e historial
        con arquitectura desacoplada, base de datos real y visualización ejecutiva.
    </p>
</div>
""", unsafe_allow_html=True)

m1, m2, m3, m4 = st.columns(4)

with m1:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">📘 Libros totales</div>
        <div class="metric-value">{total_books}</div>
        <div class="metric-note">Elementos registrados en catálogo</div>
    </div>
    """, unsafe_allow_html=True)

with m2:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">🟢 Disponibles</div>
        <div class="metric-value">{available_books}</div>
        <div class="metric-note">Libros listos para préstamo</div>
    </div>
    """, unsafe_allow_html=True)

with m3:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">🔴 Prestados</div>
        <div class="metric-value">{borrowed_books}</div>
        <div class="metric-note">Libros actualmente en préstamo</div>
    </div>
    """, unsafe_allow_html=True)

with m4:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">👥 Usuarios</div>
        <div class="metric-value">{total_users}</div>
        <div class="metric-note">Lectores registrados</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="section-title-dark">Panel ejecutivo</div>', unsafe_allow_html=True)

left, right = st.columns([2, 1])

with left:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown("### 📖 Últimos libros registrados")

    if books:
        df = pd.DataFrame(books)
        df = df[["titulo", "autor", "genero", "disponible"]].tail(8)
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
    else:
        st.info("Todavía no hay libros registrados.")

    st.markdown('</div>', unsafe_allow_html=True)

with right:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown("### 📊 Estado del catálogo")

    chart_data = pd.DataFrame({
        "Estado": ["Disponibles", "Prestados"],
        "Cantidad": [available_books, borrowed_books]
    })

    st.bar_chart(chart_data.set_index("Estado"))
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="section-title-dark">Módulos del sistema</div>', unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">📚</div>
        <div class="feature-title">Catálogo inteligente</div>
        <div class="feature-text">
            Consulta libros, disponibilidad, búsqueda por autor o título y estado del inventario.
        </div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">👤</div>
        <div class="feature-title">Gestión de usuarios</div>
        <div class="feature-text">
            Registra usuarios, evita duplicados y mantiene una base organizada de lectores.
        </div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">🔄</div>
        <div class="feature-title">Préstamos e historial</div>
        <div class="feature-text">
            Controla préstamos, devoluciones, historial por usuario y analítica temporal.
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="section-title-dark">Stack técnico</div>', unsafe_allow_html=True)

s1, s2, s3, s4 = st.columns(4)

with s1:
    st.markdown('<div class="feature-card"><div class="feature-title">FastAPI</div><div class="feature-text">API REST modular con routers.</div></div>', unsafe_allow_html=True)

with s2:
    st.markdown('<div class="feature-card"><div class="feature-title">PostgreSQL</div><div class="feature-text">Base de datos en tercer contenedor.</div></div>', unsafe_allow_html=True)

with s3:
    st.markdown('<div class="feature-card"><div class="feature-title">Docker</div><div class="feature-text">Entorno reproducible con Compose.</div></div>', unsafe_allow_html=True)

with s4:
    st.markdown('<div class="feature-card"><div class="feature-title">Pytest</div><div class="feature-text">Tests, mocks, integración y coverage.</div></div>', unsafe_allow_html=True)
