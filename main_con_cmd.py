import spacy
import time
from test.knowledge import preguntas_y_respuestas

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

    # Si la similitud es mayor o igual a un umbral específico, consideramos la respuesta como correcta
    if similitud >= 0.7:  # Umbral de similitud (ajustable según necesidades)
        return True
    else:
        return False

def practicar_entrevista():

    """
    Función para simular la práctica de 
    una entrevista de desarrollo web
    """

    print("Bienvenido a la práctica de la entrevista de desarrollo web.")
    print("Responderás preguntas sobre HTML, CSS y otros temas relacionados.\n")

    contador = 0

    for tema, preguntas_respuestas in preguntas_y_respuestas.items():
        print(f"---- Tema: {tema} ----\n")
        for qa_pair in preguntas_respuestas:
            pregunta = qa_pair['pregunta']
            respuesta_correcta = qa_pair['respuesta']

            print(pregunta)
            respuesta_usuario = input("\nTu respuesta: ")

            if evaluar_respuesta(respuesta_usuario, respuesta_correcta):
                print("¡Respuesta correcta!\n")
                contador += 1
            else:
                print(f"Respuesta incorrecta. La respuesta correcta es: {respuesta_correcta}\n")

    if contador == len(preguntas_y_respuestas['Python']):
        print("¡El puesto de trabajo es suyo. Enhorabuena!.\n")
    else:
        print(f"Has respondido correctamente a {contador} de {len(preguntas_y_respuestas['Python'])} preguntas.\n")
        print("El puesto de trabajo no es suyo.\n")

if __name__ == "__main__":

    print("\nIniciando la práctica para la entrevista de desarrollo web.\n")
    print("Por favor, espera un momento mientras se cargan las preguntas y respuestas...\n")
    time.sleep(5)
    print("¡Listo! Comencemos:\n")
    practicar_entrevista()
