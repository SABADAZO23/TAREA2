class Encuesta:
    def __init__(self):
        # Lista de preguntas directamente en el código
        self.preguntas = [
            "¿Cuando trabajas en grupo, te gusta proponer ideas o prefieres que te asignen tareas?",
            "¿Qué es lo que más te molesta cuando trabajas con otras personas?",
            "¿Cómo manejas la presión cuando hay poco tiempo para entregar algo?",
            "¿Si hay diferencias en el grupo, prefieres hablarlas de frente o dejarlas pasar?",
            "¿Qué parte de un proyecto disfrutas más: investigar, organizar, exponer o redactar?",
            "¿Cuál es la idea o propuesta que tienes en mente para este proyecto?"
        ]
        self.respuestas = {}

    def agregar_respuesta(self, estudiante, respuestas_usuario):
        self.respuestas[estudiante.nombre] = {
            "edad": estudiante.edad,
            "carrera": estudiante.carrera,
            "respuestas": respuestas_usuario
        }
        estudiante.respuestas = respuestas_usuario

        nombre_archivo = f"{estudiante.nombre}.txt"
        with open(nombre_archivo, "w", encoding="utf-8") as f:
            f.write(f"Nombre: {estudiante.nombre}\n")
            f.write(f"Edad: {estudiante.edad}\n")
            f.write(f"Carrera: {estudiante.carrera}\n")
            f.write("Respuestas:\n")
            for i, (preg, resp) in enumerate(zip(self.preguntas, respuestas_usuario), start=1):
                f.write(f"{i}. {preg} → {resp}\n")
        print(f"Respuestas de {estudiante.nombre} guardadas en {nombre_archivo}")

    def mostrar_resultados(self):
        print("\n=== RESULTADOS DE LA ENCUESTA ===")
        for nombre, datos in self.respuestas.items():
            print(f"\nEstudiante: {nombre}")
            print(f"Edad: {datos['edad']}")
            print(f"Carrera: {datos['carrera']}")
            print("\nRespuestas:")
            respuestas_usuario = datos["respuestas"]
            for i, resp in enumerate(respuestas_usuario, start=1):
                if i-1 < len(self.preguntas):
                    print(f"{i}. {self.preguntas[i-1]}")
                    print(f"   Respuesta: {resp}")

    def resumen(self):
        # Primero guardamos el CSV como antes
        print("\nResumen general en CSV")
        import csv
        nombre_csv = "resumen_encuesta.csv"
        with open(nombre_csv, "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Nombre", "Edad", "Carrera"] + self.preguntas)
            for nombre, datos in self.respuestas.items():
                fila = [nombre, datos["edad"], datos["carrera"]] + datos["respuestas"]
                writer.writerow(fila)
        print(f"Resumen guardado en {nombre_csv}")

        # Ahora agregamos el conteo de preferencias
        print("\n=== RESUMEN DE PREFERENCIAS ===")
        # Para cada pregunta
        for num_pregunta, pregunta in enumerate(self.preguntas):
            print(f"\nPregunta {num_pregunta + 1}: {pregunta}")
            # Contamos las respuestas
            conteo = {}
            for datos in self.respuestas.values():
                respuesta = datos["respuestas"][num_pregunta]
                conteo[respuesta] = conteo.get(respuesta, 0) + 1
            
            # Mostramos las respuestas y su frecuencia
            print("Respuestas:")
            for respuesta, cantidad in conteo.items():
                porcentaje = (cantidad / len(self.respuestas)) * 100
                print(f"- '{respuesta}': {cantidad} vez(ces) ({porcentaje:.1f}%)")
