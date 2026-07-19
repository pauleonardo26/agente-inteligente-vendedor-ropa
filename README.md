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

------------------------------------------------

---

# 🏗️ Arquitectura del Proyecto

Este proyecto implementa un **Agente Inteligente Vendedor de Ropa** utilizando una arquitectura basada en agentes (Agentic AI). En lugar de responder únicamente con texto generado por un modelo de lenguaje, el agente es capaz de decidir cuándo necesita consultar información externa para construir una respuesta más precisa.

La solución integra un modelo de lenguaje de Google Gemini con LangChain y LangGraph, utilizando herramientas (Tools) que permiten acceder al inventario de productos almacenado en un archivo CSV.

La arquitectura fue diseñada para ser modular, facilitando futuras ampliaciones sin modificar el funcionamiento principal del agente.

## Arquitectura general

```text
                        Usuario
                           │
                           ▼
              Consulta sobre una prenda
                           │
                           ▼
          Google Gemini 2.5 Flash (LLM)
                           │
                           ▼
         create_react_agent() - LangChain
                           │
                           ▼
            LangGraph (Control del flujo)
                           │
          ┌────────────────┴────────────────┐
          │                                 │
          ▼                                 ▼
 Analiza la consulta              Decide si usar una Tool
                                            │
                                            ▼
                          Consultar Inventario
                                 (Tool)
                                            │
                                            ▼
                               Pandas
                                            │
                                            ▼
                               inventario.csv
                                            │
                                            ▼
                          Información encontrada
                                            │
                                            ▼
                     Respuesta generada por Gemini
                                            │
                                            ▼
                                  Usuario
```

## Componentes principales

### Usuario

Es quien interactúa con el sistema realizando preguntas relacionadas con los productos disponibles, por ejemplo:

- ¿Tienen polos negros?
- ¿Qué talla hay disponible?
- ¿Cuánto cuesta este producto?
- ¿Qué prendas tienen en stock?

El usuario no necesita conocer cómo funciona internamente el sistema; simplemente conversa con el agente de manera natural.

---

### Modelo de Lenguaje (Google Gemini 2.5 Flash)

Google Gemini es el responsable de comprender la intención del usuario, interpretar la consulta y redactar una respuesta clara y natural.

Sin embargo, el modelo no inventa la información del inventario. Cuando necesita datos reales, utiliza una herramienta para consultarlos antes de responder.

---

### LangChain

LangChain actúa como la capa de integración entre el modelo de lenguaje y las herramientas disponibles.

Permite definir el comportamiento del agente, registrar herramientas, construir prompts y gestionar la comunicación con el modelo de IA.

---

### create_react_agent()

El agente fue construido utilizando la función `create_react_agent()`.

Esta implementación sigue el patrón **ReAct (Reason + Act)**, donde el modelo:

1. Analiza la pregunta.
2. Decide si necesita consultar información.
3. Ejecuta la herramienta correspondiente.
4. Analiza el resultado obtenido.
5. Genera la respuesta final para el usuario.

Este enfoque permite respuestas más precisas y fundamentadas en datos reales.

---

### LangGraph

LangGraph coordina el flujo completo del agente.

Su función principal es organizar las distintas etapas del proceso, controlar la ejecución de herramientas y mantener un flujo estructurado entre el razonamiento del modelo y las acciones realizadas.

Gracias a esta arquitectura, el proyecto puede crecer fácilmente incorporando nuevas herramientas o funcionalidades.

---

### Tool: Consulta del Inventario

El agente dispone de una herramienta especializada cuya responsabilidad es consultar el inventario de productos.

Cuando el modelo detecta que necesita información sobre disponibilidad, tallas, colores, precios o stock, activa esta herramienta para obtener los datos directamente desde el archivo CSV.

De esta manera, las respuestas se basan en información actualizada y no en conocimiento generado por el modelo.

---

### Pandas

Pandas se utiliza para cargar y procesar el archivo `inventario.csv`.

Esta biblioteca facilita la lectura, búsqueda y filtrado de datos, permitiendo localizar rápidamente los productos que cumplen con los criterios solicitados por el usuario.

---

### Archivo inventario.csv

El archivo `inventario.csv` constituye la fuente de datos del proyecto.

En él se almacena el catálogo de prendas disponibles con información como:

- Nombre del producto
- Categoría
- Talla
- Color
- Precio
- Stock disponible

