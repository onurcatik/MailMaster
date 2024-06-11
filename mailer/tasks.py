from celery import shared_task
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

@shared_task
def send_mass_email(subject, message, from_email, recipient_list):
    context = {
        'subject': subject,
        'message': message,
        'from_name': from_email.split('@')[0]  # Just an example, modify as needed
    }
    
    html_content = render_to_string('email_template.html', context)
    
    for recipient in recipient_list:
        msg = EmailMultiAlternatives(subject, message, from_email, [recipient])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
