# Alexie

this is the backend repository for 'alexie', a project of a emotional diary for people  who want to have better understanding of their emotional processes, people diagnosed with alexithymia, autism, anxious people or people who want to record and follow their daily emotions in general.

in this project, we use:

| ![Python](    https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=whit)       | [Python](https://www.python.org/)       | v3.9.10 |

| ![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)   | [Django](https://www.djangoproject.com/)        | v4.1.5     |

| ![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)   | [Django Rest Framework](https://www.django-rest-framework.org/)        | v3.14      |

| ![Postgres](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)   | [PostgreSQL](https://www.postgresql.org/)       | v12.9      |

running in windows:

you need to create a database
 
you need to open your terminal and:

create an env
  - choose a folder and run
    python -m env <folder_name>
    
  - go to the folder you created and inside it, there is a script folder.
  - in the script folder, you run 
    activate.bat
your env is created and active to run the project

so, you need to go to the folder you cloned the project

install the libs
  - pip install -r requirements.txt

populate the db
  - python manage.py makemigrations
  - python manage.py migrate
  - python manage.py loaddata <name_app>

create an superuser
  - python manage.py createsuperuser

run the project
  - python manage.py runserver 

    
