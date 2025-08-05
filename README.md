# 🛠️ Microservicio de Productos

Este proyecto es un microservicio RESTful para la gestión de productos, desarrollado con Django 4.2+ y Django REST Framework.

---

## 🚀 Características

- API RESTful con endpoints para CRUD de productos
- Paginación configurable (`per_page`)
- Respuestas estructuradas
- Documentación Swagger
- Pruebas automatizadas
- Configurado para ejecutarse en entorno local o con Docker

---

## 🧱 Estructura del Proyecto
src/
├── manage.py
├── app/
│ ├── settings.py
│ ├── urls.py
│ └── ...
└── apps/products/
├── models.py
├── serializers.py
├── views.py
└── tests/

---

## ⚙️ Requisitos

- Python 3.11
- Docker (opcional)

---

## 💻 Instalación Local

```bash
# Clona el repositorio
git clone https://github.com/AngelRodriguez319/wolf-sellers-assessment.git
cd wolf-sellers-assessment

# Crea entorno virtual
python -m venv .venv
source .venv/bin/activate  # o .venv\Scripts\activate en Windows

# Instala dependencias
pip install -r requirements.txt

# Ejecuta migraciones
python src/manage.py migrate

# Corre el servidor
python src/manage.py runserver
```

---

## 🐳 Instalación con docker

```bash
# Clona el repositorio
git clone https://github.com/AngelRodriguez319/wolf-sellers-assessment.git
cd wolf-sellers-assessment

# Build del contenedor
docker-compose build

# Levantar el servicio
docker-compose up
```

---

## 🐳 Documentación de endpoints

Una vez el servidor esté corriendo, no se requiere usuario para ejecutar los endpoints:
- Swagger: http://localhost:8000/api/docs/
- Redoc: http://localhost:8000/api/redoc/
- Django Rest Framework: http://localhost:8000/docs/

---

## 🧪 Ejecutar pruebas

```bash
# Instalación local
python src/manage.py test apps.products.tests

# Instalación con Docker
docker-compose run web python manage.py test apps.products.tests
```

---

## 📘 Documentación de la API

No se requiere usuario para ejecutar los endpoints.

---

### 📦 Modelo: `Product`

| Campo        | Tipo         | Requerido | Descripción                      |
|--------------|--------------|-----------|----------------------------------|
| `uuid`       | UUID         | No        | ID único generado automáticamente (automático) |
| `name`       | String       | Sí        | Nombre del producto              |
| `description`| Text         | No        | Descripción del producto         |
| `price`      | Decimal      | Sí        | Precio del producto              |
| `available`  | Boolean      | No        | Si el producto está disponible (`True` por defecto) |
| `created_at` | DateTime     | No        | Fecha de creación (automático)  |
| `updated_at` | DateTime     | No        | Fecha de última modificación (automático)    |

---

### 📋 Endpoints disponibles

#### Obtener listado de productos

**GET** `/api/products/`

**Query params:**

- `page`: número de página (por defecto: 1)
- `per_page`: número de resultados por página (por defecto: 50)

**Respuesta:**
```json
{
  "count": 125,
  "page": 1,
  "per_page": 50,
  "results": [
    {
      "uuid": "f8a16...",
      "name": "Producto 1",
      "description": "Descripción del producto",
      "price": "199.99",
      "available": true,
      "created_at": "2025-08-05T12:00:00Z",
      "updated_at": "2025-08-05T12:00:00Z"
    },
    ...
  ]
}
```

#### Crear un producto

**POST** `/api/products/`

**Body:**

```json
{
  "name": "Nuevo producto",
  "description": "Descripción",
  "price": "100.00",
  "available": true
}
```

**Respuesta:**
```json
{
  "uuid": "1c2d3e...",
  "name": "Nuevo producto",
  "description": "Descripción",
  "price": "100.00",
  "available": true,
  "created_at": "...",
  "updated_at": "..."
}
```

#### Obtener un producto por ID

**GET** `/api/products/{id}/`

**Respuesta:**
```json
{
    "uuid": "f8a16...",
    "name": "Producto 1",
    "description": "Descripción del producto",
    "price": "199.99",
    "available": true,
    "created_at": "2025-08-05T12:00:00Z",
    "updated_at": "2025-08-05T12:00:00Z"
}
```

#### Actualizar un producto (todos los campos)

**PUT** `/api/products/{id}/`

**Body:**
```json
{
  "name": "Nombre actualizado",
  "description": "Texto actualizado",
  "price": "150.00",
  "available": false
}
```

**Respuesta:**
```json
{
    "uuid": "f8a16...",
    "name": "Nombre actualizado",
    "description": "Texto actualizado",
    "price": "150.00",
    "available": false,
    "created_at": "2025-08-05T12:00:00Z",
    "updated_at": "2025-08-05T12:00:00Z"
}
```

#### Actualizar un producto (parcialmente)

**PATCH** `/api/products/{id}/`

**Body:**
Solo los campos que se desean modificar
```json
{
  "price": "199.99"
}
```

**Respuesta:**
```json
{
    "uuid": "f8a16...",
    "name": "Producto 1",
    "description": "Descripción del producto",
    "price": "199.99",
    "available": false,
    "created_at": "2025-08-05T12:00:00Z",
    "updated_at": "2025-08-05T12:00:00Z"
}
```

#### Eliminar un producto

**DELETE** `/api/products/{id}/`

**Respuesta:** 204 No Content

---

### ✅ Códigos de respuesta

| Código | Significado            |
| ------ | ---------------------- |
| 200    | Respuesta satisfactoria                     |
| 201    | Producto creado exitosamente    |
| 204    | Producto eliminado exitosamente |
| 400    | Error de validación en campos    |
| 404    | Producto no encontrado          |
