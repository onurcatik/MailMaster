from django.urls import path
from .views import (
    send_email_view,
    success_page,
    base_page,
    recipient_list_view,
    recipient_add_view,
    recipient_edit_view,
    recipient_delete_view,
)

urlpatterns = [
    path('base/', base_page, name='base_page'),
    path('send-email/', send_email_view, name='send_email'), 
    path('success/', success_page, name='success_page'),
    path('recipients/', recipient_list_view, name='recipient_list'),
    path('recipients/add/', recipient_add_view, name='recipient_add'),
    path('recipients/edit/<int:pk>/', recipient_edit_view, name='recipient_edit'),
    path('recipients/delete/<int:pk>/', recipient_delete_view, name='recipient_delete'),
    path('dashboard/', recipient_list_view, name='dashboard'),
]
