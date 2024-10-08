from .views import HomePageView, ContactPageView, CategoryPageView, SinglePageView, news_list
from django.urls import path, include


urlpatterns = [
    path('',HomePageView.as_view(), name="home"),
    path('news/',news_list, name='news'),
    path('category/',CategoryPageView.as_view(), name='category'),
    path('single/',SinglePageView.as_view(), name='single'),
    path('contact/',ContactPageView.as_view(), name='contact')
]