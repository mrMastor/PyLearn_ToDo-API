from rest_framework.routers import DefaultRouter
from .views import ItemViewSet

router = DefaultRouter(trailing_slash=True)

app_name = "mylist"

router.register(
    prefix="tasks",
    viewset=ItemViewSet,
    basename="tasks",
)

urlpatterns = router.urls
