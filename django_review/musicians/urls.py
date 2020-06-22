from django.urls import path
from . import views

app_name = "musicians"

urlpatterns = [
    path('', views.index, name="index"),
    path('<int:musician_pk>/', views.detail, name="detail"),
]