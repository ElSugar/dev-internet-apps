from django.urls import path
from . import views


urlpatterns = [
  path('', views.index, name='index'),
  path('russia/', views.russia, name='russia'),
  path('greece/', views.greece, name='greece'),
  path('scandinavia/', views.scandinavia, name='scandinavia'),
  path('china/', views.china, name='china'),
]