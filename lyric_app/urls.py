from . import views
from django.urls import path


urlpatterns = [
    # path('', views.GenreList.as_view(), name='home'),
    path('lyric/<int:pk>/', views.lyric_detail, name='lyric_detail'),
    path('lyric/create/', views.lyric_create, name='lyric_create'),
    path('lyric/delete/<int:pk>/', views.lyric_delete, name='lyric_delete'),
    path('lyric/edit/<int:pk>/', views.lyric_edit, name='lyric_edit'),
    path('lyric_detail/<int:pk>/', views.lyric_detail, name='lyric_detail'),
    path('lyric/user_page/', views.user_page, name='user_page'),
    path('', views.LyricList.as_view(), name='home'),
    
]