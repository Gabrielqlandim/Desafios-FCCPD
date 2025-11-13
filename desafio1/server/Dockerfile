FROM python:3.12-slim

WORKDIR /app

# Instala o Flask diretamente (pra evitar qualquer problema com requirements.txt)
RUN pip install --no-cache-dir flask

# Copia o código da aplicação
COPY app.py .

EXPOSE 8080

CMD ["python", "app.py"]
