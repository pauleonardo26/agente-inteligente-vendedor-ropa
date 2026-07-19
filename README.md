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

 Ejecución del Programa

## Requisitos previos

Antes de ejecutar el **Agente Inteligente Vendedor de Ropa**, es necesario contar con los siguientes requisitos:

- Python 3.10 o superior.
- Entorno virtual configurado.
- Dependencias del proyecto instaladas.
- API Key de Google Gemini configurada.
- Archivo `inventario.csv` disponible dentro de la estructura del proyecto.

---

## Activación del entorno virtual

Se recomienda utilizar un entorno virtual para mantener organizadas las dependencias del proyecto.

### Windows

```bash
venv\Scripts\activate
```

### Linux / MacOS

```bash
source venv/bin/activate
```

---

## Instalación de dependencias

Con el entorno virtual activo, ejecutar el siguiente comando:

```bash
pip install -r requirements.txt
```

Este comando instala las librerías necesarias para ejecutar el agente:

- LangChain.
- LangGraph.
- Google Gemini.
- Pandas.
- Librerías complementarias del proyecto.

---

## Configuración de Google Gemini

El proyecto utiliza **Google Gemini 2.5 Flash** como modelo de lenguaje.

Para permitir la comunicación con Gemini es necesario configurar la API Key.

### Windows

```bash
set GOOGLE_API_KEY="TU_API_KEY"
```

### Linux / MacOS

```bash
export GOOGLE_API_KEY="TU_API_KEY"
```

La API Key permite que el agente pueda enviar consultas al modelo Gemini y recibir respuestas generadas por inteligencia artificial.

---

# Inicio del agente

Después de configurar el entorno, ejecutar el archivo principal del proyecto:

```bash
python agente_ia_challenge.py
```

Si la configuración es correcta, el sistema iniciará el agente inteligente y quedará preparado para recibir consultas sobre el inventario de ropa.

---

# Ejemplo de ejecución

```text
=========================================
 Agente Inteligente Vendedor de Ropa
=========================================

Sistema iniciado correctamente.

Realiza una consulta sobre los productos disponibles.
```

---

# Ejemplos de conversación

## Consulta general de productos

### Usuario

```text
¿Qué productos tienes disponibles?
```

### Agente

```text
Tengo disponibles los siguientes productos:

- Polo niño avenger
  Categoría: Ropa niño
  Talla: 4
  Precio: S/35
  Stock: 20 unidades

- Polo niño spiderman
  Categoría: Ropa niño
  Talla: 6
  Precio: S/38
  Stock: 15 unidades

- Conjunto niño deportivo
  Categoría: Ropa niño
  Talla: 8
  Precio: S/65
  Stock: 10 unidades
```

---

## Consulta por talla

### Usuario

```text
¿Tienes ropa para niño talla 10?
```

### Agente

```text
Sí, encontré un producto disponible:

Producto:
Casaca niño invierno

Categoría:
Ropa niño

Talla:
10

Precio:
S/75

Stock:
8 unidades
```

---

## Consulta de stock

### Usuario

```text
¿Cuánto stock queda del pantalón jean niño?
```

### Agente

```text
El producto encontrado es:

Producto:
Pantalón niño jean

Categoría:
Ropa niño

Talla:
12

Precio:
S/50

Stock disponible:
12 unidades
```

---

# Finalizar la ejecución

Para detener la ejecución del agente durante una sesión activa:

```bash
Ctrl + C
```

El programa finalizará la sesión actual.

---

# Flujo de ejecución del agente

El proceso completo de una consulta funciona de la siguiente manera:

```text
Usuario realiza una pregunta
          |
          ↓
El agente interpreta la consulta
          |
          ↓
Evalúa si necesita consultar información
          |
          ↓
Ejecuta la Tool de consulta
          |
          ↓
Pandas procesa el archivo inventario.csv
          |
          ↓
Obtiene la información del producto
          |
          ↓
Gemini genera una respuesta en lenguaje natural
          |
          ↓
Usuario recibe la respuesta
```

