from django.db.models import Q
from rest_framework import viewsets, generics, permissions, decorators, response
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .models import Product
from .serializers import ProductSerializer, RegisterSerializer
from .permissions import IsAuthenticatedOrReadOnly


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filterset_fields = ['category']
    search_fields = ['name', 'category']
    ordering_fields = ['price', 'created_at', 'updated_at', 'name']


@decorators.action(detail=False, methods=['get'], url_path='search', permission_classes=[permissions.AllowAny])
def search(self, request):
    q = request.query_params.get('q', '')
    category = request.query_params.get('category')
    qs = self.get_queryset()
    if q:
        qs = qs.filter(Q(name__icontains=q) | Q(description__icontains=q) | Q(category__icontains=q))
    if category:
        qs = qs.filter(category__iexact=category)
        page = self.paginate_queryset(qs)
    if page is not None:
        ser = self.get_serializer(page, many=True)
        return self.get_paginated_response(ser.data)
        ser = self.get_serializer(qs, many=True)
    return response.Response(ser.data)
