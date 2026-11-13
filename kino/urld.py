from django.urls import path
from .views import *


urlpatterns = [
    path('', create_garn),
    path('films/', show_films, name='show_films'),

    path('comments/', show_comments, name='show_comments'),

    path('ganr/', show_ganr, name='show_ganr'),
    path('add_film/', create_film, name='add_film'),


    path('add_comment/', create_comment, name='create_comment'),
    path('film/<int:id>/', detail_film, name='detail_film'),
    path('del_film/<int:id>/', delete_film, name='delete_film'),

    path('comment/<int:id>/', detail_comment, name='detail_comment'),

    path('del_comment/<int:id>/', delete_comment, name='delete_comment'),
    path('ganr/<int:id>/', detail_ganr, name='detail_ganr'),

    path('del_ganr/<int:id>/', delete_ganr, name='delete_ganr'),
]
