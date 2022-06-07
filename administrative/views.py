from django.shortcuts import render
from . models import Student,Staff
# Create your views here.
def dashboard(request):
    total_students = Student.objects.all()
    total_staff = Staff.objects.all()
    context = {
        'total_students':total_students,
        'total_staff': total_staff
    }
    return render(request, 'administrative/index.html',context)