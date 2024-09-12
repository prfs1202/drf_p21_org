from apps.models import Product
from django.db.models import IntegerChoices
from django_filters import ChoiceFilter, FilterSet


class ProductFilterSet(FilterSet):
    class Number(IntegerChoices):
        N1 = 1
        N2 = 2
        N3 = 3

    n = ChoiceFilter(choices=Number.choices)

    class Meta:
        model = Product
        fields = 'category',

    # def get_length(self, queryset, name, value):
    #     return queryset.annotate(name_length=Length('name')).filter(name_length__gte=value)
