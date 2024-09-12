# from re import search

# from django_elasticsearch_dsl_drf.filter_backends import SearchFilterBackend, SuggesterFilterBackend
# from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
from rest_framework.filters import SearchFilter
from rest_framework.generics import CreateAPIView, ListCreateAPIView
from rest_framework.permissions import AllowAny

from apps.documents import ProductDocument
from apps.models import Category, Product, User
from apps.paginations import CustomPageNumberPagination
from apps.serializers import (
    CategoryModelSerializer,
    ProductModelSerializer,
    RegisterUserModelSerializer,
    UserModelSerializer
)

#
# class ProductDocumentViewSet(DocumentViewSet):
#     document = ProductDocument
#     serializer_class = ProductDocumentSerializer
#
#     filter_backends = [
#         SearchFilterBackend,
#         SuggesterFilterBackend
#     ]
#     search_fields = ('name', 'description')


class UserListAPIView(ListCreateAPIView):
    queryset = User.objects.order_by('id')
    serializer_class = UserModelSerializer
    pagination_class = CustomPageNumberPagination

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


class CategoryListCreateAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer


class ProductListCreateAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name', 'description']
    # permission_classes = IsAuthenticated,


class RegisterCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterUserModelSerializer
    permission_classes = AllowAny,
