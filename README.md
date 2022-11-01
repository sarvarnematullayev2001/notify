# Notify  
  



### Description  
'Notify' is among the projects, I have grown as a junior developer. At the beginning we thought, it is designed only for Novalab Tech, but in the future, we planned to add extra features and make it one of the open-source project.   
  



### User Interface  
Here you can see how user interface looks like. Login page:  
  

![login page](https://user-images.githubusercontent.com/79350805/199223286-f95cd3ea-b45d-4d57-8219-861f3dcbff6f.png){align="center"}


If you come late to your office, you can notify your HR:  
  

![lateness page](https://user-images.githubusercontent.com/79350805/199223567-6f3b906d-8e64-4de8-832a-e741f833b593.png)  


If you prefer to work from home, you may inform your HR, Project Manager or any other person through this page:  
  

![work from home](https://user-images.githubusercontent.com/79350805/199223869-1cb0d399-35a2-4681-ac94-638a802e4b00.png) 


Because of some reason, you need a break, this page is just designed for you:  
  

![take time off](https://user-images.githubusercontent.com/79350805/199223942-6f4f77a1-bcd4-49fe-bc39-4e825d3e2613.png)  


If any of your colleague behave themselves very bad and his actions make you uncomfortable, you may warn them:  
  

![warn](https://user-images.githubusercontent.com/79350805/199224005-2d3871da-8446-4a26-ae4e-3864ec5bdefa.png)


Your all remote dates, breaks, warnings, latenesses are recorded and through this page monthly and yearly statistics of that:  
  

![statistics](https://user-images.githubusercontent.com/79350805/199224072-b98ad52d-5d65-4003-83a4-7ccd48edfbc3.png)  


User detail page:  
  

![user-detail](https://user-images.githubusercontent.com/79350805/199224156-6e3794be-0fa8-45c1-bf71-2f648cf2119e.png)  


In app there is also 'Collegues', 'Teams' pages which their UI is almost same, but has different functionality:  
  

![teams](https://user-images.githubusercontent.com/79350805/199224207-2b23c898-6b87-44d1-8137-018fe5c0c16d.png)  


You may also be aware of upcoming monthly birthday date of your colleagues:  
  

![birthday](https://user-images.githubusercontent.com/79350805/199224280-5794afaf-4f22-4bbb-b6a8-0b36319f7ceb.png) 


### Technologies used:
![python](https://img.shields.io/badge/-python-grey?style=for-the-badge&logo=python&logoColor=white&labelColor=306998)
![django](https://img.shields.io/badge/-django-grey?style=for-the-badge&logo=django&logoColor=white&labelColor=092e20)
![postgresql](https://img.shields.io/badge/postgre-SQL-%23000.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![linux](https://img.shields.io/badge/linux-grey?style=for-the-badge&logo=linux&logoColor=white&labelColor=072c61)
![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)

## Connect with me  
<div align="center">
<a href="https://github.com/sarvarnematullayev2001" target="_blank">
<img src=https://img.shields.io/badge/github-%2324292e.svg?&style=for-the-badge&logo=github&logoColor=white alt=github style="margin-bottom: 5px;" />
</a>
<a href="https://www.linkedin.com/in/sarvar-nematullayev-37056424b/" target="_blank">
<img src=https://img.shields.io/badge/linkedin-%231E77B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white alt=linkedin style="margin-bottom: 5px;" />
</a>
<a href="https://gitlab.com/sarvarnematullayev2001" target="_blank">
<img src=https://img.shields.io/badge/gitlab-%2324292e.svg?&style=for-the-badge&logo=gitlab&logoColor=white alt=gitlab style="margin-bottom: 5px;" />
</a> 
</div>  

### Language: python 3.8 +

### Frameworks : Django 4+, DjangoRestFramework 3.12 +

### Deployment: gunicorn, gitlab ci/cd , supervisord

### Database : postgresql 12+

# Project Setup

#### Create Database

```bash
>>> create role oncosmetic_user with login password 'oncosmetic_password';
>>> create database oncosmetic with owner ecommerce_user;
```

#### Django install

```bash
>>> git clone 
>>> virtualenv .venv
>>> source .venv/bin/activate
>>> source conf
>>> pip install -r requirements.txt
>>> python manage.py migrate
```

# Architecture

```
.
└── apps
    └── app_name
        ├──  migrations
        ├──  __init__.py
        ├──  admin.py
        ├──  apps.py
        ├──  models.py
        ├──  serializer.py
        ├──  service.py
        ├──  tests.py
        ├──  urls.py
        ├──  views.py
    └──  config
        ├──  __init__.py
        ├──  asgi.py
        ├──  urls.py
        ├──  settings.py
        ├──  wsgi.py
        
    ├── .gitignore
    ├── .gitlab-ci.yml
    ├──  manage.py
    ├──  requirements.txt
```

### models.py

```python
from core.base_model import BaseModel
from django.db import models


class MyModel(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
```

### serializer.py

```python
from rest_framework import serializers


class MyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = 'my_model'
        fields = '__all__'  # or ['id', 'name']


class CustomSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()

```

### service.py

```python
from rest_framework.response import Response


def my_service(name: str):
    """business logicians"""
    return Response({'detail': 'successfully'}, status=200)
```

### views.py

```python
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView


class MyModelView(ModelViewSet):
    queryset = 'my_queryset'
    serializer_class = 'my_serializer_class'


class MyView(APIView):
    def post(self, request):
        serializer = 'my_serializer(request.data)'
        'serializer.is_valid(raise_exception=True)'
        return 'my_service(**serializer.validated_data)'
```

### urls.py

```python
from django.urls import path

'from .views import MyView'

urlpatterns = [
    path('my_view/', 'MyView.as_view()')
]
```

### main.urls.py

```python
from django.urls import path, include

urlpatterns = [
    path('/api/v1/{app_name}/', include('{app_name.urls}'))
]
```

# Python Code Style

#### Not recommended

```python
def db(x):
    return x * 2
```

#### Recommended

```python
def multiply_by_two(x: int) -> int:
    return x * 2
```
