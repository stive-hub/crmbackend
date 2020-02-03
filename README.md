Setting up the project
======

- Git clone to desktop - https://github.com/bangalorebyte-cohort30-1912/crmbackend.git

- Setting up Environment (ensaure pipenv in installed) at the root of the project (where pipfile is..)

```python
$ pipenv install
$ pipenv shell
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver
```
- In the browser Open localhost:8000
  
(the google login will throw an error if url routed to 127.0.0.0:8000). this was done to make deployment easier.





