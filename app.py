import streamlit as st
import pandas as pd

from langchain.tools import Tool
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



def consultar_inventario(pregunta: str) -> str:
    """
    Devuelve el contenido completo del inventario para que el modelo
    responda únicamente utilizando esa información.
    """
    return df.to_string(index=False)

herramienta_inventario = Tool(
    name="Inventario",
    func=consultar_inventario,
    description="""
    Utiliza esta herramienta para consultar el inventario de ropa.
    Contiene productos, categorías, tallas, precios y stock.
    """
)



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
    tools=[herramienta_inventario]
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

            mensaje = respuesta["messages"][-1].content

        st.success("Respuesta")

        st.write(mensaje)



with st.expander("Ver inventario"):

    st.dataframe(
        df,
        use_container_width=True
    )
