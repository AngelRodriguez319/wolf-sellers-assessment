# Dockerfile

FROM python:3.11-slim

# Establece el directorio de trabajo principal
WORKDIR /app

# Copiar e instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todo el proyecto
COPY . .

# Ir al subdirectorio "src" donde está manage.py
WORKDIR /app/src

# Exponer el puerto 8000
EXPOSE 8000

# Comando por defecto: aplicar migraciones y levantar servidor
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]