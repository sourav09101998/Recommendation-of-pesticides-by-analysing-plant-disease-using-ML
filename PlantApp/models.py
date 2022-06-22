from django.db import models

# Create your models here.
class Inferences(models.Model):

    image =  models.ImageField(upload_to='leafImages',blank=False)
    prediction = models.TextField(max_length=100,blank=False)

    def __str__(self):
        return self.prediction

class Query(models.Model):

    queryId = models.IntegerField(primary_key=True)
    query   = models.TextField(max_length=1000,blank=False)
    image   = models.ImageField(upload_to='query_images',default='media/default.jpg')


class Answer(models.Model):
    query = models.ForeignKey(Query,on_delete=models.CASCADE)
    res   = models.TextField(max_length=2000,blank=False)