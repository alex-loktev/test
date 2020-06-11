source /home/www/code/insta/env/bin/activate
exec gunicorn -c "/home/www/code/insta/my_insta/gunicorn_config.py" redactor.wsgi

