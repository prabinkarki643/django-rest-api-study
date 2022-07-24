import uuid
from django.db import models

# Create your models here.


class BaseModel(models.Model):
    # uid = models.UUIDField(primary_key=True,editable=False,default=uuid.uuid4)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        abstract = True


class Book(BaseModel):
    title = models.CharField(max_length=100,)
    description = models.TextField()


class BookCompany(BaseModel):
    book=models.ForeignKey(Book,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    