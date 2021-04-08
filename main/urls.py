from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('index/', views.index, name='index'),
    path('detail/<int:id>', views.detail, name='detail'),
    path('ask/', views.ask, name='ask'),

]
