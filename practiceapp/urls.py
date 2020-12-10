from django.urls import path

from . import views

app_name = "practiceapp"

urlpatterns = [
    path('', views.index, name='index'),
    path('blog_cards/', views.blog_cards, name="blog_cards"),
    path('nice_login/', views.nice_login, name="nice_login"),
    path('ads_manager/', views.ads_manager, name="ads_manager"),
]
