import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Consola del Pastor",
    page_icon="✝️",
    layout="wide"
)

# CSS personalizado
st.markdown("""
    <style>
    .stApp {
        background-color: #1a1a2e;
    }
    .big-text {
        font-size: 48px;
        text-align: center;
        padding: 50px;
        color: white;
        background-color: #16213e;
        border-radius: 10px;
        min-height: 400px;
        display: flex;
        align-items: center;
        justify-content: center;
        margin-top: 20px;
    }
    .status {
        color: #4CAF50;
        font-size: 16px;
    }
    </style>
    """, unsafe_allow_html=True)

# Inicializar estado
if 'texto_actual' not in st.session_state:
    st.session_state.texto_actual = "Esperando al pastor..."

# Layout en columnas
col1, col2 = st.columns([1, 2])

with col1:
    st.markdown("### 📝 Panel de Control")
    st.markdown('<p class="status">✅ Conectado</p>', unsafe_allow_html=True)
    
    # Campo de texto
    nuevo_texto = st.text_area(
        "Mensaje para la congregación:",
        height=250,
        placeholder="Escribe aquí el mensaje..."
    )
    
    # Botones
    col_btn1, col_btn2 = st.columns(2)
    
    with col_btn1:
        if st.button("📢 Actualizar", type="primary", use_container_width=True):
            if nuevo_texto.strip():
                st.session_state.texto_actual = nuevo_texto
                st.success("✅ Actualizado")
            else:
                st.warning("⚠️ Escribe algo")
    
    with col_btn2:
        if st.button("🗑️ Limpiar", use_container_width=True):
            st.session_state.texto_actual = "Esperando al pastor..."
            st.info("Limpiado")

with col2:
    st.markdown("### 📺 Pantalla de Proyección")
    
    # Mostrar texto grande
    st.markdown(f'<div class="big-text">{st.session_state.texto_actual}</div>', 
                unsafe_allow_html=True)
