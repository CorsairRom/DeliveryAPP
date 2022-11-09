from rest_framework.serializers import ModelSerializer
from crud.models import cliente, direccion

class PostSerializer(ModelSerializer):
    class Meta:
        model = direccion
        field = ['nombre', 'descripcion']
        exclude = ['id']