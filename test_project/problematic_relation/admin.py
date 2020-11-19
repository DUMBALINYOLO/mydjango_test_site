from django.contrib import admin
from .models import StudentClass, Subject, Mbalisi, ClassSubject, StudentEnrollment, StudentSubject 

# Register your models here.


admin.site.register(Subject)
admin.site.register(StudentClass)
admin.site.register(Mbalisi)
admin.site.register(ClassSubject)
admin.site.register(StudentEnrollment)
admin.site.register(StudentSubject )
