# ChallengeAgenteiIABimBamBuy_jorge_Bartra_Corona
AI-powered RAG assistant for answering corporate questions using PDF documents, ChromaDB, Gemini 2.5 Flash and Streamlit.

#  🤖 BimBam Buy AI 

## 📖 Descripción

BimBam Buy AI es un asistente inteligente desarrollado con la arquitectura **Retrieval-Augmented Generation (RAG)**, diseñado para responder consultas sobre documentación empresarial de manera precisa y fundamentada.

El sistema procesa documentos PDF, genera representaciones vectoriales (embeddings) mediante HuggingFace, almacena la información en una base de datos vectorial ChromaDB y utiliza el modelo **Gemini 2.5 Flash** para generar respuestas basadas únicamente en la información recuperada.

La aplicación fue desarrollada en **Python** e implementa una interfaz web con **Streamlit**, permitiendo que los usuarios consulten información de forma simple, rápida e intuitiva.

Este proyecto fue realizado como trabajo académico aplicando tecnologías de Inteligencia Artificial Generativa, Recuperación Aumentada por Generación (RAG) y Procesamiento de Lenguaje Natural (NLP), incluyendo además una propuesta de despliegue sobre **Oracle Cloud Infrastructure (OCI)**.
---

# 🚀 Tecnologías utilizadas

- Python 3.11
- Streamlit
- LangChain
- ChromaDB
- HuggingFace Embeddings
- Google Gemini 2.5 Flash
- PyPDF
- Sentence Transformers

---

# ⚙️ Funcionamiento

El flujo de trabajo del sistema es el siguiente:

1. Carga automática de documentos PDF.
2. Extracción del contenido de los documentos.
3. División del texto en fragmentos (chunks).
4. Generación de embeddings utilizando HuggingFace.
5. Creación de una base vectorial mediante ChromaDB.
6. Recuperación semántica de los fragmentos más relevantes.
7. Generación de respuestas mediante Gemini 2.5 Flash.
8. Presentación de la respuesta y de los documentos utilizados como fuente.

---
---

# 📂 Estructura del proyecto

```text
AgenteBimBamBuy/
│
├── app.py
├── rag.py
├── requirements.txt
├── README.md
├── documentos/
│   ├── documento1.pdf
│   ├── documento2.pdf
│   └── ...
└── .gitignore
```

# ▶️ Instalación

Clonar el repositorio:

```bash
git clone https://github.com/TU-USUARIO/TU-REPOSITORIO.git
```

Ingresar al proyecto:

```bash
cd TU-REPOSITORIO
```

Instalar las dependencias:

```bash
pip install -r requirements.txt
```

---

# ▶️ Ejecución

Iniciar la aplicación con:

```bash
streamlit run app.py
```

Luego abrir en el navegador:

```text
http://localhost:8501
```

---

# ✨ Características

- Consulta inteligente sobre documentos empresariales.
- Recuperación semántica mediante ChromaDB.
- Integración con Gemini 2.5 Flash.
- Interfaz web desarrollada con Streamlit.
- Visualización de las fuentes utilizadas para cada respuesta.
- Arquitectura preparada para despliegue en Oracle Cloud Infrastructure (OCI).

---

# 🎯 Objetivo

El objetivo del proyecto es demostrar la implementación de un asistente conversacional basado en RAG capaz de responder preguntas utilizando exclusivamente la información contenida en documentos empresariales, proporcionando respuestas confiables, trazables y fáciles de consultar.

---

# 👨‍💻 Autor

Proyecto desarrollado como trabajo académico sobre Inteligencia Artificial Generativa y Arquitecturas RAG.



# Explicación <img width="100" height="100" alt="image" src="https://github.com/user-attachments/assets/db84c214-db47-4f2b-9743-b377f9ffdd69" />

El punto 7 presenta la propuesta de despliegue en Oracle Cloud Infrastructure, y

El punto 8 documenta la ejecución y validación funcional del sistema, acompañada por capturas de pantalla como evidencia.
