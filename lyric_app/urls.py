from . import views
from django.urls import path


urlpatterns = [
    
    path('lyric/<int:pk>/', views.lyric_detail, name='lyric_detail'),
    path('lyric/create/', views.lyric_create, name='lyric_create'),
    path('lyric_delete/<int:pk>/', views.lyric_delete, name='lyric_delete'),
    path('lyric/edit/<int:pk>/', views.lyric_edit, name='lyric_edit'),
    path('lyric_detail/<int:pk>/', views.lyric_detail, name='lyric_detail'),
    path('lyric/user_page/', views.user_page, name='user_page'), # personal page of work
    path('', views.home, name='home'),                      # updated from path('', views.LyricList.as_view(), name='home'), by Jeff
    # path('', views.LyricList.as_view(), name='home'),     # rmoved for new index page by Jeff
    # path('genre/create/', views.GenreCreate.as_view(), name='genre_create'), # to meet unit test requirements
    path('genre_list/', views.GenreList.as_view(), name='genre_list'), # to meet unit test requirements
    path('lyric_list/', views.LyricList.as_view(), name='lyric_list'), # community page
    
]