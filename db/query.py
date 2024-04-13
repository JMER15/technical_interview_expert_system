import sqlite3

# Conecta a la base de datos
conn = sqlite3.connect('technical_interview_questions.db')
cursor = conn.cursor()

try:

    # Consulta para obtener 2 preguntas de nivel 1 de manera aleatoria
    cursor.execute("SELECT * FROM qa_pair_python WHERE level = 1 ORDER BY RANDOM() LIMIT 2;")
    questions_level_1 = cursor.fetchall()  # Obtener todas las filas (preguntas)

    # Consulta para obtener 2 preguntas de nivel 2 de manera aleatoria
    cursor.execute("SELECT * FROM qa_pair_python WHERE level = 2 ORDER BY RANDOM() LIMIT 2;")
    questions_level_2 = cursor.fetchall()  # Obtener todas las filas (preguntas)

    # Consulta para obtener 2 preguntas de nivel 3 de manera aleatoria
    cursor.execute("SELECT * FROM qa_pair_python WHERE level = 3 ORDER BY RANDOM() LIMIT 2;")
    questions_level_3 = cursor.fetchall()  # Obtener todas las filas (preguntas)

    # Crear un array con las preguntas de diferentes niveles
    questions_array = [questions_level_1, questions_level_2, questions_level_3]

    """
    guardar el resultado de la consulta en un diccionario igual que este: 
    {'question': '¿Qué es Python?', 'answer': 'Python es un lenguaje de programación interpretado, interactivo y orientado a objetos.', 'level': 1}
    """
    preguntas_y_respuestas = []
    for question in questions_array:
        for qa_pair in question:
            pregunta_dict = {
                "question": qa_pair[1],
                "answer": qa_pair[2],
                "level": qa_pair[3]
            }
            preguntas_y_respuestas.append(pregunta_dict)

except sqlite3.Error as e:
    print(f"Error de SQLite: {e}")

finally:
    # Cierra la conexión a la base de datos
    cursor.close()
    conn.close()
