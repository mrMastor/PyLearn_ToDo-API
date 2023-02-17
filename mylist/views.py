from django.shortcuts import render
from django.views.generic import (
    DetailView,
    CreateView,
    ListView,
    UpdateView,
    DeleteView,
)
from mylist.models import ToList
from django.urls import reverse_lazy
from rest_framework import viewsets
from .serializers import ItemSerializer
from .filters import ToListFilterSet


def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    # Генерация "количеств" некоторых главных объектов
    count_item = ToList.objects.all().count()
    # Не выполненные задачи
    count_item_false = ToList.objects.filter(status=False).count()
    return render(
        request,
        "index.html",
        context={"count_item": count_item, "count_item_false": count_item_false},
    )


class ListListView(ListView):
    model = ToList
    fields = ["status", "name"]
    context_object_name = "full_lists"
    template_name = "todolist_full.html"


class ListViewFalse(ListView):
    model = ToList
    context_object_name = "list_false"
    queryset = ToList.objects.filter(status=False)
    template_name = "todolist.html"


class ItemCreateView(CreateView):
    model = ToList
    context_object_name = "add_item"
    fields = ["status", "name"]
    prepopulated_fields = {"slug": ["name"]}
    template_name = "item_create.html"


class ItemDetailView(DetailView):
    model = ToList
    context_object_name = "item_detail"
    template_name = "item_detail.html"


class ItemUpdateView(UpdateView):
    model = ToList
    fields = ["status", "name", "slug"]
    readonly_fields = (
        "date_create",
        "date_complite",
    )
    context_object_name = "item_update"
    template_name = "item_update.html"


class ItemDeleteView(DeleteView):
    model = ToList
    template_name = "item_delete.html"
    context_object_name = "item_delete"
    success_url = reverse_lazy("index")


class ItemViewSet(viewsets.ModelViewSet):
    queryset = ToList.objects.all()
    serializer_class = ItemSerializer
    filterset_class = ToListFilterSet

    def update(self, request, *args, **kwargs):
        if request.data.__contains__("name") == False:
            try:
                old_name = ToList.objects.get(id=self.kwargs["pk"])
                request.data["name"] = str(old_name.name)
                return super().update(request, *args, **kwargs)
            except:
                return super().update(request, *args, **kwargs)
        else:
            return super().update(request, *args, **kwargs)
