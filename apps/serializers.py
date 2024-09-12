from django.contrib.auth.hashers import make_password
# from django_elasticsearch_dsl_drf.serializers import DocumentSerializer
from rest_framework import serializers
from rest_framework.fields import CharField

from apps.documents import ProductDocument
from apps.models import Category, Product, User


# class ProductDocumentSerializer(DocumentSerializer):
#     class Meta:
#         document = ProductDocument
#
#         fields = (
#             'id',
#             'name',
#             'description'
#         )

class RegisterUserModelSerializer(serializers.ModelSerializer):
    confirm_password = CharField(write_only=True)

    class Meta:
        model = User
        fields = 'id', 'first_name', 'last_name', 'username', 'password', 'confirm_password'

        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, attrs):
        confirm_password = attrs.pop('confirm_password')
        if confirm_password != attrs.get('password'):
            raise serializers.ValidationError('Passwords did not match!')
        attrs['password'] = make_password(confirm_password)
        return attrs


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = 'id', 'first_name', 'last_name', 'username', 'type', 'email', 'date_joined'


class CategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = 'id', 'name', 'slug'
        read_only_fields = 'slug',


class ProductModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = 'updated_at',
        read_only_fields = 'slug',

    def to_representation(self, instance: Product):
        repr = super().to_representation(instance)
        repr['category'] = CategoryModelSerializer(instance.category).data
        repr['owner'] = UserModelSerializer(instance.owner).data
        return repr
