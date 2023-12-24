from django.contrib import admin
from .models import Student,AdditionalInfo

@admin.register(Student)
class Student(admin.ModelAdmin):
    list_display = ['id', 'name', 'age', 'roll', 'mobile', 'email', 'city', 'state']



@admin.register(AdditionalInfo)
class AdditionalInfo(admin.ModelAdmin):
    list_display=['id','father_name','father_mobile','father_age','father_email']