from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(
        Person,
        through='Membership',
        through_fields=('group', 'person'),
    )

    def __str__(self):
        return self.name

class Membership(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    inviter = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name="membership_invites",
    )
    invite_reason = models.CharField(max_length=64)

    def __str__(self):
        return self.id


class Student(models.Model):
    name = models.CharField(max_length=200)
    subjects = models.ManyToManyField(
                            'problematic_relation.Subject',
                            through='problematic_relation.StudentSubject'

                        )

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=200)
    students = models.ManyToManyField(
        'Student', 
        # related_name="courses",
        through='Enrollment'
    )


    def __str__(self):
        return self.name



class Enrollment(models.Model):

    student = models.ForeignKey('Student', on_delete=models.PROTECT)
    course = models.ForeignKey('Course', on_delete=models.PROTECT)
    date_enrolled = models.DateTimeField(auto_now_add=True)
    final_grade = models.CharField(max_length=340, blank=True, null=True)


    class Meta:
        unique_together = [['student', 'course']]


    def __str__(self):
        return self.student.__str__()




# class StudentClass(models.Model)











