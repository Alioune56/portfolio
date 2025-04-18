from django.db import models

class Experience(models.Model):
    date = models.CharField(max_length=50)
    poste = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    lieu = models.CharField(max_length=100)

class Education(models.Model):
    date = models.CharField(max_length=50)
    ecole = models.CharField(max_length=100)
    lieu = models.CharField(max_length=100)
    poste = models.CharField(max_length=100)
