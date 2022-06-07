from django.shortcuts import render
from . models import Student
# Create your views here.
def dashboard(request):
    total_students = Student.objects.all()
    context = {
        'total_students':total_students
    }
    return render(request, 'administrative/index.html',context)