from django.urls import path
from .views import send_email_view, add_person, person_list, success_page
 

urlpatterns = [
    path('send-email/', send_email_view, name='send_email'),
    path('add-person/', add_person, name='add_person'),
    path('person-list/', person_list, name='person_list'),
    path('success/', success_page, name='success_page'),
    #path('schedule-email/', schedule_email_view, name='schedule_email'),
    #path('email-scheduled/', email_scheduled, name='email_scheduled'),
]