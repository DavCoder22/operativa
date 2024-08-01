import openai
import os


class GptAnaliser:

    @staticmethod
    def interpretar_sensibilidad(resultados):
        """
        Obtiene una interpretación de sensibilidad utilizando GPT.

        :param resultados: Diccionario con los resultados del problema resuelto.
        :return: Descripción generada por GPT.
        """
        # Configurar la clave de API de OpenAI aca se pone lo que te pase

        # Construir el prompt para GPT
        prompt = (
            "A continuación se presenta un análisis de sensibilidad para un problema de programación lineal. "
            "Se incluyen cambios hipotéticos en los coeficientes de la función objetivo y las restricciones para "
            "demostrar cómo pueden afectar la solución óptima. Por favor, interpreta los resultados y proporciona "
            "una descripción detallada de cómo estos cambios pueden impactar en la solución óptima.\n\n"

            "Resultados del Problema de Programación Lineal:\n"
            f"Función Objetivo: {resultados['Función']}\n"
            f"Tipo de Objetivo: {resultados['Objetivo']}\n"
            f"Variables y Valores: {resultados['Variables']}\n"
            f"Coeficientes: {resultados['Coeficientes']}\n"
            f"Restricciones: {resultados['Restricciones']}\n"
            f"Valor de la Función Objetivo: {resultados['Valor_Objetivo']}\n"
            f"Holguras: {resultados['Holguras']}\n"
            f"Artificios: {resultados['Artificios']}\n\n"

            "Ejemplo de Análisis de Sensibilidad:\n"
            "1. Si el coeficiente del término x en la función objetivo aumenta de 40 a 50, ¿cómo afecta esto a la "
            "solución óptima y al valor de la función objetivo?\n"
            "2. Si la cantidad total de recurso disponible para la primera restricción aumenta de 100 a 120, ¿cómo "
            "se modificaría la solución óptima?\n\n"

            "Por favor, proporciona una interpretación detallada de estos resultados y ejemplos."
        )

        # Realizar la solicitud a OpenAI
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Cambia el modelo según tus necesidades
            messages=[
                {"role": "system",
                 "content": "Eres un asistente experto en programación lineal y análisis de sensibilidad."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=400
        )

        # Obtener la respuesta
        informacion = response.choices[0]['message']['content'].strip()
        return informacion


# Ejemplo de uso
if __name__ == "__main__":
    resultados = {
        "Función": "3x + 2y",
        "Objetivo": "Maximizar",
        "Variables": {"x": 2.5, "y": 1.5},
        "Coeficientes": [3, 4],
        "Restricciones": ["x + y <= 5", "x >= 0", "y >= 0"],
        "Valor_Objetivo": 15,
        "Holguras": {"holgura_1": 0.0},
        "Artificios": {"artificial_1": 0.0}
    }

    descripcion_sensibilidad = GptAnaliser.interpretar_sensibilidad(resultados)
    if descripcion_sensibilidad:
        print("Descripción de Sensibilidad:")
        print(descripcion_sensibilidad)
