from django.urls import path
from .views import RetrieveResponseView

urlpatterns = [
    path('response/', RetrieveResponseView.as_view(), name='response-retrieve'),
]