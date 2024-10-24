from django.urls import path
from .views import indexView

urlpatterns = [
    path('fbv-index/', indexView, name='fbv-index'),
]