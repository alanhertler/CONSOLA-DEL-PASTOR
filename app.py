import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Consola del Pastor",
    page_icon="✝️",
    layout="wide"
)

# CSS mejorado con letras más elegantes
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600&family=Merriweather:wght@300;400&display=swap');
    
    .stApp {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
    }
    
    .big-text {
        font-family: 'Merriweather', serif;
        font-size: 56px;
        font-weight: 300;
        text-align: center;
        padding: 60px 40px;
        color: #ffffff;
        background: linear-gradient(135deg, #0f3460 0%, #16213e 100%);
        border-radius: 20px;
        min-height: 450px;
        display: flex;
        align-items: center;
        justify-content: center;
        margin-top: 20px;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
        line-height: 1.6;
        border: 2px solid rgba(255, 215, 0, 0.2);
    }
    
    .status {
        color: #4CAF50;
        font-size: 18px;
        font-family: 'Montserrat', sans-serif;
        font-weight: 600;
        text-shadow: 0 0 10px rgba(76, 175, 80, 0.5);
    }
    
    h3 {
        font-family: 'Montserrat', sans-serif !important;
        color: #FFD700 !important;
        font-weight: 600 !important;
        text-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
    }
    
    .stTextArea label {
        font-family: 'Montserrat', sans-serif;
        color: #e0e0e0 !important;
        font-size: 16px;
    }
    
    .stTextArea textarea {
        font-family: 'Merriweather', serif !important;
        font-size: 18px !important;
        background-color: #0f3460 !important;
        color: white !important;
        border: 2px solid rgba(255, 215, 0, 0.3) !important;
        border-radius: 10px !important;
    }
    
    .stButton button {
        font-family: 'Montserrat', sans-serif !important;
        font-weight: 600 !important;
        font-size: 16px !important;
        border-radius: 10px !important;
        padding: 12px 24px !important;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3) !important;
    }
    
    .stSuccess, .stWarning, .stInfo {
        font-family: 'Montserrat', sans-serif !important;
        border-radius: 10px !important;
    }
    </style>
    """, unsafe_allow_html=True)

# Inicializar estado
if 'texto_actual' not in st.session_state:
    st.session_state.texto_actual = "Esperando al pastor..."

# Layout en columnas
col1, col2 = st.columns([1, 2])

with col1:
    st.markdown("### 📝 Panel d
