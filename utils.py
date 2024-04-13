import spacy
import sqlite3

SIMILARITY_THRESHOLD = 0.7

# Cargar el modelo de spaCy en español
nlp = spacy.load("es_core_news_lg")

def evaluar_respuesta(respuesta_usuario, respuesta_correcta):

    """
    Evalúa si la respuesta del usuario es 
    correcta utilizando el modelo de spaCy en español
    """

    doc_usuario = nlp(respuesta_usuario.lower())
    doc_correcta = nlp(respuesta_correcta.lower())

    # Calcular la similitud entre las respuestas utilizando el modelo de spaCy
    similitud = doc_usuario.similarity(doc_correcta)

    print(f"Similitud: {similitud}")

    # Si la similitud es mayor o igual a un umbral específico, consideramos la respuesta como correcta
    if similitud >= SIMILARITY_THRESHOLD:
        return True
    else:
        return False

def practicar_entrevista(preguntas_respuestas, respuestas_usuario):

    """
    Función para simular la práctica de 
    una entrevista de desarrollo web
    """
    resultados = []

    for index, qa_pairs in enumerate(preguntas_respuestas):
        for qa_pair in qa_pairs:
            pregunta = qa_pair[1]
            respuesta_correcta = qa_pair[2]
            
            # Obtener la respuesta del usuario si está disponible
            if respuestas_usuario:
                respuesta_usuario = respuestas_usuario.pop(0)
            else:
                respuesta_usuario = ""

            # Evaluar si la respuesta del usuario es correcta
            es_correcta = evaluar_respuesta(respuesta_usuario, respuesta_correcta)

            # Guardar el resultado de la evaluación
            resultados.append({
                "pregunta": pregunta,
                "respuesta_usuario": respuesta_usuario,
                "respuesta_correcta": respuesta_correcta,
                "es_correcta": es_correcta
            })

    return resultados

def obtener_tipo_preguntas(language):

    # Conecta a la base de datos
    conn = sqlite3.connect('technical_interview_questions.db')
    cursor = conn.cursor()

    questions_array = []

    try:
        
        # Consulta para obtener 2 preguntas de nivel 1 de manera aleatoria
        cursor.execute(f"SELECT * FROM qa_pair_{language} WHERE level = 1 ORDER BY RANDOM() LIMIT 2;")
        questions_level_1 = cursor.fetchall()  # Obtener todas las filas (preguntas)

        # Consulta para obtener 2 preguntas de nivel 2 de manera aleatoria
        cursor.execute(f"SELECT * FROM qa_pair_{language} WHERE level = 2 ORDER BY RANDOM() LIMIT 2;")
        questions_level_2 = cursor.fetchall()  # Obtener todas las filas (preguntas)

        # Consulta para obtener 2 preguntas de nivel 3 de manera aleatoria
        cursor.execute(f"SELECT * FROM qa_pair_{language} WHERE level = 3 ORDER BY RANDOM() LIMIT 2;")
        questions_level_3 = cursor.fetchall()  # Obtener todas las filas (preguntas)

        # Crear un array con las preguntas de diferentes niveles
        questions_array = [questions_level_1, questions_level_2, questions_level_3]

        # guardar el resultado de la consulta en un diccionario igual que este: {'id': 1, 'question': '¿Qué es Python?', 'answer': 'Python es un lenguaje de programación interpretado, interactivo y orientado a objetos.', 'level': 1}
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

    return questions_array
