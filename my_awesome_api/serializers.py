from rest_framework import serializers

from my_awesome_api.models import Person, Species , ocrData

class PersonSerializer(serializers.ModelSerializer):
   class Meta:
       model = Person
       fields = ('name', 'birth_year', 'eye_color', 'species')


class SpeciesSerializer(serializers.ModelSerializer):
   class Meta:
       model = Species
       fields = ('name', 'classification', 'language')


class OcrdataSerializer(serializers.ModelSerializer):
   class Meta:
       model = ocrData
       fields = ('imageUrl',)