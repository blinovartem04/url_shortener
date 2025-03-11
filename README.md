# Key Features
* Create short links for long URLs.
* Redirect users from short links to original URLs.
* Simple and intuitive user interface.
* Deployable on the internet using platforms like Heroku, Render, or any VPS.
* Extensible functionality (e.g., click statistics, custom short links).

# Technologies
* Python.
* Django
* HTML/CSS
* SQLite
  
# Installation and Setup
## Local Development
### Clone the repository:
* git clone https://github.com/blinovartem04/url_shortener.git
* cd url-shortener
### Install dependencies:
* pip install -r requirements.txt
### Apply migrations:
* python manage.py migrate
### Create a superuser (optional):
* python manage.py createsuperuser
### Run the development server:
* python manage.py runserver
### Open the application in your browser:
* http://127.0.0.1:8000/

# Deployment
### 1. Sign up at Render.
### 2. Create a new Web Service and connect your GitHub repository.
### 3. Configure the following settings:
* Build Command: pip install -r requirements.txt
* Start Command: gunicorn urlshortener.wsgi:application
### 4.Add environment variables:
* ALLOWED_HOSTS: your-render-app.onrender.com
* DEBUG: False
* DATABASE_URL: (provided by Render)
