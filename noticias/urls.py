from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('artigos', views.titulos, name='artigos'),
    path('artigos/<int:titulo_id>/', views.corpo, name='article_detail'),
]
