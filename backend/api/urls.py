from django.urls import path
from .views import get_sentiment

urlpatterns = [
    path('predict/', get_sentiment),
]
