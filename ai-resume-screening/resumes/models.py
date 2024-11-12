# resumes/models.py
from django.db import models

class Candidate(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    skills = models.TextField()
    years_of_experience = models.IntegerField()

    def __str__(self):
        return self.name
