from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import DroneModels

data_db = [
    {'id': 1, 'title': 'Геоскан LITE', 'content': '''Геоскан LITE информация.''','img':'BAS/images/geoskan_lite.png',
     'is_published': True},
    {'id': 2, 'title': 'Геоскан 201', 'content': 'Геоскан 201 информация', 'img':'BAS/images/geoskan_201.png', 'is_published': False},
    {'id': 3, 'title': 'Геоскан 701', 'content': 'Геоскан 701 Информация', 'img':'BAS/images/geoskan_701.png', 'is_published': True},
    {'id': 4, 'title': 'Геоскан 401', 'content': 'Геоскан 401 Информация', 'img':'BAS/images/geoskan_401.png', 'is_published': True},
    {'id': 5, 'title': 'Геоскан 401', 'content': 'Геоскан 401 Информация', 'img':'BAS/images/geoskan_401.png', 'is_published': True},
]


# Create your views here.
def index(request):
    posts = DroneModels.published.all()
    data = {
        'title':'Каталог Российских моделей БАС',
        'data': data_db,
        'post':posts
    }
    return render(request, 'BAS/index.html', context=data)

def about(request, about_slug):
    drone = get_object_or_404(DroneModels, slug = about_slug)
    posts = DroneModels.published.all()
    data = {
        'title':'Каталог Российских моделей БАС',
        'data': data_db,
        'drone': drone,
        'post':posts
    }
    return render(request, 'BAS/about.html', context=data)



