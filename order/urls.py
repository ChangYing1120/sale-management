from django.urls import path
from order import views

urlpatterns = [
    path('create-order', views.CreateOrderView.as_view(), name='create_order_view'),
    path('weekly_procurement_orders/', views.WeeklyProcurementOrderView.as_view(), name='weekly_procurement_orders'),
    path('ajax-create-order/', views.ajax_create_order, name='ajax_create_order'),
    path('ajax_weekly_procurement_orders/', views.ajax_weekly_procurement_orders, name='ajax_weekly_procurement_orders'),
    path('update-order-status/', views.update_order_status, name='update_order_status'),
    path('export_orders/', views.export_orders, name='export_orders'),
    path('reports/', views.ReportView.as_view(), name='report_view'),
    path('export_report/', views.export_report, name='export_report'),
]
