django-admin startproject myfirstapi
cd myfirstapi

python3 ./manage.py startapp firstapp
cd myfirstapi
#add firstapp and rest_framework to settings.py installed apps

#make migrations
python3 manage.py makemigrations
python3 manage.py migrate
#python3 ../manage.py makemigrations firstapp



#run server
python3 ../manage.py runserver