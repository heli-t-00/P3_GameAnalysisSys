# install venv

# run this command to update pip
```shell
python.exe -m pip install --upgrade pip
```
# starting a django project steps for terminal
pip install django

# run this command to create project
django-admin startproject (name of project)

# MOVE the project up one level

# run this command to create app
python manage.py startapp (name of app)

# test and run server to make sure it works
python manage.py runserver


# install django rest framework
pip install django_rest_framework

# generate the neccessary code to set up the database
python manage.py migrate

# create superuser
python manage.py createsuperuser

python manage.py makemigrations
python manage.py migrate


# freezing what is installed into requirements (SNAPSHOT OF PIP INSTALLS)
python -m pip freeze > requirements.txt

# installs everything from requirements
pip install -r requirements.txt

