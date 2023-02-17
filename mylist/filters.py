from django_filters import FilterSet
from django_filters import CharFilter, BooleanFilter
from .models import ToList


class ToListFilterSet(FilterSet):
    """Набор фильров для представления для модели статей."""

    is_active = BooleanFilter(field_name="status")
    title = CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model = ToList
        fields = ["name", "status"]
