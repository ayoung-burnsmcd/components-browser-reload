# Django Project Template

This is a standard [Django project
template](https://docs.djangoproject.com/en/4.2/ref/django-admin/#startproject)
that can be used to diagnose an issue when [Django
Components](https://github.com/EmilStenstrom/django-components) and [Django
Browser Reload](https://github.com/adamchainz/django-browser-reload) are used at the same time.

```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py runserver
```

Open it at http://127.0.0.1:8000/ .

When you first run this project django-browser-reload will be commented out of the `example/settings.py` and `example/urls.py` files.

Change the `value` at `line 12` of `components/test/test.py` to any value other than `foo` and refresh the browser to see the update.

To enable django-browser-reload, stop the server, remove the comments at `lines 39 & 52` of `example/settings.py` and `line 23` of `example/urls.py`, restart the server.

If you try and change the value in `components/test/test.py` it will not update on browser refresh any longer. Stopping and starting the server is the only way to get the updates out of the `test.py` file.

Disabling django-browser-reload again brings the functionality back.
