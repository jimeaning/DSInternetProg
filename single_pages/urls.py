# single_pages 아래 있는 urls.py
# single_pages는 템플릿이랑 urls랑 views만 !

from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing),
    path('about_me/', views.about_me)
]