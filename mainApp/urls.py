from django.urls import path, include
from . import views
from .views import Actions

urlpatterns = [
    path('actions', Actions.as_view()),
]
