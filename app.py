import streamlit as st
import plistlib
import json
# --- Configuración de la página ---
st.set_page_config(
    page_title="Angles Composer to Timeline Converter",
    page_icon=":rocket:",
    layout="wide"
)
def convert_composer_to_timeline(plist_file, current_user):
    """
    Convierte un archivo plist de Angles Composer a un diccionario de Timeline.

    Args:
        plist_file: El archivo plist subido.
        current_user (str): El nombre del usuario actual del sistema.

    Returns:
        dict: El diccionario con la estructura de Timeline.
    """
    plist_data = plistlib.load(plist_file)

    # Esta línea se mantiene exactamente como la ha corregido el usuario.
    valid_groups = [g for g in plist_data.get("groups", []) if g.get("name") != 'Topic' and g.get('clips')]

    timeline_data = {
        "row_count": len(valid_groups),
        "show_rows_by_category": False,
        "uuid_timeline": plist_data.get("UUID composer", ""),
        "rows": [],
        "data_version": 2
    }

    for i, group in enumerate(valid_groups):
        row = {
            "height": group.get("height", 20),
            "clips": [], # Inicializar clips como una lista vacía para reconstruirla
            "uuid_row": group.get("uuid group", ""),
            "height_real": group.get("height", 20),
            "row_name": group.get("name", ""),
            "color": "0.25,0.25,0.8",
            "row_number": i + 1
        }

        for clip in group.get("clips", []):
            # Crear una copia del clip para modificar edit_info
            modified_clip = clip.copy()
            
            # Actualizar el autor en edit_info
            if "edit_info" in modified_clip:
                modified_clip["edit_info"]["author"] = current_user
            else:
                modified_clip["edit_info"] = {"author": current_user, "edit_seconds": 0} # Añadir un valor por defecto si no existe

            row["clips"].append(modified_clip)
        
        timeline_data["rows"].append(row)

    return timeline_data


# --- Configuración de la barra lateral y lógica de autenticación ---
st.markdown(
    """
    <style>
    [data-testid="stSidebar"] {
        background-color: rgb(25, 26, 38); /* Color de fondo del logo2.png */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

if 'authenticated' not in st.session_state:
    st.session_state['authenticated'] = False
    st.session_state['username'] = ""

with st.sidebar:
    st.image("/Users/martinjauma/Documents/CODIGO/AnglesComposerToTimeline/img/logo2.png", width=150) # Usando logo2.png
    st.title("Autenticación")

    if not st.session_state['authenticated']:
        username = st.text_input("Usuario")
        password = st.text_input("Contraseña", type="password")

        if st.button("Iniciar Sesión"):
            if username == "Angles" and password == "json":
                st.session_state['authenticated'] = True
                st.session_state['username'] = username
                st.success("¡Inicio de sesión exitoso!")
                st.rerun()
            else:
                st.error("Usuario o contraseña incorrectos.")
    else:
        st.write(f"Bienvenido, {st.session_state['username']}!")
        if st.button("Cerrar Sesión"):
            st.session_state['authenticated'] = False
            st.session_state['username'] = ""
            st.success("Sesión cerrada correctamente.")
            st.rerun()

# --- Contenido de la Aplicación Principal (solo si está autenticado) ---
if st.session_state['authenticated']:
    st.title("Convertir ***Composer*** a  ***Timeline***")

    st.write("Sube un archivo .plist de ***Angles Standaloan Composer Archive*** para convertirlo a un archivo .json de Timeline.")

    # Usar el nombre de usuario autenticado
    authenticated_username = st.session_state['username']
    # st.info(f"Usuario actual: {authenticated_username}")

    uploaded_file = st.file_uploader("Elige un archivo .plist", type="plist")

    if uploaded_file is not None:
        st.write("Archivo subido exitosamente.")

        if st.button("Convertir a JSON"):
            try:
                timeline_json_data = convert_composer_to_timeline(uploaded_file, authenticated_username)
                
                st.success("¡Conversión exitosa!")

                # Convertir el diccionario a una cadena de texto para la descarga
                json_string = json.dumps(timeline_json_data, indent=2)

                st.download_button(
                    label="Descargar JSON",
                    file_name="Timeline.json",
                    mime="application/json",
                    data=json_string,
                )

                # Mostrar el JSON contraído
                with st.expander("Ver JSON Convertido", expanded=False):
                    st.json(timeline_json_data)

            except Exception as e:
                st.error(f"Ocurrió un error durante la conversión: {e}")
else:
    st.info("Por favor, inicia sesión en la barra lateral para usar la aplicación.")