from django.shortcuts import render

# Create your views here.
def index(request):
    #home
    return render (request,'administrative/index.html')