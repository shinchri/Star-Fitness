from django.urls import path

from .views import HomeView, MainView

app_name = 'main'

urlpatterns = [
  path('', MainView.as_view(), name="main"),
  path('home/', HomeView.as_view(), name="home"),
]