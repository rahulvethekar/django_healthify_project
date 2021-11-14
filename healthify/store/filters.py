import django_filters
from .models import Product
catagory_choices = (

    ('Covid Essentials','Covid Essentials'),
    ('Personal Care','Personal Care'),
    ('Home Care','Home Care'),
    ('Nutrition & Fitness Supplements','Nutrition & Fitness Supplements'),


)

class ProductFilter(django_filters.FilterSet):

    Category = django_filters.ChoiceFilter(choices = catagory_choices,label = 'Filter by Category')
    Price = django_filters.RangeFilter(label='Filter by Price')

    class Meta:
        model = Product
        fields = ('Category','Price')
