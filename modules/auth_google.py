# auth.py

import streamlit as st
from pymongo import MongoClient
import datetime

# Conexión a MongoDB
try:
    client = MongoClient(st.secrets["MONGO_URI"])
    db = client.login_logs # Nombre de la base de datos
    login_collection = db.logs # Nombre de la colección
except Exception as e:
    st.error(f"Error al conectar a MongoDB: {e}")
    st.stop()

def login_required():
    """
    Verifica si el usuario está logueado. Si no, muestra la pantalla de login.
    Llamar esto al inicio de cada app para forzar login antes de mostrar el contenido.
    """
    if not getattr(st.user, "is_logged_in", False):
        _show_login_screen()
        st.stop()  # Detiene la ejecución de la app si no está logueado
    else:
        _log_login_event(st.user.email)
        _show_user_sidebar()

def _log_login_event(user_email):
    try:
        login_data = {
            "timestamp": datetime.datetime.now(),
            "user_email": user_email
        }
        login_collection.insert_one(login_data)
    except Exception as e:
        st.warning(f"No se pudo registrar el inicio de sesión en MongoDB: {e}")

def _show_login_screen():
    st.set_page_config(initial_sidebar_state="collapsed")
    st.markdown("""
        <style>
            [data-testid="stSidebar"] {
                display: none;
            }
        </style>
    """, unsafe_allow_html=True)

    st.title("🔐 Inicio de sesión requerido")
    st.subheader("Iniciá sesión con Google para continuar.")
    st.button("➡️ Iniciar sesión con Google", on_click=st.login, type="primary")

def _show_user_sidebar():
    with st.sidebar:
        st.sidebar.image("img/logo2.png", width=200)
        st.divider()
        # st.header("👤 Usuario")
        col1, col2 = st.columns([1, 3])
        with col1:
            if st.user.picture:
                st.image(st.user.picture, use_container_width=True)
        with col2:
            st.subheader(st.user.name)
        st.caption(st.user.email)
        st.button("🚪 Cerrar sesión", on_click=st.logout)