---

# Resumen

La ejecución del proyecto permite interactuar con un agente inteligente capaz de responder preguntas sobre productos de ropa utilizando información real almacenada en el archivo:

```
inventario.csv
```

El agente combina:

- Google Gemini 2.5 Flash para la generación de respuestas.
- LangChain para la construcción del agente.
- LangGraph para administrar el flujo.
- Pandas para consultar los datos del inventario.

De esta manera, el sistema puede interpretar consultas en lenguaje natural y entregar información del inventario de forma automática.

------------------------------------------

# 🔑 Configuración de Google Gemini

Para que el **Agente Inteligente Vendedor de Ropa** pueda comprender las consultas del usuario y generar respuestas en lenguaje natural, es necesario configurar una API Key de Google Gemini.

La API Key permite autenticar la aplicación y establecer una comunicación segura con el modelo de lenguaje.

> **Importante:** Nunca compartas tu API Key ni la publiques en un repositorio público de GitHub.

---

# Obtener una API Key

La API Key puede obtenerse desde **Google AI Studio**.

El proceso general es el siguiente:

1. Iniciar sesión con una cuenta de Google.
2. Acceder a Google AI Studio.
3. Crear una nueva API Key.
4. Copiar la clave generada.
5. Guardarla en un lugar seguro.

Una vez obtenida, podrá utilizarse para autenticar las solicitudes realizadas al modelo Gemini.

---

# Configuración en Google Colab

Durante el desarrollo de este Challenge, la API Key se configuró utilizando las herramientas disponibles en Google Colab.

La clave se almacenó como un secreto del entorno y posteriormente fue leída desde el notebook para evitar escribirla directamente en el código.

Este método ofrece una mayor seguridad, ya que la clave permanece protegida y no forma parte del repositorio.

---

# Configuración mediante variables de entorno

En proyectos ejecutados de forma local, una práctica habitual consiste en utilizar variables de entorno.

De esta manera, la API Key permanece fuera del código fuente y puede cambiarse sin modificar la aplicación.

Este enfoque mejora la seguridad y facilita la administración de credenciales en diferentes entornos.

---

# Inicialización del modelo

Una vez configurada la API Key, el proyecto crea una instancia del modelo Google Gemini.

A partir de ese momento, el agente puede enviar consultas al modelo de lenguaje y recibir respuestas generadas mediante Inteligencia Artificial.

La inicialización del modelo constituye uno de los primeros pasos del flujo de ejecución del proyecto.

---

# Integración con LangChain

Después de inicializar Gemini, el modelo se integra con LangChain.

Esta integración permite que el agente:

- Comprenda preguntas formuladas en lenguaje natural.
- Utilice herramientas cuando sea necesario.
- Razone antes de responder.
- Genere respuestas claras y coherentes.

LangChain actúa como intermediario entre el modelo de lenguaje y el resto de componentes del sistema.

---

# Flujo de autenticación

El proceso completo puede resumirse mediante el siguiente diagrama:

```text
Google AI Studio
        │
        ▼
Generación de API Key
        │
        ▼
Almacenamiento seguro
        │
        ▼
Inicialización de Gemini
        │
        ▼
Integración con LangChain
        │
        ▼
Creación del Agente
        │
        ▼
Consultas del Usuario
```

---

# Buenas prácticas de seguridad

Durante el desarrollo de aplicaciones basadas en Modelos de Lenguaje es recomendable seguir algunas medidas de seguridad:

- No publicar la API Key en GitHub.
- No escribir la clave directamente dentro del código fuente.
- Utilizar variables de entorno o sistemas de gestión de secretos.
- Revocar la clave inmediatamente si se sospecha que ha sido expuesta.
- Crear nuevas credenciales cuando sea necesario.

