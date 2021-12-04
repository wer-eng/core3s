from django.db.models.fields import CharField
import django_filters
from django_filters.filters import CharFilter 
from .models import Student

    
class StudentFilter (django_filters.FilterSet):
    TYPE={
        ('firstName','firstName')
    }
    status = django_filters.ChoiceFilter(choices=TYPE)
    firstName = django_filters.CharFilter(lookup_expr='icontains')
    lastname = django_filters.CharFilter(lookup_expr='icontains')
    TC = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model=  Student
        feilds=('firstName','lastName','TC')
        exclude=('image')
    