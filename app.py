import streamlit as st
import pandas as pd


from langchain_core.tools import tool
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.prebuilt import create_react_agent



st.set_page_config(
    page_title="Agente Inteligente Vendedor de Ropa",
    page_icon="🛍️",
    layout="wide"
)

st.title("🛍️ Agente Inteligente Vendedor de Ropa")

st.markdown("""
Este agente responde preguntas utilizando únicamente la información
contenida en el archivo **inventario.csv**.
""")



GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]



llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=GOOGLE_API_KEY,
    temperature=0
)


df = pd.read_csv("inventario.csv")


@tool
def consultar_inventario(pregunta: str) -> str:
    """
    Consulta el inventario de ropa disponible.
    Contiene productos, categorias, tallas, precios y stock.
    """
    return df.to_string(index=False)


    

from langchain_core.tools import tool

@tool
def consultar_inventario(pregunta: str) -> str:
    """
    Consulta el inventario de ropa disponible.
    Contiene productos, categorias, tallas, precios y stock.
    """
    return df.to_string(index=False)
    

prompt = PromptTemplate.from_template("""
Eres un asistente especializado en ventas de ropa.

Responde únicamente utilizando la información obtenida de la herramienta Inventario.

Si la información no existe en el inventario responde:

"No encontré esa información en el inventario."

Pregunta del usuario:

{input}
""")



agent = create_react_agent(
    llm,
    tools=[consultar_inventario]
)


st.subheader("Realiza una consulta")

pregunta = st.text_input(
    "Escribe tu pregunta",
    placeholder="Ejemplo: ¿Qué productos hay disponibles?"
)

if st.button("Consultar"):

    if pregunta.strip() == "":
        st.warning("Ingrese una pregunta.")

    else:

        with st.spinner("Consultando inventario..."):

            respuesta = agent.invoke(
                {
                    "messages": [
                        (
                            "user",
                            prompt.format(input=pregunta)
                        )
                    ]
                }
            )

            contenido = respuesta["messages"][-1].content

            if isinstance(contenido, list):
                mensaje_final = contenido[0]["text"]
            else:
                mensaje_final = contenido

        st.success("Respuesta del agente")
        st.write(mensaje_final)




with st.expander("Ver inventario"):

    st.dataframe(
        df,
        use_container_width=True
    )
