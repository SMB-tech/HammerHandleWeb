from django.shortcuts import render
#from arches.app.models.system_settings import settings

def index(request):
    return render(request, 'index.htm')
