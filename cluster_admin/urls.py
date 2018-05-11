from django.urls import path
from django.conf.urls import include
from . import views

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('overview/', views.overview),
    path('create/', views.Create_Cluster.as_view(), name='create_cluster')
]
