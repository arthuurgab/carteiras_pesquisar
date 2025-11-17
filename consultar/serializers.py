from rest_framework import serializers
from .models import Detalhes

class detalhesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Detalhes
        fields = '__all__'