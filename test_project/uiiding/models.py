from django.db import models
import uuid

def random_string():
    random_pk = str(uuid.uuid4()).replace("-", '').upper()[:10]
    return random_pk

# Create your models here.


class Mother(models.Model):
    # number = models.CharField(
    #                     str(uuid.uuid4()).replace("-", '').upper()[:20],
    #                     primary_key= True,
    #                     max_length=255, 
    #                     unique=True,
    #                     blank=True, 
    #                     default=None,
    #                 )
    # number = models.UUIDField(
    #             primary_key=True, 
    #             default= str(uuid.uuid4()).replace("-", '').upper()[:20],
    #             editable=False
    #         )
    number = models.CharField(
                        primary_key= True,
                        max_length=255, 
                        unique=True,
                        blank=True, 
                        default=random_string(),
                    )
    name = models.CharField(max_length=90)


    def __str__(self):
        return f'{self.name} {self.number}'


    

