from rest_framework.viewsets import ModelViewSet
from .models import Product
from .serializer import ProductSerializer


# Create your views here.
class ProductViewSet (ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

