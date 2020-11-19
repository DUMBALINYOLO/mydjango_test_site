from django.db import models

# Create your models here.

class Mbalisi(models.Model):
    name = models.CharField(max_length=200)


    def __str__(self):
        return self.name


class Subject(models.Model):
    
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    


class StudentClass(models.Model):
    name = models.CharField(max_length=200)
    subjects = models.ManyToManyField(
        'Subject', 
        # related_name="courses",
        through='ClassSubject'
    )
    students = models.ManyToManyField(
        'm2m.Student', 
        # related_name="courses",
        through='StudentEnrollment',

    )


    def __str__(self):
        return self.name


class StudentEnrollment(models.Model):

    STATUS = [
        ('enrolled', 'ENROLLED'),
        ('disenroll', 'DISENROLLED')
    ]

    enr_klass = models.ForeignKey('StudentClass', on_delete=models.PROTECT)
    stdnt = models.ForeignKey('m2m.Student', on_delete=models.PROTECT)
    status = models.CharField(max_length=200, choices=STATUS, default="enrolled")
    enrollment_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.stdnt.__str__()} {self.enr_klass.__str__()} {self.enrollment_date}'


    class Meta:
        unique_together = [['stdnt', 'enr_klass']]




class ClassSubject(models.Model):
    STATUS =[
        ('study', "study"),
        ('none_study', 'none_study')
    ]
    subject = models.ForeignKey('Subject', on_delete=models.PROTECT)
    klass = models.ForeignKey('StudentClass', on_delete=models.PROTECT)
    subject_teacher = models.ForeignKey(
                            'Mbalisi', 
                            on_delete=models.SET_NULL,
                            related_name="taught_subjects",
                            blank=True,
                            null=True,
                        )
    status = models.CharField(max_length=200, choices=STATUS)

    class Meta:
        unique_together = [['klass', 'subject']]

    

    def __str__(self):
        return f'{self.subject.__str__()} {self.klass.__str__()}'


class StudentSubject(models.Model):
    STATUS =[
        ('study', "study"),
        ('none_study', 'none_study')
    ]
    subject = models.ForeignKey('Subject', on_delete=models.PROTECT)
    student = models.ForeignKey('m2m.Student', on_delete=models.PROTECT)
    status = models.CharField(max_length=200, choices=STATUS)

    class Meta:
        unique_together = [['student', 'subject']]

    

    def __str__(self):
        return f'{self.subject.__str__()} {self.student.__str__()}'





