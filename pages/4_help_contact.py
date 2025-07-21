# pages/4_help_contact.py

import streamlit as st

st.set_page_config(
    page_title="Ayuda y Contacto",
    page_icon="❓",
    layout="centered",
)

st.title("Ayuda y Contacto")

st.header("¿Cómo funciona?")
st.write("""
1.  **Inicia sesión:** Utiliza tu cuenta de Google para acceder a la aplicación.
2.  **Sube tu archivo:** Arrastra y suelta o selecciona un archivo `.plist` generado por la aplicación Angles Composer.
3.  **Convierte:** Haz clic en el botón "Convertir a JSON".
4.  **Descarga:** Una vez procesado, podrás descargar el archivo `Timeline.json` resultante y, opcionalmente, previsualizar su contenido.
""")

st.header("Preguntas Frecuentes (FAQ)")
st.subheader("¿Mis archivos están seguros?")
st.write("Sí. Tus archivos se procesan en el momento y no se guardan en nuestro servidor. La conexión es segura y tu privacidad es nuestra prioridad.")

st.subheader("¿Qué pasa si la conversión falla?")
st.write("Si encuentras un error, asegúrate de que tu archivo `.plist` no esté corrupto y haya sido generado correctamente. Si el problema persiste, no dudes en contactarnos.")

st.header("Contacto")
st.write("Para cualquier problema, sugerencia o pregunta, por favor envía un correo electrónico a:")
st.info("[tu email de contacto]")
