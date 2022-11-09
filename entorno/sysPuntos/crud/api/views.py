from rest_framework.viewsets import ModelViewSet
from crud.models import cliente, direccion
from crud.api.serializer import PostSerializer

class PostApiViewSet(ModelViewSet):
    serializer_class = PostSerializer
    queryset = direccion.objects.all()