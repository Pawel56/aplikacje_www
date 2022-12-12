from django.urls import path, include
from . import views

urlpatterns = [
    path('persons/', views.person_list),
    path('person/<int:pk>/', views.person_detail),
    path('person/update/<int:pk>/', views.person_update),
    path('person/delete/<int:pk>/', views.person_delete),
    path('persons/<str:nazwa>', views.person_search),
    path('teams/', views.teams_list),
    path('team/<int:pk>/', views.team_detail),
    path('druzyna/<int:pk>/czlonkowie', views.team_persons_list),
]