Estas prácticas ayudan a proteger el acceso al modelo y evitan el uso no autorizado de la API.

---

# Consideraciones importantes

El funcionamiento del agente depende de una conexión válida con Google Gemini.

Si la API Key no está configurada correctamente o presenta algún problema, el agente no podrá generar respuestas.

Asimismo, es posible que existan límites de uso asociados a la cuenta o al plan disponible en Google AI Studio, por lo que conviene revisar periódicamente la documentación oficial y el consumo de la API.

---

# Resultado esperado

Una vez completada la configuración:

- El modelo Google Gemini quedará correctamente inicializado.
- LangChain podrá comunicarse con el modelo.
- El agente estará preparado para interpretar consultas.
- Las herramientas podrán utilizarse cuando sea necesario.
- El sistema estará listo para ejecutar conversaciones sobre el inventario de ropa.

La siguiente sección muestra cómo ejecutar el proyecto y presenta ejemplos de interacción con el agente.

-------------------------------------------


 Funcionamiento Interno del Agente

El **Agente Inteligente Vendedor de Ropa** utiliza una arquitectura basada en agentes de inteligencia artificial que permite interpretar consultas realizadas en lenguaje natural y responder utilizando información real almacenada en un inventario.

El sistema integra:

- Google Gemini 2.5 Flash como modelo de lenguaje.
- LangChain para la construcción del agente.
- LangGraph para controlar el flujo de ejecución.
- ReAct como patrón de razonamiento y acción.
- Tools para ejecutar tareas específicas.
- Pandas para procesar el archivo `inventario.csv`.

---

# Flujo interno del agente

Cuando un usuario realiza una consulta, el agente sigue el siguiente proceso:

```text
Usuario
   |
   ↓
Pregunta en lenguaje natural
   |
   ↓
Agente inteligente basado en ReAct
   |
   ↓
LangGraph administra el flujo
   |
   ↓
El agente decide si necesita utilizar una herramienta
   |
   ↓
Tool consulta inventario.csv
   |
   ↓
Pandas procesa los datos
   |
   ↓
Información del producto encontrada
   |
   ↓
Gemini genera la respuesta final
   |
   ↓
Usuario recibe la información
```

---

# Arquitectura del agente

El funcionamiento del sistema está basado en la interacción entre diferentes componentes especializados.

## Componentes principales

| Componente | Función |
|---|---|
| Google Gemini 2.5 Flash | Comprensión del lenguaje y generación de respuestas |
| LangChain | Creación y configuración del agente |
| LangGraph | Organización del flujo de ejecución |
| ReAct | Razonamiento y selección de acciones |
| Tool | Consulta de información del inventario |
| Pandas | Lectura y procesamiento del archivo CSV |

---

# LangGraph

## ¿Qué es LangGraph?

LangGraph es un framework utilizado para construir aplicaciones basadas en agentes mediante una estructura de grafos.

Un grafo permite representar un proceso mediante:

- Estados.
- Nodos.
- Conexiones.
- Transiciones.

Esto permite controlar de manera organizada cómo el agente recibe información, toma decisiones y ejecuta acciones.

---

## Función de LangGraph dentro del proyecto

En este proyecto, LangGraph administra el ciclo de ejecución del agente.

El flujo general es:

```text
Inicio
  |
  ↓
Recibir consulta del usuario
  |
  ↓
Procesar información con el agente
  |
  ↓
Evaluar necesidad de consulta
  |
  ↓
Ejecutar herramienta disponible
  |
  ↓
Obtener información del inventario
  |
  ↓
Generar respuesta
  |
  ↓
Finalizar proceso
```

LangGraph permite conectar el modelo Gemini con las herramientas necesarias para resolver la consulta del usuario.

---

# Patrón ReAct

## ¿Qué es ReAct?

ReAct significa:

```
Reasoning + Acting
```

(Razonamiento + Acción)

