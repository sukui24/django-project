# django-project

# Used Technologies
- [Python 3.12.0](https://www.python.org/)
- [Django 5.0](https://www.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)

## Environment variables
- SECRET_KEY - Secret key for django's settings, can be a row of ~32 random characters
- DEBUG - Debug mode. Recommended for use '1', but will work fine with '0'

# Local Setup
- Open your VSCode or any other IDE
- Enter empty folder
    - Make sure you entered your folder in terminal, it will show path to folder
- Clone project
  ```bash
  git clone https://github.com/sukui24/django-project.git
  ```
- Enter repository folder
  ```bash
  cd django-project
  ```
- Create virtual environment:
  ```bash
  python -m venv venv
  ```
- Activate virtual environment:
  ```bash
  venv/scripts/activate
  ```
  > you will see (venv) before you folder path in termian (At least in VSCode)
- Enter project folder:
  ```bash
  cd django_project
  ```
- Install requirements:
  ```bash
  pip install -r requirements.txt
  ```
- Provide migrations:
  ```bash
  python manage.py migrate
  ```
- Load fixtures ('dummy' data for website testing)
  ```bash
  python manage.py loaddata fixtures.json
  ```
- Configure virtual environment variables:
    - Create .env file in project folder (./django_project/)
    - Copy everything from .env.example to .env
    - Fill up variables (their meaning you can see above in this readme)
- Run tests to make sure everything working fine:
  ```bash
  python manage.py test
  ```
- Run server:
  ```bash
  python manage.py runserver
  ```

## Notes
Django Project has admin panel to edit all data manually. To enter it you need to create super user:
- Make sure you into virtual environment (venv)
    - If not you can go back to hosting guide and enter it again
      > if venv folder already exists there's no need to create it again
- Make sure your into project folder (you will have your own path):
  > C:\python\some\path\django-project\django_project>
- Create super user:
  ```bash
  python manage.py createsuperuser
  ```
  - Fill up all asked fields
- Now you can go to http://127.0.0.1:8000/admin/ it's enpoint for admin panel
- Log in and change any data :)
