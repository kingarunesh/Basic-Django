from django.urls import path
from .views import course


urlpatterns = [
    path("course", view=course, name="course")
]
