from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = "review"
urlpatterns = [

    path('', views.index, name='index'),

    path('<int:catid>/', views.index, name='index'),
]