El agente consulta este archivo cada vez que necesita responder preguntas relacionadas con el inventario.

---

## Beneficios de esta arquitectura

Esta arquitectura ofrece diversas ventajas:

- Separación entre el razonamiento y el acceso a los datos.
- Respuestas basadas en información real del inventario.
- Código modular y fácil de mantener.
- Facilidad para incorporar nuevas herramientas.
- Escalabilidad para futuras integraciones.
- Organización clara del flujo de ejecución mediante LangGraph.
- Uso de tecnologías modernas de Inteligencia Artificial Generativa.

- ----------------------------------------

---

# 📁 Estructura del Proyecto

Una buena organización de archivos facilita el mantenimiento del código, mejora la legibilidad y permite que otros desarrolladores comprendan rápidamente el funcionamiento del proyecto.

La estructura utilizada en este Challenge es la siguiente:

```text
Agente-Inteligente-Vendedor-de-Ropa/
│
├── inventario.csv
├── main.py
├── requirements.txt
├── README.md
│
└── (archivos auxiliares del proyecto)
```

> **Nota:** La estructura puede ampliarse en futuras versiones incorporando nuevos módulos, herramientas o carpetas específicas sin afectar el funcionamiento principal del agente.

---

# Descripción de los archivos

## 📄 main.py

Es el archivo principal del proyecto.

Desde este archivo se inicia la aplicación y se configura el funcionamiento general del agente inteligente.

Entre sus responsabilidades se encuentran:

- Inicializar el modelo Google Gemini.
- Configurar LangChain.
- Crear el agente mediante `create_react_agent()`.
- Registrar las herramientas disponibles.
- Ejecutar el flujo controlado por LangGraph.
- Recibir las consultas del usuario.
- Mostrar las respuestas generadas.

En otras palabras, **main.py** es el punto de entrada de toda la aplicación.

---

## 📊 inventario.csv

Este archivo almacena el inventario de prendas de vestir que el agente utiliza como fuente de información.

Cada fila representa un producto disponible y cada columna contiene una característica relevante, como:

- Nombre del producto.
- Categoría.
- Talla.
- Color.
- Precio.
- Stock disponible.

Gracias a este enfoque, la información puede actualizarse modificando únicamente el archivo CSV, sin necesidad de cambiar el código del agente.

---

## 📦 requirements.txt

Este archivo reúne todas las dependencias necesarias para ejecutar el proyecto.

Permite instalar fácilmente las bibliotecas utilizadas mediante un único comando, garantizando que otros desarrolladores puedan reproducir el mismo entorno de trabajo.

Entre las principales dependencias se incluyen:

- Python
- LangChain
- LangGraph
- Pandas
- Google Generative AI

---

## 📘 README.md

Este documento describe el proyecto de forma completa.

Incluye información sobre:

- Objetivos.
- Arquitectura.
- Tecnologías utilizadas.
- Instalación.
- Configuración.
- Ejecución.
- Ejemplos de uso.
- Mejoras futuras.
- Licencia.

Su finalidad es servir como guía para cualquier persona interesada en comprender, ejecutar o colaborar con el proyecto.

---

# Organización lógica del sistema

Aunque el proyecto es compacto, internamente puede entenderse como la interacción de varios componentes especializados:

```text
Usuario
   │
   ▼
main.py
   │
   ▼
Agente Inteligente
   │
   ├──────────────► Modelo Gemini
   │
   ├──────────────► PromptTemplate
   │
   ├──────────────► create_react_agent()
   │
   ├──────────────► LangGraph
   │
   └──────────────► Tool
                      │
                      ▼
                  Pandas
                      │
                      ▼
               inventario.csv
```

Cada componente cumple una función específica dentro del flujo del agente, favoreciendo una arquitectura clara, organizada y preparada para futuras ampliaciones.

---

# Diseño modular

Uno de los principios aplicados en este proyecto es la modularidad.

Cada tecnología cumple un propósito bien definido:

- **Gemini** interpreta y genera respuestas.
- **LangChain** conecta el modelo con las herramientas.
- **LangGraph** coordina el flujo de ejecución.
- **PromptTemplate** organiza las instrucciones enviadas al modelo.
- **Pandas** procesa el inventario.
- **inventario.csv** almacena la información de los productos.

Esta separación de responsabilidades facilita el mantenimiento del código y permite incorporar nuevas funcionalidades sin alterar la lógica principal del agente.

