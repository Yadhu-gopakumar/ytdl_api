from .views import api
from django.urls import path
urlpatterns = [
    path('ytdlapi/',api,name='api')

]
