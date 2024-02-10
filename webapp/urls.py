from django.urls import path
from webapp.views.ads_view import index, HomeView, AdsDetailView, AdsCreateView, AdsUpdateView, DeleteAdsView
from webapp.views.comment_views import CommentCreateView, CommentDeleteView

app_name = 'webapp'

urlpatterns = [
    path('', index),
    path('home/', index, name='index'),
    path('ads/list/', HomeView.as_view(), name='list'),
    path('ads/create/', AdsCreateView.as_view(), name='create_ads'),
    path('ads/<int:pk>/detail/', AdsDetailView.as_view(), name='detail_ads'),
    path('ads/<int:pk>/update/', AdsUpdateView.as_view(), name='update_ads'),
    path('ads/<int:pk>/delete/', DeleteAdsView.as_view(), name='delete_ads'),
    path('comments/<int:pk>/create/', CommentCreateView.as_view(), name='comment_create'),
    path('comments/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete')

]