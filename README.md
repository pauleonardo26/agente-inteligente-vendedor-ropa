# 👕 Agente Inteligente Vendedor de Ropa

> Challenge Oracle Next Education (ONE) – Especialización en Inteligencia Artificial

![Python](https://img.shields.io/badge/Python-3.x-blue)
![LangChain](https://img.shields.io/badge/LangChain-1.3.x-green)
![LangGraph](https://img.shields.io/badge/LangGraph-1.2.x-orange)
![Gemini](https://img.shields.io/badge/Google-Gemini%202.5%20Flash-red)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-purple)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

---

# Descripción

Este proyecto corresponde al **Challenge Oracle Next Education (ONE)** y consiste en el desarrollo de un **Agente Inteligente Vendedor de Ropa**, construido con tecnologías modernas de Inteligencia Artificial.

El agente utiliza un modelo de lenguaje de Google Gemini, integrado mediante LangChain y orquestado con LangGraph, para comprender las preguntas del usuario, consultar un inventario de productos almacenado en un archivo CSV y generar respuestas útiles y naturales.

A diferencia de un chatbot tradicional basado únicamente en respuestas predefinidas, este agente puede razonar sobre la información disponible y decidir cuándo consultar el inventario antes de responder.

El proyecto fue desarrollado siguiendo una arquitectura basada en agentes (Agentic AI), aplicando el patrón ReAct (Reason + Act), permitiendo separar el razonamiento del modelo de las acciones ejecutadas sobre los datos.

Actualmente el sistema permite consultar información sobre prendas disponibles, incluyendo características como:

- Nombre del producto
- Categoría
- Talla
- Color
- Precio
- Stock disponible

Toda la información es obtenida dinámicamente desde un archivo **inventario.csv**, evitando respuestas estáticas.

---

# Objetivos del proyecto

Los principales objetivos de este Challenge fueron:

- Aplicar conceptos modernos de Inteligencia Artificial Generativa.
- Construir un agente inteligente utilizando LangChain y LangGraph.
- Integrar un modelo LLM de Google Gemini.
- Utilizar herramientas (Tools) para consultar información externa.
- Implementar el patrón ReAct para el razonamiento del agente.
- Leer información desde un archivo CSV utilizando Pandas.
- Generar respuestas útiles basadas en datos reales.
- Comprender la arquitectura de agentes inteligentes moderna.
- Desarrollar un proyecto siguiendo buenas prácticas de organización y documentación.
- Publicar el proyecto en GitHub con una documentación profesional.

---

# Vista general del proyecto

El flujo general del sistema es el siguiente:

```text
Usuario
   │
   ▼
Pregunta sobre una prenda
   │
   ▼
Google Gemini 2.5 Flash
   │
   ▼
LangChain Agent
(create_react_agent)
   │
   ▼
LangGraph
(Control del flujo)
   │
   ▼
Tool
Consultar Inventario
(Pandas)
   │
   ▼
inventario.csv
   │
   ▼
Respuesta generada
   │
   ▼
Usuario
```

---

# Características principales

✔ Agente basado en Inteligencia Artificial.

✔ Arquitectura moderna con LangGraph.

✔ Patrón ReAct (Reason + Act).

✔ Integración con Google Gemini 2.5 Flash.

✔ Consulta dinámica de inventario.

✔ Lectura de datos mediante Pandas.

✔ Respuestas naturales generadas por un LLM.

✔ Proyecto desarrollado completamente en Python.

✔ Código organizado para facilitar futuras ampliaciones.