-------------------------------------------------------

---

# 🔄 Flujo de Funcionamiento del Agente

Uno de los aspectos más importantes de este proyecto es comprender cómo fluye la información desde que el usuario realiza una consulta hasta que recibe una respuesta generada por el agente.

A diferencia de una aplicación tradicional, donde las respuestas suelen estar programadas manualmente, este sistema combina el razonamiento de un Modelo de Lenguaje (LLM) con herramientas capaces de consultar información real del inventario.

El proceso completo puede dividirse en varias etapas.

---

# Paso 1. El usuario realiza una consulta

Todo comienza cuando el usuario escribe una pregunta relacionada con las prendas disponibles.

Por ejemplo:

- ¿Tienen polos negros?
- ¿Qué talla hay del polo deportivo?
- ¿Cuánto cuesta la casaca azul?
- ¿Qué productos tienen stock?

El usuario interactúa con el agente utilizando lenguaje natural, sin necesidad de emplear comandos especiales.

---

# Paso 2. La consulta llega al agente

La pregunta es recibida por el agente creado mediante `create_react_agent()`.

En esta etapa, el agente analiza la intención del usuario para determinar qué información necesita antes de responder.

No todas las consultas requieren acceder al inventario. El agente decide cuándo es necesario utilizar una herramienta y cuándo puede responder directamente.

---

# Paso 3. El modelo razona

Google Gemini interpreta la consulta utilizando el contexto proporcionado por el PromptTemplate.

Durante este proceso el modelo analiza aspectos como:

- Qué está preguntando el usuario.
- Qué información necesita obtener.
- Si debe consultar datos externos.
- Cómo estructurar la respuesta final.

Este razonamiento ocurre antes de generar la respuesta.

---

# Paso 4. Decisión de utilizar una herramienta

Si el agente identifica que necesita información del inventario, activa la herramienta encargada de realizar la consulta.

Este comportamiento corresponde al patrón **ReAct (Reason + Act)**:

1. Razonar.
2. Decidir.
3. Ejecutar una acción.
4. Analizar el resultado.
5. Responder.

Gracias a este enfoque, el agente no depende únicamente del conocimiento del modelo, sino también de datos reales.

---

# Paso 5. Consulta del inventario

La herramienta utiliza Pandas para leer el archivo `inventario.csv`.

Dependiendo de la consulta realizada, puede buscar información como:

- Productos disponibles.
- Colores.
- Tallas.
- Precios.
- Stock.

El resultado obtenido se devuelve al agente para que continúe con el proceso.

---

# Paso 6. Interpretación de los datos

Una vez obtenida la información del inventario, el modelo analiza los resultados.

En esta etapa no solo presenta los datos encontrados, sino que también los organiza en una respuesta clara y comprensible para el usuario.

Por ejemplo, si existen varias prendas que cumplen con la búsqueda, el agente puede resumir la información en una respuesta natural.

---

# Paso 7. Generación de la respuesta

Finalmente, Google Gemini redacta la respuesta utilizando tanto el razonamiento del modelo como la información obtenida desde el inventario.

El objetivo es ofrecer respuestas útiles, coherentes y basadas en datos reales.

---

# Diagrama del flujo completo

```text
Usuario
   │
   ▼
Escribe una consulta
   │
   ▼
PromptTemplate
   │
   ▼
Google Gemini 2.5 Flash
   │
   ▼
create_react_agent()
   │
   ▼
LangGraph controla el flujo
   │
   ▼
¿Necesita consultar datos?
   │
   ├──────── No ─────────► Respuesta al usuario
   │
   └──────── Sí
             │
             ▼
      Tool de consulta
             │
             ▼
          Pandas
             │
             ▼
      inventario.csv
             │
             ▼
 Información recuperada
             │
             ▼
 Google Gemini interpreta
             │
             ▼
Respuesta final
             │
             ▼
Usuario
```

---

# Ventajas de este flujo

La arquitectura implementada proporciona varios beneficios:

- El agente responde utilizando información actualizada.
- Se evita depender exclusivamente del conocimiento del modelo.
- La lógica del sistema permanece organizada y modular.
- Es posible incorporar nuevas herramientas sin modificar el flujo principal.
- La consulta al inventario se realiza únicamente cuando es necesaria, optimizando el funcionamiento del agente.

