from django.urls import include, path
from rest_framework.routers import DefaultRouter

from book import views

router = DefaultRouter()
router.register("books", views.BookViewSet)

app_name = "book"

urlpatterns = [path("", include(router.urls))]
