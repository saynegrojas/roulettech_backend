# Roulettech Backend

This is the backend part of the Roulettech web application, built with Django and the Django REST Framework. It provides a RESTful API for the frontend to interact with.

## Getting Started

1. Clone the repository:

   ```bash
   https://github.com/saynegrojas/roulettech_backend.git
   
2. Create a virtual environment and activate it:

   ```python -m venv env``` to create a virtual environment
   ```source env/bin/activate``` to activate the virtual environment.

4. Install the dependencies:

   ```pip install -r requirements.txt``` where the `requirements.txt` directory is located.

5. Run the migrations

   ```python manage.py makemigrations``` generates migration files based on model changes.

   ```python manage.py migrate``` apply the generated migration files to the database

6. Start the development server:

   ```python manage.py runserver``` to start the development server at  `http://localhost:8000/`.
