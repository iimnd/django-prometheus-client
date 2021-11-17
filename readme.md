virtualenv newenv

python manage.py runserver

echo $PYTHONPATH

source newenv/bin/activate

pip install django

python manage.py runserver

pip install prometheus-client

python manage.py runserver



path : 
- /ovo
- /gopay
- /metrics


desktop/django_prome_client
