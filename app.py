# app.py

import streamlit as st
import plistlib
import json
from modules.auth_google import login_required

# ────────────────────────────────
# CONFIGURACIÓN DE LA PÁGINA
# ────────────────────────────────
st.set_page_config(
    page_title="Convertir Composer a Timeline",
    page_icon="📂",
    layout="centered",
)

# ────────────────────────────────
# AUTENTICACIÓN
# ────────────────────────────────
login_required()
current_user = st.user.name or "usuario"  # nombre del usuario logueado

# ────────────────────────────────
# FUNCIÓN PARA CONVERTIR PLIST
# ────────────────────────────────
def convert_composer_to_timeline(plist_file, current_user):
    plist_data = plistlib.load(plist_file)
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
            "clips": [],
            "uuid_row": group.get("uuid group", ""),
            "height_real": group.get("height", 20),
            "row_name": group.get("name", ""),
            "color": "0.25,0.25,0.8",
            "row_number": i + 1
        }

        for clip in group.get("clips", []):
            modified_clip = clip.copy()
            if "edit_info" in modified_clip:
                modified_clip["edit_info"]["author"] = current_user
            else:
                modified_clip["edit_info"] = {"author": current_user, "edit_seconds": 0}
            row["clips"].append(modified_clip)

        timeline_data["rows"].append(row)

    return timeline_data

# ────────────────────────────────
# INTERFAZ PRINCIPAL
# ────────────────────────────────
st.image("img/logo2.png", width=150)
st.title("Convertir ***Composer*** a ***Timeline***")

st.write("Subí un archivo `.plist` de **Angles Composer** para convertirlo a `.json` de Timeline.")

uploaded_file = st.file_uploader("📤 Archivo .plist", type="plist")

if uploaded_file is not None:
    st.success("Archivo subido exitosamente.")

    if st.button("⚙️ Convertir a JSON"):
        try:
            timeline_json_data = convert_composer_to_timeline(uploaded_file, current_user)
            json_string = json.dumps(timeline_json_data, indent=2)

            st.download_button(
                label="📥 Descargar JSON",
                file_name="Timeline.json",
                mime="application/json",
                data=json_string,
            )

            with st.expander("👁️ Ver JSON Convertido", expanded=False):
                st.json(timeline_json_data)

        except Exception as e:
            st.error(f"❌ Error en la conversión: {e}")
