from django.urls import path
from .views import fees


urlpatterns = [
    path("fees/", view=fees)
]
