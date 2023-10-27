release: python db_project/manage.py migrate && python db_project/manage.py collectstatic --noinput
web: gunicorn --pythonpath db_project db_project.wsgi