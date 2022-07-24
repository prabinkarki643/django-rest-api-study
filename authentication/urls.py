from authentication.classes.custom_auth_token import CustomAuthToken
from . import views
from django.urls import path
from rest_framework.authtoken import views as authTokenViews


urlpatterns = [

]

urlpatterns += [
    path('login', CustomAuthToken.as_view()),
    path('get_details_from_token',views.get_details_from_token)
]
