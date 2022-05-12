from rest_framework.viewsets import ModelViewSet

from .models import Product
from .serializers import ProductSerializer, ProductListSerializer, ProductDetailSerializer

class ProfessionalViewSet(ModelViewSet):

    queryset = Product.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return ProductSerializer
        elif self.action == 'retrieve':
            return ProductDetailSerializer
        elif self.action == 'list':
            return ProductListSerializer
        elif self.action == 'update' or self.action == 'destroy':
            return ProductSerializer
