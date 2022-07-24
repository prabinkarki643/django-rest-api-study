from . import views
from django.urls import path

#URLConf
urlpatterns = [
    path('hello-html-render/',views.say_hello_in_html),
    path('hello-json-render/',views.say_hello_in_json)
]