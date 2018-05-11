from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('downloads', views.downloads, name='downloads'),
    path('walkthrough', views.walkthrough, name='walkthrough'),
    path('walkthrough_install', views.walkthrough_install, name='walkthrough_install'),
    path('walkthrough_add_coin', views.walkthrough_add_coin, name='walkthrough_add_coin'),
    path('walkthrough_add_coin_1', views.walkthrough_add_coin_1, name='walkthrough_add_coin_1'),
    path('walkthrough_add_coin_2', views.walkthrough_add_coin_2, name='walkthrough_add_coin_2'),
    path('walkthrough_end', views.walkthrough_end, name='walkthrough_end'),
]
