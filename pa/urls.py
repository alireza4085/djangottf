from django.urls import path 
from . import views
#adfkjslkfja

urlpatterns = [
    path('', views.home, name='home' ),
    path('researcher/', views.researcher, name='add researcher' ),
    path('addresearcher/', views.addresearcher, name='addresearcher'),
    path('researcher_list/', views.showResearcher, name='researcher list'),
    path('edit-researcher/<int:ID_re>/', views.edit_researcher_view, name='edit-researcher'),
    path('delete-researcher/<int:ID_re>/', views.delete_researcher_view, name='delete-researcher'),

    path('superrisor/', views.superrisor, name='add superrisor' ),
    path('addsuperrisor/', views.addsuperrisor, name='addsuperrisor'),

    path('institute/', views.institute, name='add institute' ),
    path('addinstitute/', views.addinstitute, name='addinstitute'),
    
    path('essey/', views.essey, name='add essey' ),
    path('inventions/', views.inventions, name='add inventions' ),
    path('budget/', views.budget, name='add budget' ),
    path('superrisor_list/', views.superrisor_list, name='superrisor list'),
    path('institute_list/', views.institute_list, name='institute list'),
    path('essey_list/', views.essey_list, name='essey list'),
    path('inventions_list/', views.inventions_list, name='inventions list'),
    path('budget_list/', views.budget_list, name='budget list'),
    path('personality_list/', views.personality_list, name='personality list'),
    path('activity_list/', views.activity_list, name='activity list'),
]
