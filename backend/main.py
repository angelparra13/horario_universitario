"""
main.py — Punto de entrada del servidor

Este es el archivo que ejecutas para levantar la API.
Sus responsabilidades son:
  - Crear la instancia principal de la aplicación FastAPI
  - Registrar todas las rutas (materias, bloques)
  - Configurar CORS para que el frontend pueda hacer peticiones
    desde otro puerto sin que el navegador lo bloquee
  - Definir el puerto y host donde corre el servidor

Comando para ejecutarlo:
  uvicorn main:app --reload

NO debe contener lógica de negocio. Solo configuración y arranque.
"""
