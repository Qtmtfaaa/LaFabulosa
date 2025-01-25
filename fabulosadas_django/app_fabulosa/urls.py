from django.urls import path
from app_fabulosa import views

urlpatterns = [
    path('', views.index, name='index'),
    path('retos/', views.retos, name='RetosFabulosos')
]
