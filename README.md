# django-database-project-heroku
### This tutorial is for standart Django project with app, static files and sqlite3 database.

## 1. Create Heroku App

Create Heroku app on `heroku.com` and in settings choose Buildpack as Python.

## 2. Create required files in Django project

Create `runtime.txt` in project root folder next to `manage.py` file. Check your Python version:

```python
py --version
Python 3.10.9
```

Add this to `runtime.txt` file:

```python
python-3.10.9
```

Create `Procfile` (no extensions) in root folder next to `requirements.txt`.

```python
release: python YourProjectName/manage.py migrate && python YourProjectName/manage.py collectstatic --noinput
web: gunicorn --pythonpath YourProjectName YourProjectName.wsgi
```

## 4. Install required packages

Install required packages and add them to `requirements.txt` file in root folder.

```python
pip install gunicorn django-heroku whitenoise dj-database-url
pip freeze > requirements.txt
```

## 5. Add Database on Heroku app

In `heroku.com` app overview add-ons choose Heroku Postgres database.

## 6. Configure Django settings

Adapt `setting.py` file for deploy on Heroku. Add imports:

```python
import django_heroku
import os
import dj_database_url
```

Comment out a secret key line

```python
# SECRET_KEY = local_settings.SECRET_KEY
```

Set `DEBUG` to `False`

```python
DEBUG = False
```

Add whitenoise package:

```python
MIDDLEWARE = [
    # ...
    'whitenoise.middleware.WhiteNoiseMiddleware',
```

Configure database

```python
DATABASES = {
    'default': dj_database_url.config(default=os.environ.get('DATABASE_URL'))
}
```

Configure static files

```python
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Whitenoise settings
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
WHITENOISE_MANIFEST_STRICT = False
WHITENOISE_USE_FINDERS = True
WHITENOISE_INDEX_FILE = True
WHITENOISE_AUTOREFRESH = True
WHITENOISE_MIMETYPES = (
    ('application/font-woff', 'application/font-woff'),
    # Add other mimetypes as needed
)
```

Add `django_heroku` to the end of settings file. It effectively sets up the project to run smoothly on Heroku.

```python
django_heroku.settings(locals())
```

## 7. Configure secret key

Create `.env` file in project root folder next to `manage.py` file. Make sure it is in `gitignore`. Add the secret key from `local_settings.py`.

```python
SECRET_KEY = 'YourSecretKeyFromLocalSettings'
```

Then add the same secret key to Heroku's Config Vars in Heroku app on `heroku.com`.

Push all the changes to Github.

## 8. Deploy on Heroku

On your Heroku app choose depoyment method from Github and connect your repository, choose the branch and click on `Deploy Branch` button. The Django app should be successfully deployd on Heroku without database data.

## 8. Export your local database

If your data is in a local database and you want to move it to the Heroku database, you can use Django's built-in dumpdata management command to export your data to a JSON. For example, to export the data to a JSON file named data.json, you can run the following command:

```python
python manage.py dumpdata > data.json
```

Push to Github and deploy branch again.

Now open Heroku console (in Heroku app page click on `More` on the right corner and then on `Run console`) and write:

```python
python YourProjectName/manage.py loaddata YourProjectName/data.json
```

After this, you should see all data pushed to Heroku app. **Good luck!**