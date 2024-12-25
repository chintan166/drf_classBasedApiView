python3 -m venv env

source env/bin/activate

pip install django

django-admin startproject watchmate

cd watchmate

python3 manage.py startapp watchlist_app

python3 manage.py  makemigrations

python3 manage.py migrate

python3 manage.py createsuperuser

pip install djangorestframework

python3 manage.py runserver 8069


---------------------------------------------------------------------

**http://127.0.0.1:8071/movie/list/**

![image](https://github.com/user-attachments/assets/babee29e-2263-43c5-b9ff-aedaa00f22e5)

---------------------------------------------------------------------------
**http://127.0.0.1:8071/movie/1**

![image](https://github.com/user-attachments/assets/e2875654-02e6-4c40-b670-d593fd3fc0ce)



