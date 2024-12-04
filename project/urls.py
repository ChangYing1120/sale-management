from django.urls import path
from project import views

urlpatterns = [
    path('', views.Home.as_view(), name='main'),
    path('ajax-create-project/', views.ajax_create_project, name='ajax_create_project'),
    path('ajax-update-status-project/', views.ajax_update_status_project, name='ajax_update_status_project'),
    path('ajax_get_project/', views.ajax_get_project, name='ajax_get_project'),
    path('ajax_update_project/', views.ajax_update_project, name='ajax_update_project'),
]
