from django.urls import re_path

from .views import contactform

urlpatterns = [
    re_path('contactform$', contactform)
]
