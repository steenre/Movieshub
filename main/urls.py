from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='landing'),
    path('movie/<int:movie_id>', views.movie, name='movie'),
    # path('', views.index, name='landing'),
    # path('', views.index, name='landing'),
]
