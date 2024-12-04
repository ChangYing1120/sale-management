from django.urls import path
from servicecall import views

urlpatterns = [
    path('maintenance-call', views.ServiceCallView.as_view(), name='maintenance_call'),
    path('ajax_create_service_call/', views.ajax_create_service_call, name='ajax_create_service_call'),
]
