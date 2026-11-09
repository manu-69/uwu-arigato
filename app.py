import streamlit as st

# --- ÁREA PRINCIPAL ---
st.title("Mi primera aplicación de Streamlit")
st.write("¡Hola, Streamlit!")
st.write("Esta es una aplicación simple")

# Reemplaza 'logo_uss.png' con el nombre del archivo de la imagen que uses
st.image("logo_uss.png", width=300)

st.button("Haz clic")
texto_principal = st.text_input("Escribe algo:")
st.write(f"Escribiste: {texto_principal}")

# --- BARRA LATERAL ---
st.sidebar.title("Mi primera barra lateral de Streamlit")
st.sidebar.write("¡Hola, Barra Lateral!")
st.sidebar.write("Esto es una barra lateral")

st.sidebar.image("logo_uss.png", width=250)

st.sidebar.button("Haz clic pero en la barra lateral")
texto_barra = st.sidebar.text_input("Escribe algo en la barra:")
st.sidebar.write(f"Escribiste en la barra: {texto_barra}")

