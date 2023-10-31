from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'icon_click/index.html')
