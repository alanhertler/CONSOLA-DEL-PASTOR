import streamlit as st

st.set_page_config(
    page_title="Panel del Pastor",
    page_icon="✝️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700&family=EB+Garamond:ital,wght@0,400;0,600;1,400&display=swap');
    
    :root {
        --oro: #c9a84c;
        --oro-claro: #f0d080;
        --fondo: #0d0d1a;
        --fondo2: #13131f;
        --borde: rgba(201,168,76,0.25);
        --texto: #e8e0cc;
    }
    
    .stApp {
        background: var(--fondo);
        background-image:
            radial-gradient(ellipse at 20% 10%, rgba(201,168,76,0.06) 0%, transparent 50%),
            radial-gradient(ellipse at 80% 90%, rgba(201,168,76,0.04) 0%, transparent 50%);
    }
    
    .header-container {
        text-align: center;
        margin-bottom: 28px;
        padding-top: 30px;
    }
    
    .cruz {
        font-size: 28px;
        color: var(--oro);
        margin-bottom: 6px;
        animation: pulso 3s ease-in-out infinite;
    }
    
    @keyframes pulso {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.6; }
    }
    
    .titulo {
        font-family: 'Cinzel', serif;
        font-size: 22px;
        letter-spacing: 4px;
        color: var(--oro-claro);
        text-transform: uppercase;
        margin-bottom: 4px;
    }
    
    .subtitulo {
        font-size: 11px;
        letter-spacing: 6px;
        color: rgba(201,168,76,0.5);
        font-family: 'EB Garamond', serif;
        font-style: italic;
    }
    
    .estado-bar {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 8px;
        background: rgba(255,255,255,0.04);
        border: 1px solid var(--borde);
        border-radius: 30px;
        padding: 7px 18px;
        font-size: 14px;
        margin: 0 auto 28px;
        width: fit-content;
        font-family: 'EB Garamond', serif;
        color: var(--texto);
    }
    
    .estado-dot {
        width: 8px;
        height: 8px;
        border-radius: 50%;
        background: #4caf82;
        box-shadow: 0 0 8px #4caf82;
        animation: parpadeo 2s ease-in-out infinite;
    }
    
    @keyframes parpadeo {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.4; }
    }
    
    .ultimo-enviado {
        background: rgba(201,168,76,0.06);
        border: 1px solid var(--borde);
        border-radius: 10px;
        padding: 14px 20px;
        margin: 0 auto 28px;
        font-style: italic;
        font-size: 15px;
        color: rgba(232,224,204,0.7);
        text-align: center;
        font-family: 'EB Garamond', serif;
        max-width: 600px;
    }
    
    .grilla-botones {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 14px;
        max-width: 600px;
        margin: 0 auto 20px;
    }
    
    .btn-versiculo {
        background: linear-gradient(135deg, rgba(201,168,76,0.08), rgba(201,168,76,0.03));
        border: 1px solid var(--borde);
        border-radius: 12px;
        padding: 18px 16px;
        cursor: pointer;
        text-align: left;
        transition: all 0.2s ease;
        font-family: 'EB Garamond', serif;
    }
    
    .btn-versiculo:hover {
        border-color: rgba(201,168,76,0.6);
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(201,168,76,0.15);
    }
    
    .ref {
        font-family: 'Cinzel', serif;
        font-size: 12px;
        letter-spacing: 2px;
        color: var(--oro);
        margin-bottom: 6px;
        display: block;
    }
    
    .texto-corto {
        font-size: 14px;
        line-height: 1.5;
        color: rgba(232,224,204,0.85);
        font-style: italic;
    }
    
    .separador {
        text-align: center;
        font-family: 'Cinzel', serif;
        font-size: 10px;
        letter-spacing: 4px;
        color: rgba(201,168,76,0.3);
        margin: 20px 0 14px;
    }
    
    .stButton button {
        width: 100%;
        background: linear-gradient(135deg, rgba(201,168,76,0.08), rgba(201,168,76,0.03)) !important;
        border: 1px solid var(--borde) !important;
        border-radius: 12px !important;
        padding: 18px 16px !important;
        color: var(--texto) !important;
        font-family: 'EB Garamond', serif !important;
        transition: all 0.2s ease !important;
    }
    
    .stButton button:hover {
        border-color: rgba(201,168,76,0.6) !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 20px rgba(201,168,76,0.15) !important;
    }
    
    .stTextInput input {
        background: rgba(0,0,0,0.3) !important;
        border: 1px solid rgba(201,168,76,0.2) !important;
        border-radius: 8px !important;
        color: var(--texto) !important;
        font-family: 'EB Garamond', serif !important;
        font-size: 15px !important;
    }
    
    .stTextInput input:focus {
        border-color: var(--oro) !important;
    }
    
    h1, h2, h3 {
        display: none !important;
    }
    
    .block-container {
        max-width: 650px !important;
        padding-top: 2rem !important;
    }
    </style>
    """, unsafe_allow_html=True)

# Header
st.markdown("""
    <div class="header-container">
        <div class="cruz">✝</div>
        <div class="titulo">Panel del Pastor</div>
        <div class="subtitulo">Culto Digital Sincronizado</div>
    </div>
    """, unsafe_allow_html=True)

# Estado
st.markdown("""
    <div class="estado-bar">
        <div class="estado-dot"></div>
        <span>Conectado al servidor ✓</span>
    </div>
    """, unsafe_allow_html=True)

# Inicializar estado
if 'texto_actual' not in st.session_state:
    st.session_state.texto_actual = "— Ningún mensaje enviado aún —"

# Último mensaje enviado
st.markdown(f'<div class="ultimo-enviado">{st.session_state.texto_actual}</div>', unsafe_allow_html=True)

# Versículos predefinidos
versiculos = [
    {
        "ref": "Juan 3:16",
        "corto": "Porque de tal manera amó Dios al mundo...",
        "completo": "Juan 3:16 — Porque de tal manera amó Dios al mundo, que ha dado a su Hijo unigénito, para que todo aquel que en él cree, no se pierda, mas tenga vida eterna."
    },
    {
        "ref": "Salmo 23:1",
        "corto": "El Señor es mi pastor, nada me faltará.",
        "completo": "Salmo 23:1 — El Señor es mi pastor; nada me faltará. En lugares de delicados pastos me hará descansar."
    },
    {
        "ref": "Filipenses 4:13",
        "corto": "Todo lo puedo en Cristo que me fortalece.",
        "completo": "Filipenses 4:13 — Todo lo puedo en Cristo que me fortalece."
    },
    {
        "ref": "Jeremías 29:11",
        "corto": "Planes de bienestar y no de calamidad...",
        "completo": "Jeremías 29:11 — Porque yo sé los pensamientos que tengo acerca de vosotros, dice el Señor, pensamientos de paz y no de mal, para daros el futuro que esperáis."
    },
    {
        "ref": "Romanos 8:28",
        "corto": "A los que aman a Dios, todo les ayuda a bien.",
        "completo": "Romanos 8:28 — Y sabemos que a los que aman a Dios, todas las cosas les ayudan a bien, esto es, a los que conforme a su propósito son llamados."
    },
    {
        "ref": "Proverbios 3:5-6",
        "corto": "Confía en el Señor con todo tu corazón...",
        "completo": "Proverbios 3:5-6 — Confía en el Señor con todo tu corazón, y no te apoyes en tu propia prudencia. Reconócelo en todos tus caminos, y él enderezará tus veredas."
    },
    {
        "ref": "Mateo 11:28",
        "corto": "Venid a mí todos los que estáis cansados...",
        "completo": "Mateo 11:28 — Venid a mí todos los que estáis trabajados y cargados, y yo os haré descansar."
    }
]

# Grilla de versículos
st.markdown('<div class="grilla-botones">', unsafe_allow_html=True)

cols = st.columns(2)
for idx, v in enumerate(versiculos):
    with cols[idx % 2]:
        if st.button(f"{v['ref']}", key=f"v{idx}"):
            st.session_state.texto_actual = f'"{v["completo"]}"'
            st.rerun()
        st.markdown(f'<div class="texto-corto" style="margin-top:-10px; margin-bottom:10px;">{v["corto"]}</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Separador
st.markdown('<div class="separador">✦ MENSAJE PERSONALIZADO ✦</div>', unsafe_allow_html=True)

# Campo personalizado
col1, col2 = st.columns([4, 1])
with col1:
    custom_text = st.text_input("", placeholder="Escribí un mensaje libre...", label_visibility="collapsed")
with col2:
    if st.button("ENVIAR"):
        if custom_text.strip():
            st.session_state.texto_actual = f'"{custom_text}"'
            st.rerun()
