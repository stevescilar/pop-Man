from django.db import models

# Create your models here.
class Class(models.Model):
    name = models.CharField(max_length=50, blank=True)
    created_at = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,blank=True,null=True)
    def __str__(self):
            return self.name
    
    class Meta:
        verbose_name = 'Class'
        verbose_name_plural = 'Classes'

class Subject(models.Model):
        name = models.CharField(max_length=50, blank=True)
        subject_class = models.ForeignKey(Class, verbose_name="Class", on_delete=models.CASCADE)
        created_at = models.DateTimeField(auto_now_add=True,blank=True,null=True)
        updated_at = models.DateTimeField(auto_now=True,blank=True,null=True)

        def __str__(self):
            return self.name 

class Student(models.Model):
    name = models.CharField(max_length=50, blank=True)
    age = models.CharField(max_length=40, blank=True)
    student_class = models.ForeignKey(Class, verbose_name=("Class"), on_delete=models.CASCADE,null=True) 
    stream = models.CharField(max_length=20, blank=True)
    created_at = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,blank=True,null=True)

    def __str__(self):
            return self.name


class Parent(models.Model):
    name = models.CharField(max_length=50, blank=True)
    student_name = models.ForeignKey(Student, on_delete=models.CASCADE,null=True)
    created_at = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,blank=True,null=True)

    def __str__(self):
            return self.name

class Exam(models.Model):
        # student_name = models.ForeignKey(Student, on_delete = models.CASCADE, null=True)
        # 
        # subject_name = models.ManyToManyField(Subject,on_delete=models.CASCADE,null=True)
        score = models.IntegerField()

        def __str__(self):
            return str(self.student_name)


class Finance(models.Model):
        total_fee = models.IntegerField()
        class_name = models.ForeignKey(Class, on_delete=models.CASCADE, null=True)
        
        def __str__(self):
            return str(self.class_name)


class Staff(models.Model):
        name = models.CharField(max_length=50, blank=True)
        contact = models.CharField(max_length=12,blank=True)
        teacher_class = models.ForeignKey(Class, verbose_name=("Class"), on_delete=models.CASCADE,null=True) 
        created_at = models.DateTimeField(auto_now_add=True,blank=True,null=True)
        updated_at = models.DateTimeField(auto_now=True,blank=True,null=True)

        def __str__(self):
            return self.name