# ERP Car Sales

ERP Car Sales is a Django REST API for managing car catalog data, branches, inventory movements, customers, and employee authentication for a car sales ERP workflow.

## Current Scope

- Backend-only Django project
- JWT-based authentication for employees
- CRUD endpoints for reference data such as branches, regions, colors, makes, fuel types, and countries
- Inventory and transfer management endpoints
- Auto-generated API docs with Swagger and ReDoc

## Tech Stack

- Python 3.12+
- Django 5
- Django REST Framework
- Simple JWT
- drf-yasg
- SQLite for local development

## Project Structure

```text
erp-car-sales/
├── backend/
│   ├── api/          # ERP domain models, serializers, viewsets, routes
│   ├── users/        # Custom user model and auth endpoints
│   ├── core/         # Django settings, URLs, schema config
│   ├── manage.py
│   └── requirements.txt
├── LICENSE
└── README.md
```

## Setup

1. Create a virtual environment:

   ```bash
   cd backend
   python3 -m venv .venv
   source .venv/bin/activate
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run migrations:

   ```bash
   python manage.py migrate
   ```

4. Start the development server:

   ```bash
   python manage.py runserver
   ```

The API will be available at `http://127.0.0.1:8000/`.

## Docker

Run the project with Docker Compose:

```bash
docker compose up --build
```

This starts the Django app on `http://127.0.0.1:8000/` and applies migrations automatically on container start.

Useful commands:

```bash
docker compose down
docker compose exec web python manage.py createsuperuser
docker compose exec web python manage.py test
```

## Main URLs

- API root: `http://127.0.0.1:8000/api/v1/`
- Swagger UI: `http://127.0.0.1:8000/swagger/`
- ReDoc: `http://127.0.0.1:8000/redoc/`
- Admin panel: `http://127.0.0.1:8000/admin/`

## Authentication Endpoints

- `POST /api/v1/users/signup/`
- `POST /api/v1/users/login/`
- `POST /api/v1/users/token/`
- `POST /api/v1/users/token/refresh/`

`signup` requires the following fields:

- `username`
- `password`
- `email`
- `first_name`
- `last_name`
- `middle_name`
- `date_of_birth`
- `gender`
- `address`
- `position`
- `salary`
- `hire_date`

## Example Requests

Create a user:

```bash
curl -X POST http://127.0.0.1:8000/api/v1/users/signup/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "admin1",
    "password": "StrongPass123!",
    "email": "admin@example.com",
    "first_name": "Admin",
    "last_name": "User",
    "middle_name": "System",
    "date_of_birth": "1995-04-12",
    "gender": "male",
    "address": "Tashkent",
    "position": "manager",
    "salary": "2500.00",
    "hire_date": "2024-01-15"
  }'
```

Login:

```bash
curl -X POST http://127.0.0.1:8000/api/v1/users/login/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "admin1",
    "password": "StrongPass123!"
  }'
```

## Quality Checks

Run Django checks:

```bash
cd backend
.venv/bin/python manage.py check
```

Run tests:

```bash
cd backend
.venv/bin/python manage.py test
```

Run checks in Docker:

```bash
docker compose run --rm web python manage.py check
docker compose run --rm web python manage.py test
```

## Fixes Applied

- Connected the project to the custom `users.User` model via `AUTH_USER_MODEL`
- Registered models from the `api.models` package so Django can discover them correctly
- Fixed transfer serializer querysets that were passed incorrectly
- Fixed signup so passwords are hashed instead of stored as plain text
- Expanded signup serializer to include required user fields
- Improved login response to return both access and refresh tokens
- Added basic API and auth regression tests
- Updated dependency guidance for fresh local setup
