from django.urls import path
from .views import dotoListAPIView, dotoCreateView, dotoUpdateView, dotoDeleteView 



urlpatterns = [
    path('', dotoListAPIView.as_view()),
    path('create/', dotoCreateView.as_view()),
    path('<int:pk>/', dotoUpdateView.as_view()),
    path('delete/<int:pk>/', dotoDeleteView.as_view())

]