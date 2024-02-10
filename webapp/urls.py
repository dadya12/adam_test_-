from django.urls import path
from webapp.views import homepage

app_name = 'webapp'

urlpatterns = [
    path('', homepage),
    path('home/', homepage, name='index')
]