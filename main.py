from flask import Flask, render_template, request
from utils import *

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("home.html")

preguntas_y_respuestas = {}  # Variable global para almacenar las preguntas

@app.route("/test/<language>", methods=["GET", "POST"])
def test(language):

    global preguntas_y_respuestas  # Accedemos a la variable global
    
    if preguntas_y_respuestas == {}:  # Verificamos si las preguntas ya han sido generadas
        preguntas_y_respuestas = obtener_tipo_preguntas(language)  # Generamos las preguntas solo si no han sido generadas antes
    
    if request.method == "GET":
        return render_template("test.html", language=language, preguntas_y_respuestas=preguntas_y_respuestas)
    elif request.method == "POST":
        respuestas_usuario = []
        for key, value in request.form.items():
            if key.startswith('respuesta_'):
                respuestas_usuario.append(value)
        resultados = practicar_entrevista(preguntas_y_respuestas, respuestas_usuario)
        preguntas_y_respuestas = {}
        return render_template("resultados.html", resultados=resultados)

if __name__ == "__main__":
    app.run(debug=True)
