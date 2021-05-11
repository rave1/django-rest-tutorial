from django.db import models

# Create your models here.

GENDER_CHOICES = [
    ('m', 'male'),
    ('f','female'),
]
OCCUPATIONS = {
    ('p','plumber'),
    ('m','mechanic'),
    ('d','developer'),
    ('w','welder'),
}




class Person(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=20, null=False, default="John")
    last_name  = models.CharField(max_length=20, null=False, default="Doe")
    gender = models.CharField(choices=GENDER_CHOICES, default='not specified', max_length=10)
    occupation = models.CharField(choices=OCCUPATIONS, default='not specified', max_length=20)
    class Meta:
        ordering = ['created']
