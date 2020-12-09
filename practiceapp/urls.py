from django.urls import path

from . import views

app_name = "practiceapp"

urlpatterns = [
    path('', views.index, name='index'),
    path('blog_cards/', views.blog_cards, name="blog_cards"),
]
