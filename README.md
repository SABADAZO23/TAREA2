# Universidad Nacional de Colombia  
### Facultad de Ingeniería  
### Programa de Ingeniería Electrónica  


# TAREA 2  
**Sistema de Encuesta para Estudiantes en Python**

**Autor:** Jose Dario Ángulo Solis  
**Asignatura:** Programación Orientada a Objetos




## 📖 Introducción

El presente informe describe el desarrollo de un sistema en **Python** que permite gestionar encuestas para estudiantes de manera estructurada y automatizada.  
El proyecto surge como parte de las actividades académicas de la asignatura *Fundamentos de Python*, con el propósito de aplicar conceptos de programación estructurada y orientada a objetos en un contexto práctico.

El programa está diseñado para registrar estudiantes, aplicarles una encuesta y almacenar sus respuestas en un archivo, garantizando un proceso ordenado y fácil de analizar.

---

## 🎯 Objetivos

### Objetivo general
Desarrollar un sistema de encuestas en Python que permita registrar estudiantes, realizar preguntas y guardar las respuestas en un archivo para su posterior análisis.

### Objetivos específicos
- Implementar una clase **Estudiante** que maneje la información básica de cada participante.  
- Diseñar un módulo que administre el proceso de encuesta y la captura de respuestas.  
- Integrar los módulos en un archivo principal que coordine la ejecución del programa.  
- Generar un archivo en formato Excel que consolide las respuestas obtenidas.  

---

## ⚙️ Metodología

El sistema fue construido utilizando **Python 3.10**. Se organizó el código en módulos para garantizar claridad y reutilización:

- **`estudiante.py`** → Define la clase `Estudiante` con atributos y métodos relacionados con cada participante.  
- **`encuesta.py`** → Contiene la lógica de la encuesta, preguntas y recolección de respuestas.  
- **`inicio.py`** → Archivo principal que integra los módulos y ejecuta el flujo completo.  
- **`README.md`** → Documento con instrucciones de instalación y uso del sistema.  

Se utilizaron librerías como `pandas` y `openpyxl` para gestionar la exportación de datos en formato Excel.

---

## ▶️ Ejecución del programa

Para correr el programa se debe abrir una terminal en la carpeta del proyecto y ejecutar:

```bash
python inicio.py

Ejemplo de uso

Ingrese el número de estudiantes: 3

=== Registro de estudiantes ===
Nombre del estudiante 1: Ana
Nombre del estudiante 2: Luis
Nombre del estudiante 3: Sofía

=== Encuesta ===
Pregunta 1: ¿Te gusta programar en Python? 
Respuesta de Ana: Sí
Respuesta de Luis: No
Respuesta de Sofía: Sí

Resultados guardados en 'respuestas.xlsx'

