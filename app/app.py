from flask import Flask, render_template,request
import re

from lineal.LinearProgrammingSolver import LinearProgrammingSolver
from gpt.GptAnaliser import GptAnaliser

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/objective')
def objetivo():
    return render_template('objetivo.html')


@app.route('/linear', methods=['GET', 'POST'])
def linear():
    resultado = None
    if request.method == 'POST':
        # Extraer datos del formulario
        funcion_objetivo = request.form.get('funcion_objetivo')
        objetivo = request.form.get('objetivo')
        restricciones_raw = request.form.get('restriccion')

        # Procesar el campo de restricciones (separar por líneas)
        restricciones = [r.strip() for r in restricciones_raw.split('\n') if r.strip()]

        # Verificar datos recibidos (opcional, para depuración)
        print(f"Función Objetivo: {funcion_objetivo}")
        print(f"Objetivo: {objetivo}")
        print(f"Restricciones: {restricciones}")

        if not funcion_objetivo or not objetivo or not restricciones:
            return "Faltan datos en el formulario.", 400

        # Resolver el problema
        resultado = LinearProgrammingSolver.resolver_problema(funcion_objetivo, objetivo, restricciones)
        analisi=GptAnaliser.interpretar_sensibilidad(resultado)

        if resultado:
            return render_template('resultado.html',resultado=resultado,analisi=analisi)

    # Renderizar la plantilla con resultados
    return render_template('linear-programming.html')
@app.route('/transportation')
def transportation():
    return render_template('transportation.html')



if __name__ == '__main__':
    app.run(debug=True)
