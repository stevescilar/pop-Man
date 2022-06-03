from django.contrib import admin
from . models import Student,Class,Subject,Finance
# Register your models here.

class FinanceAdmin(admin.ModelAdmin):
    list_display = ('class_name','total_fee')
admin.site.register(Student)
admin.site.register(Class)
admin.site.register(Subject)
admin.site.register(Finance,FinanceAdmin)
