from django.db import models
from django.db.models import fields
from rest_framework.fields import JSONField
from .models import COVIDData
from rest_framework import serializers


class StateSexSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = COVIDData
        fields = ['id_registro', 'sexo', 'entidad_res', 'municipio_res']


class StateSexAgeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = COVIDData
        fields = ['id_registro', 'sexo',
                  'entidad_res', 'municipio_res', 'edad']


class DeadPeopleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = COVIDData
        fields = ['sexo', 'edad', 'fecha_def']


class SickPeopleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = COVIDData
        fields = ['embarazo', 
                'diabetes',	
                'epoc',	
                'asma',	
                'inmusupr',	
                'hipertension',	
                'otra_com',	
                'cardiovascular',	
                'obesidad',	
                'renal_cronica',
                'tabaquismo',
                'fecha_def'
                  ]
class SectorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = COVIDData
        fields = ['sector', 
                'entidad_um'
                  ]