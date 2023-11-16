Fastapi suport both web interfaces for 
api interaction:

    url/redoc -> ReDocs
    url/docs -> Swagger

Inside de docker compose the section 
that calls uvicorn/gunicorn most set
an bind to 0.0.0.0

    command: uvicorn api:app \ 
    --host 0.0.0.0 --port 8000

