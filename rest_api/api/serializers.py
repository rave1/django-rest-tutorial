from rest_framework import serializers
from api.models import Person, GENDER_CHOICES, OCCUPATIONS

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['id', 'created','first_name','last_name','gender' ,'occupation']