Este diseño representa una aproximación moderna al desarrollo de agentes inteligentes, combinando razonamiento, acceso a datos y generación de lenguaje natural en un único flujo de trabajo.

-------------------------------------------

---

# 🛠️ Tecnologías Utilizadas

El desarrollo de este proyecto combina diferentes tecnologías y bibliotecas orientadas a la construcción de aplicaciones basadas en Inteligencia Artificial Generativa.

Cada una cumple una función específica dentro de la arquitectura del agente.

---

# Python

**Python** es el lenguaje de programación utilizado para desarrollar todo el proyecto.

Fue elegido por su sintaxis sencilla, su amplia comunidad y la gran cantidad de bibliotecas disponibles para ciencia de datos e Inteligencia Artificial.

En este proyecto Python se utiliza para:

- Construir el agente inteligente.
- Procesar la información del inventario.
- Integrar todas las bibliotecas utilizadas.
- Ejecutar el flujo completo de la aplicación.

---

# LangChain

LangChain es el framework que permite desarrollar aplicaciones basadas en Modelos de Lenguaje (LLM).

Su función principal consiste en conectar el modelo de IA con herramientas externas y organizar la interacción entre ambos.

Dentro del proyecto, LangChain permite:

- Integrar Google Gemini.
- Crear el agente inteligente.
- Registrar herramientas (Tools).
- Gestionar la comunicación entre el modelo y las funciones del programa.
- Facilitar una arquitectura modular y extensible.

---

# LangGraph

LangGraph complementa a LangChain proporcionando una forma estructurada de controlar el flujo de ejecución del agente.

En lugar de ejecutar todas las acciones de manera lineal, LangGraph organiza el proceso en diferentes etapas, permitiendo decidir qué acción ejecutar en cada momento.

En este proyecto LangGraph se utiliza para:

- Coordinar el flujo del agente.
- Controlar el uso de herramientas.
- Gestionar el razonamiento antes y después de consultar el inventario.
- Mantener una arquitectura preparada para futuras ampliaciones.

---

# Google Gemini 2.5 Flash

Google Gemini 2.5 Flash es el Modelo de Lenguaje (LLM) utilizado por el agente.

Es el encargado de comprender las preguntas realizadas por el usuario y generar respuestas en lenguaje natural.

Su función dentro del proyecto incluye:

- Interpretar consultas.
- Analizar la intención del usuario.
- Decidir cuándo utilizar una herramienta.
- Generar respuestas claras y coherentes.
- Integrar la información recuperada desde el inventario.

El modelo no almacena el inventario dentro de su conocimiento; únicamente utiliza la información obtenida mediante las herramientas disponibles.

---

# Pandas

Pandas es la biblioteca utilizada para manipular y consultar datos estructurados.

En este proyecto permite cargar el archivo `inventario.csv` y realizar búsquedas de forma eficiente.

Entre sus funciones destacan:

- Leer archivos CSV.
- Filtrar productos.
- Consultar precios.
- Buscar tallas disponibles.
- Verificar el stock.
- Organizar la información antes de enviarla al agente.

---

# PromptTemplate

PromptTemplate permite definir la estructura de las instrucciones enviadas al modelo de lenguaje.

Gracias a esta herramienta, el agente recibe un contexto organizado que mejora la calidad de las respuestas.

En este proyecto se utiliza para:

- Definir el comportamiento del agente.
- Establecer el contexto de la conversación.
- Guiar la interpretación de las consultas.
- Mantener consistencia en las respuestas generadas.

---

# create_react_agent()

La función `create_react_agent()` se utiliza para construir el agente inteligente siguiendo el patrón **ReAct (Reason + Act)**.

Este patrón permite que el modelo:

1. Analice la consulta.
2. Razone sobre la información necesaria.
3. Decida si debe utilizar una herramienta.
4. Ejecute la herramienta correspondiente.
5. Interprete el resultado.
6. Genere la respuesta final.

Gracias a este enfoque, el agente puede combinar razonamiento e información real del inventario.

---

# inventario.csv

El archivo `inventario.csv` constituye la base de conocimiento del proyecto.

Contiene la información de los productos disponibles y es consultado dinámicamente por el agente.

Entre los datos almacenados se encuentran:

- Producto.
- Categoría.
- Talla.
- Color.
- Precio.
- Stock.

Al mantener la información separada del código, es posible actualizar el inventario simplemente modificando el archivo CSV.

