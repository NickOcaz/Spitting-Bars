from . import views
from django.urls import path


urlpatterns = [
    # path('', views.GenreList.as_view(), name='home'),
    
    
    path('lyric/<int:pk>/', views.lyric_detail, name='lyric_detail'),
    path('lyric/create/', views.lyric_create, name='lyric_create'),
    path('', views.LyricList.as_view(), name='home'),
    
]