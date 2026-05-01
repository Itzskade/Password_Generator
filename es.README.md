<p align="right">
  <a href="README.md">
    <img src="https://img.shields.io/badge/🌐%20English-README-%2312bab9?style=for-the-badge" alt="README English" />
  </a>
</p>


# Generador de contraseñas

Pequeño proyecto en Python con interfaz CLI que genera contraseñas seguras con longitud configurable. Permite usar letras, números y símbolos, regenerar contraseñas con la última longitud utilizada y validar entradas del usuario con intentos limitados.

Es una herramienta ligera, modular y enfocada al aprendizaje.

---

## 📦 Requisitos

- Python 3.10+

No requiere dependencias externas. Solo usa librerías estándar de Python.

---

## 🔧 Características

- Generación de contraseñas aleatorias seguras
- Longitud configurable (10–128 caracteres)
- Uso de letras mayúsculas, minúsculas, números y símbolos
- Regeneración usando la última longitud generada
- Validación de entrada con límite de intentos
- Menú básico en terminal
- Arquitectura modular (UI, lógica y configuración)

---

## ▶️ Uso

El programa se ejecuta en terminal y funciona mediante un menú interactivo:

- Generar una nueva contraseña indicando una longitud
- Regenerar la última contraseña generada
- Salir del programa

---

## 🧪 Ejemplos de comportamiento

✔ Generar contraseña de 12 caracteres  
→ Devuelve algo como `aF3!kL9@pQ2x`

✔ Generar contraseña de 20 caracteres  
→ Devuelve una contraseña más larga con mezcla de caracteres

✔ Regenerar última contraseña  
→ Genera una nueva usando la última longitud sin volver a pedirla

✘ Entrada inválida (ej. 5 o 200)  
→ Muestra error y solicita un valor válido

✘ Entrada no numérica  
→ Pide al usuario introducir un número válido

---

## 📝 Notas

- Proyecto creado con fines educativos
- Enfocado en diseño modular en Python
- Interacción mediante consola (CLI)
- Uso de generación aleatoria básica para seguridad
