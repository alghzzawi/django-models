from django.urls import path
from .views import HomePage,AboutPage,SnackListView

urlpatterns = [
    path("", HomePage.as_view(), name='home'),
    path('about',AboutPage.as_view(),name='about'),
    path('snake/',SnackListView.as_view(),name='snake')

]