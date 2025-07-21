# pages/3_privacy_policy.py

import streamlit as st

st.set_page_config(
    page_title="Política de Privacidad",
    page_icon="🛡️",
    layout="centered",
)

st.title("Política de Privacidad")

st.write("Última actualización: 20 de julio de 2025")

st.header("1. Introducción")
st.write("""
Esta Política de Privacidad describe cómo se recopila, utiliza y comparte su información cuando utiliza nuestra aplicación "Convertir Composer a Timeline" (el "Servicio").
""")

st.header("2. Información que Recopilamos")
st.write("""
Recopilamos la siguiente información:
- **Información de autenticación:** Cuando inicia sesión con Google, recibimos su nombre, dirección de correo electrónico y foto de perfil, según lo permitido por la configuración de su cuenta de Google.
- **Datos de uso:** Para fines de seguridad y auditoría, registramos su dirección de correo electrónico y la fecha/hora cada vez que inicia sesión correctamente en el Servicio. Esta información se almacena en una base de datos de MongoDB.
- **Archivos de usuario:** Los archivos `.plist` que sube se procesan en memoria y no se almacenan en nuestros servidores. El archivo `.json` resultante se genera para su descarga directa.
""")

st.header("3. Cómo Usamos Su Información")
st.write("""
Utilizamos la información que recopilamos para:
- Proveer y mantener el Servicio.
- Personalizar su experiencia, mostrando su nombre de usuario.
- Marcar la autoría en los archivos `.json` convertidos.
- Monitorear la seguridad y el uso de nuestro Servicio.
""")

st.header("4. Intercambio de Información")
st.write("""
No compartimos su información personal con terceros, excepto en los siguientes casos:
- Para cumplir con la ley.
- Para proteger nuestros derechos.
- Con proveedores de servicios que nos asisten en la operación del Servicio (como Google para la autenticación y MongoDB para el almacenamiento de registros), quienes están obligados a mantener la confidencialidad de la información.
""")

st.header("5. Seguridad de los Datos")
st.write("""
Tomamos medidas razonables para proteger la información que recopilamos. Sin embargo, ningún sistema de seguridad es impenetrable y no podemos garantizar la seguridad absoluta de sus datos.
""")

st.header("6. Sus Derechos")
st.write("""
Usted tiene derecho a acceder, corregir o eliminar su información personal. Puede gestionar los permisos de su cuenta de Google a través de la configuración de seguridad de Google.
""")

st.header("7. Contacto")
st.write("""
Si tiene alguna pregunta sobre esta Política de Privacidad, por favor contáctenos en [su email de contacto].
""")
