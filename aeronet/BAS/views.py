from django.http import HttpResponse
from django.shortcuts import render

data_db = [
    {'id': 1, 'title': 'Геоскан LITE', 'content': '''Геоскан LITE информация.''','img':'BAS/images/background_1.jpg',
     'is_published': True},
    {'id': 2, 'title': 'Геоскан MAX', 'content': 'Геоскан MAX информация', 'img':'BAS/images/background_1.jpg', 'is_published': False},
    {'id': 3, 'title': 'Геоскан STANDART', 'content': 'Геоскан STANDART Информация', 'img':'BAS/images/background_1.jpg', 'is_published': True},
]


# Create your views here.
def index(request):
    
    data = {
        'title':'Каталог Российских моделей БАС',
        'data': data_db,
    }
    return render(request, 'BAS/index.html', context=data)



