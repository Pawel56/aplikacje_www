from django.urls import path, include
from . import views

urlpatterns = [
    path('persons/', views.person_list),
    path('person/<int:pk>/', views.person_detail),
    path('persons/<str:nazwa>', views.person_search),
    path('teams/', views.teams_list),
    path('team/<int:pk>/', views.team_detail),
]