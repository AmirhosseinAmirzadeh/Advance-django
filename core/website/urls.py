from django.urls import path
from website import views

urlpatterns = [
    path('contact/create/', views.ContactCreateView.as_view(), name='contact-create')
]