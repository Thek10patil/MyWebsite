# MyWebsite
Developed a website using Django.

###Some useful commands##

To create virutal env
mkvirtualenv py1

workon py1

pip install django



django-admin startproject djangoproject



for making migrations 
python manage.py migrate


to login into localhost:8000/admin
need to create superuser
python manage.py createsuperuser --username=kp --email=kkp151993@gmail.com
passowrd: Test_123


Now created new application ----> posts
now add that applicaiton in seting.py
In addition to that in urls.py need to nevigates all requests of posts apps to urls.py of posts



For creation of migration file
python manage.py makemigrations projects 


For making tables inside DB 
python manage.py migrate
