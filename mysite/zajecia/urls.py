from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('persons/', views.PersonList.as_view()),
    path('person/<int:pk>/', views.PersonDetail.as_view()),
    path('persons/<str:nazwa>', views.PersonSearch.as_view()),
    path('teams/', views.TeamList.as_view()),
    path('team/<int:pk>/', views.TeamDetail.as_view()),
]