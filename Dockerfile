FROM python:3.11-slim

# Diretório da aplicação
WORKDIR /app

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# Dependências do sistema (necessário para psycopg2)
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Instala dependências do Python
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do projeto
COPY . /app/

# Coleta arquivos estáticos
RUN python manage.py collectstatic --noinput

# Expõe porta do Gunicorn
EXPOSE 8000

# Executa o Django com Gunicorn
CMD gunicorn core.wsgi:application --bind 0.0.0.0:8000