Es un patrón utilizado en agentes de inteligencia artificial donde el modelo puede analizar una consulta, decidir una acción y utilizar herramientas antes de responder.

---

## Funcionamiento de ReAct

En lugar de responder directamente, el agente realiza un proceso de análisis:

Ejemplo:

### Consulta del usuario

```text
¿Tienes polos para niño talla 6?
```

---

### Proceso interno del agente

```text
Analizar consulta:

El usuario necesita información de productos.

↓

Decisión:

Necesito consultar el inventario.

↓

Acción:

Utilizar la herramienta de consulta.

↓

Resultado:

Encontrar productos disponibles.

↓

Respuesta:

Informar al usuario sobre el producto.
```

---

# create_react_agent()

## ¿Qué es create_react_agent()?

`create_react_agent()` es una función utilizada para crear un agente basado en el patrón ReAct.

Esta función permite conectar:

- Modelo de lenguaje.
- Herramientas disponibles.
- Instrucciones del agente.
- Flujo de razonamiento y acciones.

---

## Función dentro del proyecto

Dentro del Agente Inteligente Vendedor de Ropa permite:

- Crear el agente inteligente.
- Asociar Google Gemini como modelo de lenguaje.
- Registrar la herramienta de consulta del inventario.
- Permitir que el agente decida cuándo utilizar la herramienta.
- Generar respuestas utilizando los datos obtenidos.

---

## Funcionamiento conceptual

```text
Pregunta del usuario

        ↓

Agente creado con create_react_agent()

        ↓

Analiza la consulta

        ↓

Selecciona herramienta necesaria

        ↓

Obtiene información

        ↓

Genera respuesta final
```

---

# PromptTemplate

## ¿Qué es PromptTemplate?

`PromptTemplate` es una herramienta de LangChain que permite crear instrucciones estructuradas para el modelo de inteligencia artificial.

Estas instrucciones ayudan a definir el comportamiento esperado del agente.

---

## Uso dentro del proyecto

El PromptTemplate permite indicarle al agente aspectos como:

- Su rol como vendedor de ropa.
- Cómo debe utilizar la información del inventario.
- Qué tipo de respuestas debe entregar.
- Evitar generar información que no existe.

---

## Ejemplo conceptual

```text
Eres un asistente vendedor de ropa.

Tu función es ayudar al usuario
consultando únicamente los productos
disponibles en el inventario.

Si un producto no existe,
indica que no está disponible.
```

---

# Tool de consulta de inventario

## ¿Qué es una Tool?

Una Tool es una herramienta que el agente puede utilizar para realizar una acción específica.

En este proyecto existe una herramienta encargada de consultar la información del archivo:

```text
inventario.csv
```

---

## Función de la Tool

La herramienta permite obtener información como:

- Nombre del producto.
- Categoría.
- Talla.
- Precio.
- Stock disponible.

---

## Flujo de utilización de la Tool

```text
Usuario:

¿Qué casacas tienes disponibles?

        ↓

Agente analiza la consulta

        ↓

Decide utilizar la Tool

        ↓

Tool consulta inventario.csv

        ↓

Encuentra información:

Casaca niño invierno
Talla 10
Precio S/75
Stock 8

        ↓

Gemini genera respuesta
```

---

# Consulta del inventario mediante Pandas

## ¿Qué es Pandas?

Pandas es una librería de Python utilizada para manipular, analizar y procesar datos.

En este proyecto se utiliza para leer y consultar la información almacenada en el archivo CSV.

---

## Lectura del archivo CSV

Ejemplo:

```python
import pandas as pd

inventario = pd.read_csv("inventario.csv")
```

Después de cargar el archivo, los datos pueden ser filtrados según la consulta realizada por el usuario.

---

# Estructura del inventario

El archivo `inventario.csv` contiene los siguientes campos:

