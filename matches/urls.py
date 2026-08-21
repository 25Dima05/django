from django.urls import path
from . import views

urlpatterns = [
    path('matches/', views.matches_all_list, name='matches_all_list'),
    path('matches/live/', views.matches_live_list, name='matches_live_list'),
    path('matches/future/', views.matches_future_list, name='matches_future_list'),
    path('matches/<int:match_id>/', views.match_by_id, name='match_by_id'),
]