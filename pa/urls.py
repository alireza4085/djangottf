from django.urls import path 
from . import views


urlpatterns = [
    path('', views.home, name='home' ),
    path('researcher/', views.researcher, name='add researcher' ),
    path('addresearcher/', views.addresearcher, name='addresearcher'),
    path('researcher_list/', views.showResearcher, name='researcher list'),
    path('edit-researcher/<int:ID_re>/', views.edit_researcher_view, name='edit-researcher'),
    path('delete-researcher/<int:ID_re>/', views.delete_researcher_view, name='delete-researcher'),


    path('superrisor/', views.superrisor, name='add superrisor' ),
    path('addsuperrisor/', views.addsuperrisor, name='addsuperrisor'),
    path('superrisor_list/', views.showsuperrisor, name='superrisor list'),
    # path('edit-superrisor/<int:ID_in>/', views.edit_superrisor_view, name='edit-superrisor'),
    path('delete-superrisor/<int:ID_su>/', views.delete_superrisor_view, name='delete-superrisor'),


    path('institute/', views.institute, name='add institute' ),
    path('addinstitute/', views.addinstitute, name='addinstitute'),
    path('institute_list/', views.showinstitute, name='institute list'),
    # path('edit-institute/<int:ID_in>/', views.edit_institute_view, name='edit-institute'),
    path('delete-institute/<int:ID_in>/', views.delete_institute_view, name='delete-institute'),


    path('essey/', views.essey, name='add essey' ),
    path('addessey/', views.addessey, name='addessey'),
    path('essey_list/', views.showessey, name='essey list'),
    # path('edit-essey/<int:ID_es>/', views.edit_essey_view, name='edit-essey'),
    path('delete-essey/<int:ID_es>/', views.delete_essey_view, name='delete-essey'),


    path('inventions/', views.inventions, name='add inventions' ),
    path('addinventions/', views.addinventions, name='addinventions'),
    path('inventions_list/', views.showinventions, name='inventions list'),
    # path('edit-inventions/<int:ID_inven>/', views.edit_inventions_view, name='edit-inventions'),
    path('delete-inventions/<int:ID_inven>/', views.delete_inventions_view, name='delete-inventions'),
    
    
    path('budget/', views.budget, name='add budget' ),
    path('addbudget/', views.addbudget, name='addbudget'),
    path('budget_list/', views.showbudget, name='budget list'),
    # path('edit-inventions/<int:ID_inven>/', views.edit_inventions_view, name='edit-inventions'),
    path('delete-budget/<int:deposit_ID>/', views.delete_budget_view, name='delete-budget'),

    
    path('superrisor_list/', views.superrisor_list, name='superrisor list'),
    
    path('institute_list/', views.institute_list, name='institute list'),
    
    path('essey_list/', views.essey_list, name='essey list'),
    
    path('inventions_list/', views.inventions_list, name='inventions list'),
    
    path('budget_list/', views.budget_list, name='budget list'),
    
    path('personality_list/', views.personality_list, name='personality list'),
    
    path('activity_list/', views.activity_list, name='activity list'),
]