| Campo | Descripción |
|---|---|
| Producto | Nombre del artículo |
| Categoría | Tipo de producto |
| Talla | Talla disponible |
| Precio | Valor del producto |
| Stock | Cantidad disponible |

---

# Ejemplo de consulta con Pandas

Consulta del usuario:

```text
Buscar ropa niño talla 8
```

Proceso:

```text
Filtrar inventario:

Categoría = Ropa niño

Talla = 8
```

Resultado obtenido:

```text
Producto:
Conjunto niño deportivo

Precio:
S/65

Stock:
10 unidades
```

---

# Resumen del funcionamiento técnico

El agente funciona mediante la integración de los siguientes elementos:

```text
Usuario
  ↓
Agente ReAct
  ↓
LangGraph
  ↓
create_react_agent()
  ↓
Tool de consulta
  ↓
Pandas
  ↓
inventario.csv
  ↓
Gemini 2.5 Flash
  ↓
Respuesta final
```

Esta arquitectura permite construir un agente inteligente capaz de comprender preguntas en lenguaje natural y responder utilizando información real del inventario disponible.

--------------------------------------------------------------

 Autor, Agradecimientos y Licencia

 Autor

Proyecto desarrollado por:

**Paul Leonardo Vilela Chacaltana**

Como parte del **Challenge Oracle Next Education (ONE)**, aplicando conocimientos de inteligencia artificial, agentes inteligentes y automatización.

---

Descripción del desarrollo

Durante la elaboración de este proyecto se utilizaron diferentes herramientas de aprendizaje y apoyo técnico.

El desarrollo del agente, la configuración de tecnologías, las pruebas de funcionamiento y la investigación de conceptos fueron realizados como parte del proceso de aprendizaje del Challenge ONE.

---

 Herramientas de apoyo utilizadas

 ChatGPT como asistente de aprendizaje y documentación

Durante todo el desarrollo del proyecto se utilizó **ChatGPT como herramienta de apoyo** para:

- Comprender conceptos técnicos relacionados con inteligencia artificial.
- Analizar errores durante la programación.
- Revisar la estructura del proyecto.
- Mejorar la documentación técnica.
- Organizar y redactar el archivo `README.md`.
- Explicar tecnologías utilizadas como:
  - LangChain.
  - LangGraph.
  - ReAct.
  - Google Gemini.
  - Pandas.
  - Agentes inteligentes.

ChatGPT fue utilizado como un asistente de consulta y aprendizaje, ayudando a comprender los conceptos y mejorar la presentación final del proyecto.

---

 Agradecimientos

Oracle Next Education (ONE)

Agradecimiento especial a **Oracle Next Education (ONE)** por brindar una ruta de aprendizaje enfocada en tecnología, programación e innovación, permitiendo desarrollar soluciones utilizando herramientas actuales de inteligencia artificial.

---

 Tecnologías utilizadas

Agradecimiento a los equipos responsables de crear y mantener las tecnologías utilizadas en este proyecto:

- Google Gemini.
- LangChain.
- LangGraph.
- Pandas.
- Python.
- Oracle Cloud Infrastructure.

Estas herramientas permitieron construir y documentar un agente inteligente funcional.



 Cierre del proyecto

El **Agente Inteligente Vendedor de Ropa** representa la aplicación práctica de conocimientos adquiridos durante el Challenge Oracle Next Education (ONE).

El proyecto integra:

```text
Python
   +
LangChain
   +
LangGraph
   +
Google Gemini 2.5 Flash
   +
Pandas
```

para crear un agente capaz de interpretar consultas en lenguaje natural y responder utilizando información real almacenada en un inventario.

---

# Reflexión final

Este proyecto representa una primera versión de una solución basada en inteligencia artificial aplicada a un escenario comercial.

El aprendizaje obtenido durante su desarrollo permite establecer una base para futuras mejoras, incorporando nuevas tecnologías y ampliando las capacidades del agente inteligente.

---

⭐ **Gracias por visitar este proyecto.**




