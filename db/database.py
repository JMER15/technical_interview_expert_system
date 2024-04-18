import sqlite3

# Conecta a la base de datos (la crea si no existe)
conn = sqlite3.connect('technical_interview_questions.db')

# Crea un cursor para ejecutar sentencias SQL
cursor = conn.cursor()

# borrar si ejecutamos de nuevo 
cursor.execute("DROP TABLE IF EXISTS qa_pair_python")
cursor.execute("DROP TABLE IF EXISTS qa_pair_css")
cursor.execute("DROP TABLE IF EXISTS qa_pair_expert_systems")

# Tabla qa_pair_python para preguntas y respuestas sobre python
create_table_query = '''
    CREATE TABLE qa_pair_python (
        id INTEGER PRIMARY KEY,
        question TEXT NOT NULL,
        answer TEXT NOT NULL,
        level INTEGER NOT NULL
    );
'''

# Tabla qa_pair_css para preguntas y respuestas sobre css
create_table_query2 = '''
    CREATE TABLE qa_pair_css (
        id INTEGER PRIMARY KEY,
        question TEXT NOT NULL,
        answer TEXT NOT NULL,
        level INTEGER NOT NULL
    );
'''

create_table_query3 = '''
    CREATE TABLE qa_pair_expert_systems (
        id INTEGER PRIMARY KEY,
        question TEXT NOT NULL,
        answer TEXT NOT NULL,
        level INTEGER NOT NULL
    );
'''

# Ejecuta las sentencia SQL para crear la tabla
cursor.execute(create_table_query)
cursor.execute(create_table_query2)
cursor.execute(create_table_query3)

# Preguntas y respuestas sobre python
qa_pair_python = [
    ("¿Qué es Python?", "Python es un lenguaje de programación interpretado y de alto nivel.", 1),
    ("¿Cuál es la diferencia entre Python 2 y Python 3?", "Python 2 es una versión anterior de Python, mientras que Python 3 es la versión más reciente y recomendada.", 2),
    ("¿Qué es una lista en Python?", "Una lista en Python es una estructura de datos que puede contener múltiples elementos, como números, cadenas, u otros objetos.", 3),
    ("¿Qué es un diccionario en Python?", "Un diccionario en Python es una estructura de datos que mapea claves a valores, permitiendo un acceso eficiente a los elementos.", 2),
    ("¿Qué es una función en Python?", "Una función en Python es un bloque de código reutilizable que realiza una tarea específica cuando se llama.", 1),
    ("¿Qué es la recursión en Python?", "La recursión en Python es un concepto en el que una función se llama a sí misma para resolver un problema más pequeño.", 3),
    ("¿Qué es un módulo en Python?", "Un módulo en Python es un archivo que contiene definiciones y declaraciones de Python, que se pueden importar en otros programas.", 2),
    ("¿Qué es una excepción en Python?", "Una excepción en Python es un evento que interrumpe el flujo normal de un programa y se maneja mediante bloques try-except.", 3),
    ("¿Qué es la programación orientada a objetos en Python?", "La programación orientada a objetos en Python es un paradigma de programación en el que los objetos y las clases son fundamentales para la estructura del programa.", 1),
    ("¿Qué es una clase en Python?", "Una clase en Python es una plantilla para crear objetos que define atributos y métodos comunes a todos los objetos creados a partir de ella.", 2),
    ("¿Qué es la herencia en Python?", "La herencia en Python es un mecanismo que permite a una clase heredar atributos y métodos de otra clase.", 3),
]