---

# Integración entre tecnologías

Todas las tecnologías trabajan de forma coordinada para ofrecer una experiencia de consulta inteligente.

El flujo de integración puede representarse de la siguiente manera:

```text
Python
   │
   ▼
LangChain
   │
   ▼
create_react_agent()
   │
   ▼
LangGraph
   │
   ▼
Google Gemini
   │
   ▼
Tool de consulta
   │
   ▼
Pandas
   │
   ▼
inventario.csv
   │
   ▼
Respuesta al usuario
```

Cada componente aporta una capacidad específica y, en conjunto, permiten construir un agente capaz de comprender preguntas, consultar información real y responder de manera natural.

---

# ¿Por qué esta combinación de tecnologías?

La elección de estas herramientas responde a la necesidad de construir un agente moderno, modular y escalable.

Esta arquitectura ofrece ventajas como:

- Separación clara de responsabilidades.
- Fácil mantenimiento del código.
- Integración con modelos de lenguaje de última generación.
- Consulta dinámica de información externa.
- Posibilidad de incorporar nuevas herramientas y fuentes de datos en futuras versiones.
- Base sólida para evolucionar hacia aplicaciones más completas, como asistentes de ventas con interfaces web o integraciones con plataformas de mensajería.

-----------------------------------------

---

# ⚙️ Instalación del Proyecto

Esta sección explica cómo preparar el entorno de desarrollo para ejecutar el **Agente Inteligente Vendedor de Ropa**.

El proyecto fue desarrollado utilizando **Python**, **Google Colab** y las bibliotecas LangChain, LangGraph, Google Gemini y Pandas.

## Requisitos previos

Antes de ejecutar el proyecto es necesario contar con los siguientes requisitos:

- Python 3.10 o superior.
- Una cuenta de Google con acceso a Google AI Studio.
- Una API Key de Google Gemini.
- Git (opcional, para clonar el repositorio).
- Conexión a Internet para acceder al modelo de lenguaje.

---

# Clonar el repositorio

Si deseas descargar el proyecto desde GitHub, ejecuta el siguiente comando:


https://github.com/pauleonardo26/agente-inteligente-vendedor-ropa/edit/main/README.md

Luego ingresa a la carpeta del proyecto:

agente-inteligente-vendedor-ropa




# Bibliotecas utilizadas

Las principales dependencias del proyecto son:

| Biblioteca | Función dentro del proyecto |
|------------|-----------------------------|
| Python | Lenguaje principal del proyecto |
| LangChain | Construcción del agente inteligente |
| LangGraph | Control del flujo del agente |
| Google Generative AI | Conexión con Gemini |
| LangChain Google GenAI | Integración entre LangChain y Gemini |
| Pandas | Lectura y consulta del inventario CSV |

---

# Archivo del inventario

El proyecto utiliza un archivo denominado:

```text
inventario.csv
```

Este archivo contiene la información que el agente consulta para responder preguntas relacionadas con los productos.

Debe permanecer en la carpeta principal del proyecto (o en la ruta definida dentro del código) para que el agente pueda acceder correctamente a los datos.

---

# Verificación de la instalación

Antes de ejecutar el agente, verifica que:

- Python esté correctamente instalado.
- Todas las bibliotecas se hayan instalado sin errores.
- El archivo `inventario.csv` esté disponible.
- La API Key de Google Gemini esté configurada.
- Exista conexión a Internet.

Si todos estos requisitos se cumplen, el proyecto estará listo para ejecutarse.

---

# Entorno utilizado durante el desarrollo

Este Challenge fue desarrollado principalmente utilizando **Google Colab**, lo que permitió ejecutar el proyecto directamente desde el navegador sin necesidad de instalar un entorno de desarrollo local.

Google Colab facilitó:

- La instalación de bibliotecas mediante `pip`.
- La ejecución interactiva del código.
- La organización del proyecto en celdas.
- La integración con Google Gemini mediante una API Key.

Gracias a este entorno, fue posible desarrollar y probar el agente de forma rápida y sencilla.

---

# Preparación del entorno

Una vez completados todos los pasos anteriores, el proyecto queda listo para configurar la conexión con Google Gemini y ejecutar el agente inteligente.

En la siguiente sección se explica cómo obtener y configurar la API Key necesaria para establecer la comunicación con el modelo de lenguaje.

------------------------------------------








--------------------------------------------------------

