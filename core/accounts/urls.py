from django.urls import path, include


urlpatterns = [
    path('api/v2/', include('djoser.urls')),
    path('api/v2/', include('djoser.urls.jwt')),
]