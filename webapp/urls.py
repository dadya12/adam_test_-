from django.urls import path
from webapp.views.ads_view import index, HomeView, AdsDetailView, AdsCreateView

app_name = 'webapp'

urlpatterns = [
    path('', index),
    path('home/', index, name='index'),
    path('ads/list/', HomeView.as_view(), name='list'),
    path('ads/create/', AdsCreateView.as_view(), name='create_ads'),

]