from estudiante import Estudiante
from encuesta import Encuesta

def main():
    encuesta = Encuesta()
    print("\n=== SISTEMA DE ENCUESTAS ===")
    n = int(input("\nCuantos estudiantes responderan la encuesta?: "))
    for p in range(n):
        print(f"\n--- Encuesta para el estudiante {p+1} ---")
        nombre = input("Nombre: ").strip()
        edad = int(input("Edad: ").strip())
        carrera = input("Carrera: ").strip()
        estudiante = Estudiante(nombre, edad, carrera)

        respuestas_usuario = []
        print("\n=== PREGUNTAS DE LA ENCUESTA ===")
        print("Por favor, responde las siguientes preguntas:")
        print()
        if not encuesta.preguntas:
            print("[ERROR] No hay preguntas cargadas para la encuesta.")
        else:
            for i, pregunta in enumerate(encuesta.preguntas, start=1):
                print(f"Pregunta {i}:")
                respuesta = input(f"{i}. {pregunta}\nTu respuesta: ").strip()
                print()
                respuestas_usuario.append(respuesta)

        encuesta.agregar_respuesta(estudiante, respuestas_usuario)

    encuesta.mostrar_resultados()
    encuesta.resumen()
if __name__=="__main__":
    main()

