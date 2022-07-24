from . import views
from django.urls import path
from rest_framework import routers

router = routers.SimpleRouter(trailing_slash=False)
router.register(r'', views.BookViewSet, basename='book')

urlpatterns = router.urls

urlpatterns+=[
    path('get-books',views.BookView.get)
]