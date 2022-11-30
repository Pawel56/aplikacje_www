from django.urls import path, include
from . import views

urlpatterns = [
    path('persons/', views.person_list),
    path('person/<int:pk>/', views.person_detail),
    path('person/update/<int:pk>/', views.person_update_delete),
    path('person/delete/<int:pk>/', views.person_update_delete),
    path('persons/<str:nazwa>', views.person_search),
    path('teams/', views.teams_list),
    path('team/<int:pk>/', views.team_detail),
]