import streamlit as st


def apply_global_styles():
    st.markdown(
        """
        <style>
        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
        }

        .hero {
            background: linear-gradient(135deg, #1E3A8A 0%, #2563EB 45%, #38BDF8 100%);
            padding: 32px;
            border-radius: 24px;
            color: white;
            margin-bottom: 28px;
            box-shadow: 0 12px 30px rgba(37, 99, 235, 0.25);
        }

        .hero h1 {
            font-size: 44px;
            margin-bottom: 8px;
        }

        .hero p {
            font-size: 18px;
            opacity: 0.95;
        }

        .card {
            background: white;
            padding: 24px;
            border-radius: 22px;
            border: 1px solid #E2E8F0;
            box-shadow: 0 8px 24px rgba(15, 23, 42, 0.08);
            margin-bottom: 18px;
        }

        .mini-card {
            background: #FFFFFF;
            padding: 20px;
            border-radius: 20px;
            border: 1px solid #E2E8F0;
            box-shadow: 0 6px 18px rgba(15, 23, 42, 0.06);
            height: 100%;
        }

        .section-title {
            font-size: 26px;
            font-weight: 800;
            color: #0F172A;
            margin-top: 20px;
            margin-bottom: 14px;
        }

        .muted {
            color: #64748B;
            font-size: 15px;
        }

        div[data-testid="stMetric"] {
            background: white;
            padding: 18px;
            border-radius: 18px;
            border: 1px solid #E2E8F0;
            box-shadow: 0 6px 18px rgba(15, 23, 42, 0.06);
        }

        .stButton > button {
            border-radius: 14px;
            padding: 0.6rem 1rem;
            font-weight: 700;
            border: none;
            background: #2563EB;
            color: white;
        }

        .stButton > button:hover {
            background: #1D4ED8;
            color: white;
        }

        [data-testid="stSidebar"] {
            background: #0F172A;
        }

        [data-testid="stSidebar"] * {
            color: white;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def hero(title, subtitle):
    st.markdown(
        f"""
        <div class="hero">
            <h1>{title}</h1>
            <p>{subtitle}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def section_title(text):
    st.markdown(f'<div class="section-title">{text}</div>', unsafe_allow_html=True)


def card_start():
    st.markdown('<div class="card">', unsafe_allow_html=True)


def card_end():
    st.markdown('</div>', unsafe_allow_html=True)
