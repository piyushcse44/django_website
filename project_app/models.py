from django.db import models
from django.core.validators import MaxValueValidator
import uuid

# Create your models here.

class project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True,blank=True)
    demo_link = models.CharField(max_length=2000,null=True,blank=True)
    source_link = models.CharField(max_length=2000)
    Tags = models.ManyToManyField('Tag',blank='True')
    vote_total = models.IntegerField(default=0,null='True',blank='True')
    vote_ratio = models.IntegerField(default=10,null='True',blank='True',validators=[MaxValueValidator(100)])
    date_of_creation = models.DateTimeField(auto_now_add=False)
    user_id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)

    def __str__(self):
        return self.title


class Review(models.Model):
    VOTE_TYPE = (
        ('up','up_vote'),
        ('down','down_vote'),
    )

    project = models.ForeignKey(project,on_delete = models.CASCADE)
    body = models.TextField(null =  True ,blank = True)
    value = models.CharField(max_length=100,choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add='True')
    id = models.UUIDField(default = uuid.uuid4,unique = True,primary_key= True,editable=False)

    def __str__(self):
        return self.value

class Tag(models.Model):
    name = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)

    def __str__(self):
        return(self.name)









