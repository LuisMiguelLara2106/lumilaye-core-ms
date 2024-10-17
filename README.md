# FastAPI Microservice

Este es un microservicio de ejemplo construido con FastAPI.

## Características

- Estructura de proyecto limpia y organizada
- Configuración basada en entorno
- Endpoints de API RESTful
- Tests automatizados
- Documentación automática de API (proporcionada por FastAPI)

## Cómo ejecutar

1. Instalar dependencias:
   ```
   pip install -r requirements.txt
   ```

2. Ejecutar el servidor:
   ```
   uvicorn app.main:app --reload
   ```

3. Visitar `http://localhost:8000/docs` para ver la documentación de la API.

## Ejecutar tests

Para ejecutar los tests, use el siguiente comando:

```
pytest
```

## Docker

Para construir y ejecutar con Docker:

```
docker build -t fastapi-microservice .
docker run -p 8000:8000 fastapi-microservice
```