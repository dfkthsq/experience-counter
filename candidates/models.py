from django.db import models

# Create your models here.


class Candidate(models.Model):
    name = models.CharField(max_length=30)
    totalExperience = models.IntegerField()
    workExperience = models.JSONField()

    def __str__(self):
        return self.name
