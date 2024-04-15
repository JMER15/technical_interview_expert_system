# Desarrollo del Proyecto "WebWizard: Tu Guía Experta para Entrevistas de Desarrollo Web."

## Contenido

- **[1. Descripcion](#1-descripción)**
- **[2. Objetivo](#2-objetivo)**
- **[3. Funcionamiento de la aplicación](#3-funcionamiento-de-la-aplicación)**
- **[4. Tecnologías utilizadas](#4-tecnologías-utilizadas)**
- **[5. Estructura del proyecto](#5-estructura-del-proyecto)**
- **[6. Flujo de Trabajo](#6-flujo-de-trabajo)**
- **[7. Uso de la aplicación](#7-uso-de-la-aplicación)**
- **[8. Mejoras](#8mejoras)**
- **[9. Licencia](#9-licencia)**
- **[10. Autores](#10-autores)**

## 1. Descripción.

El proyecto **WebWizard** es una aplicación web que tiene como objetivo ayudar a los estudiantes de desarrollo web a prepararse para realizar entrevistas de trabajo. La aplicación proporciona una serie de preguntas de diferentes categorías en el mundo del desarrollo web, como por ejemplo **"CSS"**, **"Python"** y **"Modelos de Inteligencia Artificial (IA)"** entre otros. 

[subir](#contenido)

## 2. Objetivo.

El objetivo de este proyecto es crear un **Sistema Experto**, capaz de presentar a los estudiantes las preguntas más frecuentes en entrevistas de trabajo, de manera que puedan prepararse para responderlas de la mejor manera posible. La idea principal de este proyecto es que sea escalable y que se puedan añadir nuevas preguntas y categorías de manera sencilla, en esta primera versión se han añadido 3 categorías de preguntas.

[subir](#contenido)

## 3. Funcionamiento de la aplicación.

La aplicación **WebWizard** es muy sencilla de utilizar, al ingresar a la página principal, el usuario podrá ver las diferentes categorías de preguntas disponibles, al hacer clic en una categoría, se desplegarán las preguntas correspondientes a esa categoría. Las preguntas inicialmente en esta versión serán **6 por categoría**, pero se espera que en futuras versiones se puedan añadir más preguntas. El usuario deberá de rellenar el formulario con sus respuestas y al finalizar podrá ver el resultado de su prueba, en la que se le indicará cuantas respuestas correctas ha tenido y cuantas incorrectas.

[subir](#contenido)

## 4. Tecnologías utilizadas.

- [Flask](https://flask.palletsprojects.com/en/3.0.x/)
Framework para Python. Se utiliza en este proyecto para crear la aplicación web y manejar las rutas y las solicitudes HTTP.

- [SpaCy](https://spacy.io)
Biblioteca de procesamiento de lenguaje natural (NLP) de código abierto. Se utiliza para el procesamiento de texto, incluyendo tokenización, análisis gramatical y extracción de información. La clase _Matcher_ es una clase de SpaCy que permite realizar coincidencias de patrones en texto utilizando reglas definidas. Se utiliza para encontrar patrones específicos en el texto, como verbos de acción o frases nominales.

- [SQLite](https://www.sqlite.org/index.html)
Se utiliza para almacenar las preguntas y respuestas de la aplicación. SQLite es una base de datos relacional que se utiliza en aplicaciones de pequeño y mediano tamaño. Es la **base de conocimiento** de un sistema experto, usado en inteligencia artificial.

- [Bootstrap y CSS](https://getbootstrap.com)
Framework de código abierto para el diseño de sitios web y aplicaciones web. Se utiliza en este proyecto para el diseño de la interfaz de usuario.

[subir](#contenido)

## 5. Estructura del proyecto.

El proyecto está estructurado de la siguiente manera:

- **main.py**: Archivo principal de la aplicación, contiene las rutas y las funciones que se ejecutan al realizar una solicitud HTTP.
  
- **main_con_cmd.py**: Exactamente igual que el main.py, pero con la diferencia de que este archivo se ejecuta desde la **cmd.**

- **technical_interview_questions.db**: Base de datos SQLite que contiene las preguntas y respuestas de la aplicación.
  
- **utils.py**: "El archivo utils.py contiene una colección de funciones de utilidad diseñadas para simplificar y mejorar el estilo del archivo principal main.py, proporcionando una forma más elegante y eficiente de realizar tareas específicas dentro del proyecto.
  
- **db/**: Carpeta que contiene los archivos relacionados con la base de datos SQLite. Tiene 2 archivos dentro de ella:
  
  - **database.py**: Script que tiene la creción de las base de datos, creación de las tablas e insercción de los datos. Con este ejecutable se crea el **technical_interview_questions.db**.
  - **query.py**: Consultas para obtener los datos de las tablas.
  
- **templates/**: Carpeta que contiene los archivos HTML de la aplicación.
  
- **static/**: Carpeta que contiene los archivos estáticos de la aplicación, como CSS, JavaScript e Imágenes.

- **test/**: Carpeta que contiene los archivos de prueba de la aplicación.
  
- **README.md**: Archivo que contiene la documentación del proyecto.

- **.gitignore**: Archivo que contiene los archivos y carpetas que se ignorarán en el control de versiones.

[subir](#contenido)

## 6. Flujo de Trabajo. **Revisar**

### Paso 1: Identificar Temas Clave para Entrevistas de Desarrollo Web.

- Fundamentos de Python
- Librerías de Python
- POO con Python

### Paso 2: Recopilar Preguntas Frecuentes de Entrevistas.

Reúne una variedad de preguntas comunes que se hacen en entrevistas de trabajo relacionadas con el desarrollo web. 

### Paso 3: Estructurar la Base de Conocimientos.

- Organiza las preguntas recopiladas en categorías lógicas, como "Fundamentos de Python", "Librerías de Python" y "POO con Python".
- Crear Modelos de Respuesta: Desarrolla modelos de respuesta para cada pregunta que incluyan la respuesta correcta, ejemplos prácticos y explicaciones detalladas.

### Paso 4: Implementar la Lógica del Sistema Expert.

- Utiliza Python para implementar la lógica del sistema experto. Puedes considerar el uso de bibliotecas como pyknow para representar reglas de inferencia o implementar tu propia lógica de procesamiento de preguntas y respuestas.

### Paso 5: Integrar Interfaz de Usuario
Desarrolla una interfaz de usuario que permita a los usuarios interactuar con el sistema experto. Puedes optar por una interfaz de línea de comandos, una aplicación web simple o una interfaz gráfica de usuario (GUI) según tus preferencias y habilidades.

### Paso 6: Alimentar el Sistema con Preguntas y Respuestas
Incorporar Preguntas y Respuestas: Introduce las preguntas y respuestas recopiladas en la base de conocimientos del sistema experto.

[subir](#contenido)

## 7. Uso de la aplicación. **TODO**

Para utilizar la aplicación **WebWizard** sigue los siguientes pasos:

## 8. Mejoras.

- **Añadir más categorías de preguntas**: En futuras versiones se pueden añadir más categorías de preguntas, como "JavaScript", "React", "Django" y "Machine Learning".
  
- **Añadir más preguntas por categoría**: Se pueden añadir más preguntas por categoría para aumentar la variedad y la dificultad de las pruebas.
  
- **Mejorar la interfaz de usuario**: Se puede mejorar la interfaz de usuario para que sea más atractiva y fácil de usar.
  
- **Añadir un cronómetro**: Se puede añadir un cronómetro para limitar el tiempo que los usuarios tienen para responder a las preguntas.
    
- **Añadir una función de retroalimentación**: Se puede añadir una función de retroalimentación para proporcionar a los usuarios información adicional sobre las respuestas correctas e incorrectas.
  
- **Añadir una función de revisión de respuestas**: Se puede añadir una función que permita a los usuarios revisar sus respuestas y corregirlas antes de finalizar la prueba.
  
- **Añadir una función de generación de informes**: Se puede añadir una función que genere un informe detallado de los resultados de la prueba, incluyendo las respuestas correctas e incorrectas, el tiempo empleado y la puntuación obtenida.
  
- **Añadir una función de recomendación de recursos**: Se puede añadir una función que recomiende a los usuarios recursos adicionales, como libros, cursos en línea y tutoriales, para ayudarles a mejorar sus habilidades y conocimientos.

[subir](#contenido)

## 9. Licencia.

Este proyecto está bajo la **licencia MIT**.

[subir](#contenido)

## 10. Autores.

- [José Miguel Escribano Ruiz](https://github.com/JMER15)
- [Virginia Ordoño Bernier](https://github.com/viorbe20)

[subir](#contenido)