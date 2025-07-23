from django.urls import path
from . import views
urlpatterns = [
    path('link-telegram/', views.link_telegram_account, name='link_telegram'),
    path('link-telegram-started/', views.go_to_bot, name='link_telegram-started'),
    path('client_dashboard' , views.client_dashboard , name = 'client_dashboard'),
    path('client_delete_project/<int:project_id>/', views.client_delete_project, name='client_delete_project'),
    path('client_edit_project/<int:project_id>/', views.client_edit_project, name='client_edit_project'),
    ## Admin Part
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('admin_edit_project/<int:project_id>/', views.admin_edit_project, name='admin_edit_project'),
    path('admin_delete_project/<int:project_id>/', views.admin_delete_project, name='admin_delete_project'),
]