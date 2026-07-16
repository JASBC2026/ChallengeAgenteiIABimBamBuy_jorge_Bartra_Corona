import os

from pypdf import PdfReader

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings


# ==============================
# CONFIGURACIÓN
# ==============================

CARPETA_PDFS = "documentos"
TAMAÑO_CHUNK = 1000

# Colocá acá tu API Key
os.environ["GOOGLE_API_KEY"] = " Acá va su propia API KEY"


# ==============================
# CARGAR DOCUMENTOS
# ==============================

documentos = []

for archivo in os.listdir(CARPETA_PDFS):

    if archivo.endswith(".pdf"):

        ruta = os.path.join(CARPETA_PDFS, archivo)

        reader = PdfReader(ruta)

        texto = ""

        for pagina in reader.pages:

            contenido = pagina.extract_text()

            if contenido:
                texto += contenido

        documentos.append({
            "documento": archivo,
            "texto": texto
        })


# ==============================
# CREAR CHUNKS
# ==============================

chunks = []

for doc in documentos:

    texto = doc["texto"]

    for i in range(0, len(texto), TAMAÑO_CHUNK):

        chunks.append({
            "texto": texto[i:i + TAMAÑO_CHUNK],
            "documento": doc["documento"]
        })


# ==============================
# EMBEDDINGS
# ==============================

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


# ==============================
# BASE VECTORIAL
# ==============================

vectorstore = Chroma.from_texts(
    texts=[chunk["texto"] for chunk in chunks],
    embedding=embeddings,
    metadatas=[
        {"documento": chunk["documento"]}
        for chunk in chunks
    ]
)


# ==============================
# MODELO GEMINI
# ==============================

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
)


# ==============================
# FUNCIÓN PRINCIPAL
# ==============================

def preguntar(pregunta):

    resultados = vectorstore.similarity_search(
        pregunta,
        k=5
    )

    contexto = ""

    documentos_usados = []

    for doc in resultados:

        contexto += f"""

Documento: {doc.metadata['documento']}

Contenido:
{doc.page_content}

----------------------------------------

"""

        if doc.metadata["documento"] not in documentos_usados:
            documentos_usados.append(doc.metadata["documento"])

    prompt = f"""
Sos un asistente inteligente de BimBam Buy.

Tu tarea es responder ÚNICAMENTE utilizando la información presente en el contexto.

No inventes información.

Si la respuesta no aparece claramente en el contexto, respondé exactamente:

"No encontré esa información en los documentos disponibles."

Contexto:

{contexto}

Pregunta:

{pregunta}

Al finalizar agregá:

Fuentes consultadas:

e indicá únicamente los nombres de los documentos utilizados.
"""

    respuesta = llm.invoke(prompt)
    
    respuesta_texto = respuesta.content

    print("\n===================================")
    print("RESPUESTA DEVUELTA POR GEMINI:")
    print(repr(respuesta_texto))
    print("===================================\n")

    return respuesta.content, documentos_usados

if __name__ == "__main__":

    while True:

        pregunta = input("\nPregunta (o escribí 'salir'): ")

        if pregunta.lower() == "salir":
            break

        respuesta, fuentes = preguntar(pregunta)

        print("\nRespuesta:")
        print(respuesta)

        print("\nFuentes:")
        for fuente in fuentes:
            print("-", fuente)