## djangoRealEsate
#### This repo is for a django demo real estate application. Fully developed by following below training course
https://udemy.com/course/python-django-dev-to-deployment


## Components
Python, django, PostgreSQL, Boostrap, Heroku

### Preview
<img src="preview.png">

Live link : https://btrealestate.herokuapp.com/




Notes for my own reference:
python manage.py runserver to run in local.
App Logic starts from RealEstate\urls.py.
Based on the url pattern a view function is called, view function will do any oprations(eg:pulling data, filtering it as needed etc) if required, and then renders a template. When rendering template, it can pass data object into the template, So the template will be rendered with that data.In the template there can be links to navigate to another page like this --> {%url 'search'%}. It calls the view function in the url pattern with is named as 'search' and call it (i think it looks in all apps url.pys for finding a match, not sure). Forms submissions are also done like this. Also the templates extend a base template, which has blocks which are replaced by the extending template