# Preguntas y respuestas sobre css
qa_pair_css = [
    ("¿Qué es CSS?", "CSS (Cascading Style Sheets) es un lenguaje de hojas de estilo utilizado para describir la presentación de un documento HTML.", 1),
    ("¿Cuál es la diferencia entre CSS y HTML?", "HTML (HyperText Markup Language) se utiliza para estructurar el contenido de una página web, mientras que CSS se utiliza para diseñar y dar estilo a la página.", 2),
    ("¿Qué es un selector en CSS?", "Un selector en CSS es una expresión que selecciona elementos HTML basados en su etiqueta, clase, id u otros atributos.", 3),
    ("¿Qué es la cascada en CSS?", "La cascada en CSS se refiere al proceso de aplicar estilos a los elementos de una página web, siguiendo un orden de prioridad y especificidad.", 2),
    ("¿Qué es un box model en CSS?", "El box model en CSS es un modelo que describe cómo se representan los elementos en una página web, incluyendo el contenido, el padding, el borde y el margen.", 1),
    ("¿Qué es un framework de CSS?", "Un framework de CSS es una colección de estilos predefinidos y componentes que facilitan el diseño y la creación de páginas web.", 3),
    ("¿Qué es un grid layout en CSS?", "Un grid layout en CSS es un sistema de diseño que permite organizar elementos en filas y columnas, facilitando la creación de diseños complejos y responsivos.", 2),
    ("¿Qué es un flexbox en CSS?", "Un flexbox en CSS es un sistema de diseño que permite organizar elementos de manera flexible y dinámica, adaptándose al tamaño de la pantalla y al contenido.", 1),
    ("¿Qué es la especificidad en CSS?", "La especificidad en CSS es un valor que determina qué regla se aplica a un elemento cuando hay múltiples reglas que se solapan.", 3),
    ("¿Qué es un pseudo-elemento en CSS?", "Un pseudo-elemento en CSS es un elemento virtual que permite aplicar estilos a partes específicas de un elemento, como la primera letra o la primera línea de un párrafo.", 2),
    ("¿Qué es un media query en CSS?", "Un media query en CSS es una técnica que permite aplicar estilos basados en las características del dispositivo, como el ancho de la pantalla o la orientación.", 1),
]

# Preguntas y respuestas sobre expert systems
qa_pair_expert_systems = [
    ("¿Qué es un sistema experto?", "Software capaz de simular el proceso de decisión que tomaría un experto humano en cierto campo en la solución de un problema.", 1),
    ("Características de los sistemas expertos", "Especialización, emulación del pensamiento humano, capacidad de aprendizaje, interactividad", 3),
    ("Tipos de sistemas expertos", "Casos, árboles de decisión, redes bayesianas, reglas", 2),
    ("¿Qué 3 tipos de conocimiento puede aportar un experto?", "Procedimental, heurístico, factual", 2),
    ("¿Qué dos estrategias de control se utilizan en los sistemas expertos?", "Razonamiento hacia adelante y razonamiento hacia atrás", 1),
    ("Nombra los cinco elementos que componen un sistema experto", "Interfaz de usuario, base de conocimiento, sistema para la adquisición de conocimiento, sistema de aplicación de decisiones, motor de inferencia", 3),
    ("Nombre los tres tipos de interfaz de usuario", "Gráfica, modo texto, combinación de ambas", 2),
]
    

# Define las sentencias SQL para insertar los datos
insert_query = '''
    INSERT INTO qa_pair_python (question, answer, level)
    VALUES (?, ?, ?)
'''

insert_query2 = '''
    INSERT INTO qa_pair_css (question, answer, level)
    VALUES (?, ?, ?)
'''

insert_query3 = '''
    INSERT INTO qa_pair_expert_systems (question, answer, level)
    VALUES (?, ?, ?)
'''

# Ejecuta la sentencia SQL de inserción para cada pregunta y respuesta
for question, answer, level in qa_pair_python:
    cursor.execute(insert_query, (question, answer, level))

for question, answer, level in qa_pair_css:
    cursor.execute(insert_query2, (question, answer, level))
    
for question, answer, level in qa_pair_expert_systems:
    cursor.execute(insert_query3, (question, answer, level))

# Guarda los cambios
conn.commit()

# Cierra la conexión a la base de datos
cursor.close()
conn.close()
