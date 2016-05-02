from django.db import models
from django.utils import timezone


class Story(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=30)
    upvotes = models.PositiveIntegerField()
    likes = models.PositiveIntegerField()
    domain = models.CharField(max_length=100)
    domainID = models.CharField(max_length =100)
    nsfw = models.BooleanField()
    archived = models.BooleanField()
    tags = models.CharField(max_length=100, blank=True)
    published_date = models.DateTimeField(blank=True, null=True)
#Reads
#Emotion Vector
    text = models.TextField()

    #def publish(self):
    #    self.published_date = timezone.now()
    #    self.save()
    def snippit(self):
        return self.text[0:250]+'...'
    
    def __unicode__(self) :
        return str(self.title)+';;'+str(self.genre)+';;'+str(self.author)

class Sims(models.Model):
    text = models.TextField()

    def __unicode__(self):
        return str(self.text)
