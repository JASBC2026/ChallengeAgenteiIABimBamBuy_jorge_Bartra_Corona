
import streamlit as st
from rag import preguntar



# Configuración de la página
st.set_page_config(
    page_title="BimBam Buy AI",
    page_icon="🤖",
    layout="centered"
)


# Estilos CSS


st.markdown(
    """
    <style>

    /* Fondo general */
    .stApp {

        background: linear-gradient(
            135deg,
            #071A33,
            #0B2A4A
        );

    }


    /* Título principal */
    h1 {

        color: #00F5D4;

        text-align: center;

        font-size: 45px;

        font-weight: 800;

    }


    /* Subtítulos */
    h2, h3 {

        color: #00F5D4;

    }


    /* Texto general */
    p, label {

        color: #FFFFFF;

    }



    /* Caja de consulta */

    .stTextInput input {

        background-color: #FFFFFF;

        color: #071A33;

        border-radius: 15px;

        border: 3px solid #00F5D4;

        padding: 12px;

        font-size: 16px;

    }


    /* Placeholder */

    .stTextInput input::placeholder {

        color: #64748B;

    }



    /* Botones */

    .stButton button {

        width: 100%;

        height: 45px;

        background-color: #FF8C42;

        color: #FFFFFF;

        border-radius: 15px;

        border: none;

        font-size: 18px;

        font-weight: bold;

        transition: 0.3s;

    }



    /* Efecto al pasar el mouse */

    .stButton button:hover {

        background-color: #00F5D4;

        color: #071A33;

    }



    /* Tarjetas del chat */

    .chat-card {

        background: #163B63;

        padding: 25px;

        border-radius: 20px;

        box-shadow:

        0px 8px 25px rgba(0,0,0,0.45);

        margin-bottom: 25px;

        border-left: 5px solid #00F5D4;

    }



    /* Usuario */

    .usuario {

        color: #00F5D4;

        font-size: 20px;

        font-weight: bold;

    }



    /* Inteligencia artificial */

    .robot {

        color: #FFC857;

        font-size: 20px;

        font-weight: bold;

    }



    /* Separadores */

    hr {

        border-color: #00F5D4;
        line-height: 1.6;

    }



    /* Métricas superiores */

    [data-testid="stMetricValue"] {

        color: #00F5D4;

        font-weight: bold;

    }


    [data-testid="stMetricLabel"] {

        color: #FFFFFF;

    }



    /* Caja de fuentes */

    .stSuccess {

        background-color: #184A63;

        border-left: 5px solid #00F5D4;

        color: #00F5D4;
        
        font-weight: bold;
    }

  /* Historial */

    h3 {

       color: #00F5D4 !important; 
    }
    
    /* Spinner */

   [data-testid="stSpinner"] {

           color: #00F5D4;

    }

    /* Divider */

  hr {
       
     border: 1px solid #00F5D4;

    }
    
    /* Respuesta del asistente */

 .respuesta {

      color: #FFFFFF !important;

      font-size: 16px;

      line-height: 1.7;

      white-space: pre-wrap;
    }
    
    </style>
    """,
    unsafe_allow_html=True
)


# Encabezado

st.title("🤖 BimBam Buy AI")

st.markdown(
    """
    <h3 style='text-align:center'>
    Asistente inteligente basado en RAG
    </h3>
    
    <p style='text-align:center'>
    Consultá información empresarial utilizando documentos cargados.
    </p>
    """,
    unsafe_allow_html=True
)



# Indicadores técnicos

col1, col2, col3 = st.columns(3)


with col1:
    st.metric(
        "📚 Documentos",
        "Activos"
    )


with col2:
    st.metric(
        "🧠 Modelo",
        "Gemini"
    )


with col3:
    st.metric(
        "📦 Base",
        "ChromaDB"
    )



# Historial

if "historial" not in st.session_state:
    st.session_state.historial = []



# Pregunta

pregunta = st.text_input(
    "🔎 Escribí tu consulta:"
    
)


# Botón consultar

if st.button("🔍 Consultar"):

    if pregunta:

        with st.spinner(
            "🤖 Analizando documentos..."
        ):

            respuesta, fuentes = preguntar(pregunta)

            # Mostrar en la terminal qué devuelve rag.py
            print("===================================")
            print("RESPUESTA RECIBIDA:")
            print(respuesta)
            print("===================================")
            print("FUENTES:")
            print(fuentes)
            print("===================================")

        st.session_state.historial.append(
            {
                "pregunta": pregunta,
                "respuesta": respuesta,
                "fuentes": fuentes
            }
        )




# Mostrar historial


st.subheader("💬 Conversación")


for chat in st.session_state.historial:


    
    st.markdown(
        """
        <div class="chat-card">

        <p class="usuario">
        👤 Usuario
        </p>
        """,
        unsafe_allow_html=True
    )


    st.markdown(chat["pregunta"])


    st.markdown(
        """
        <p class="robot">
        🤖 BimBam Buy AI
        </p>
        """,
        unsafe_allow_html=True
    )


    st.markdown(
        
        f"<div class='respuesta'>{chat['respuesta'].replace(chr(10), '<br>')}</div>",
        unsafe_allow_html=True,  
    )


    st.markdown(
        "</div>",
        unsafe_allow_html=True
    )




    st.markdown(
        "### 📄 Documentos utilizados"
    )


    for fuente in chat["fuentes"]:

        st.success(
            f"📄 {fuente}"
        )



    col1, col2 = st.columns(2)


    with col1:

        st.button(
            "👍 Útil",
            key=f"like_{chat['pregunta']}"
        )


    with col2:

        st.button(
            "👎 Mejorar",
            key=f"dislike_{chat['pregunta']}"
        )


    st.divider()