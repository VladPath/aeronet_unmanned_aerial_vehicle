from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import DroneModels



# Create your views here.
def index(request):
    posts = DroneModels.published.all()
    data = {
        'title':'Каталог Российских моделей БАС',
        'post':posts
    }
    return render(request, 'BAS/index.html', context=data)

def about(request, about_slug):
    drone = get_object_or_404(DroneModels, slug = about_slug)
    posts = DroneModels.published.all()
    data = {
        'drone': drone,
        'post':posts,
    }
    return render(request, 'BAS/about.html', context=data)



