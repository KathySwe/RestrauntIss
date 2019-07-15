from django.db import models

# Create your models here.
from django.db import models


class Category(models.Model):
    Cname = models.CharField(max_length=100)
    Cid = models.IntegerField(default=0)

    def __str__(self):
        return '{}/{}'.format(self.Cname,self.Cid)

class Restaurant(models.Model):
    Cid = models.ForeignKey(Category,on_delete=models.Aggregate)
    Rname = models.CharField(max_length=200)
    Rid = models.IntegerField(default=0)
    Radd=models.CharField(max_length=300)

    def __str__(self):
        return '{}/{}/{}/{}'.format(self.Rid,self.Rname,self.Radd,self.Cid)

class Review(models.Model):
    Rvname = models.CharField(max_length=200)
    Rvid = models.IntegerField(default=0)
    Rating = models.IntegerField(default=0)
    Rid = models.ForeignKey(Restaurant,on_delete=models.Aggregate)

    def __str__(self):
        return '{}/{}/{}/{}'.format(self.Rvid,self.Rvname,self.Rating,self.Rid)

class Comment(models.Model):
    Comid = models.IntegerField(default=0)
    Ce_text = models.CharField(max_length=200)
    Rvid= models.ForeignKey(Review,models.Aggregate)

    def __str__(self):
        return '{}/{}/{}'.format(self.Comid,self.Ce_text,self.Rvid)


