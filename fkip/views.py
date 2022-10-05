from operator import index
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'buka.html')