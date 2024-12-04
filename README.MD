*** Sale Management ***

# Technologies used for this project

We used django 5.0.1, python 3.9.7, bootstrap 5.3.1, jquery 3.7.1 in our app.

# Installation

for running our app, You have to install python or anaconda on your pc or server.

1. Install dependencies with pip. (If you are using virtual environment remember to activate it)

    `pip install -r requirements.txt`

2. Perform migrations:

    `python manage.py makemigrations`

    Or Do the migrations separately in case the command does not fail.

    `python manage.py makemigrations manager`
    `python manage.py makemigrations project`
    `python manage.py makemigrations product`
    `python manage.py makemigrations order`
    `python manage.py makemigrations servicecall`

    And finally create the database.

    `python manage.py migrate`

3. Run the project:

    `python manage.py runserver`




