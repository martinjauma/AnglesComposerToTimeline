
import streamlit as st

def show_terms_of_service():
    st.set_page_config(
        page_title="Términos de Servicio",
        page_icon="📄",
        layout="centered",
    )

    st.title("Términos de Servicio")

    st.header("1. Aceptación de los Términos")
    st.write("""
    Al utilizar la aplicación web "Convertir Composer a Timeline" (en adelante, "el Servicio"), usted acepta estar sujeto a estos Términos de Servicio ("Términos"). Si no está de acuerdo con estos Términos, no utilice el Servicio.
    """)

    st.header("2. Descripción del Servicio")
    st.write("""
    El Servicio proporciona una herramienta para convertir archivos de formato `.plist` de Angles Composer a formato `.json` de Timeline. El usuario puede subir un archivo `.plist` y descargar el archivo `.json` resultante.
    """)

    st.header("3. Uso del Servicio")
    st.write("""
    Usted se compromete a utilizar el Servicio únicamente con fines lícitos. Usted es el único responsable del contenido de los archivos que sube y convierte. Usted declara y garantiza que tiene todos los derechos necesarios sobre los archivos que utiliza con el Servicio.
    """)

    st.header("4. Privacidad y Datos")
    st.write("""
    El Servicio utiliza la autenticación de Google para identificar a los usuarios. El nombre de usuario asociado a su cuenta de Google se utilizará para marcar el archivo `.json` convertido como autor de la edición. No almacenamos sus archivos `.plist` o `.json` en nuestros servidores después de que se complete la conversión y la descarga.
    """)

    st.header("5. Propiedad Intelectual")
    st.write("""
    El Servicio y su contenido original, características y funcionalidades son y seguirán siendo propiedad exclusiva de sus creadores.
    """)

    st.header("6. Exclusión de Garantías")
    st.write("""
    El Servicio se proporciona "tal cual", sin garantía de ningún tipo, ya sea expresa o implícita. No garantizamos que el Servicio sea ininterrumpido, seguro o libre de errores.
    """)

    st.header("7. Limitación de Responsabilidad")
    st.write("""
    En ningún caso los creadores del Servicio serán responsables de ningún daño indirecto, incidental, especial, consecuente o punitivo que resulte del uso del Servicio.
    """)

    st.header("8. Cambios en los Términos")
    st.write("""
    Nos reservamos el derecho de modificar o reemplazar estos Términos en cualquier momento. Se le notificará de cualquier cambio mediante la publicación de los nuevos Términos en esta página.
    """)

    st.header("9. Contacto")
    st.write("""
    Si tiene alguna pregunta sobre estos Términos, puede contactarnos a través de [email de contacto].
    """)

show_terms_of_service()
