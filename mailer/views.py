import os
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.core.files.storage import FileSystemStorage
from django.template.loader import get_template
from django.conf import settings
from .models import Recipient
from .forms import RecipientForm


# Define a directory to store email templates
TEMPLATE_STORAGE_DIR = os.path.join(settings.BASE_DIR, 'email_templates')

'''
def recipient_list_view(request):
    recipients = Recipient.objects.all()
    return render(request, 'recipient_list.html', {'recipients': recipients})

'''
def recipient_list_view(request):
    recipients = Recipient.objects.all()
    return render(request, 'dashboard.html', {'recipients': recipients})


def recipient_add_view(request):
    if request.method == 'POST':
        form = RecipientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('recipient_list')
    else:
        form = RecipientForm()
    return render(request, 'recipient_form.html', {'form': form})

def recipient_edit_view(request, pk):
    recipient = get_object_or_404(Recipient, pk=pk)
    if request.method == 'POST':
        form = RecipientForm(request.POST, instance=recipient)
        if form.is_valid():
            form.save()
            return redirect('recipient_list')
    else:
        form = RecipientForm(instance=recipient)
    return render(request, 'recipient_form.html', {'form': form})

def recipient_delete_view(request, pk):
    recipient = get_object_or_404(Recipient, pk=pk)
    if request.method == 'POST':
        recipient.delete()
        return redirect('recipient_list')
    return render(request, 'recipient_delete.html', {'recipient': recipient})

def send_email_view(request):
    if request.method == 'POST':
        recipients = Recipient.objects.all()
        
        # Render email content
        subject = "Monthly Newsletter"
        from_email = settings.EMAIL_HOST_USER
        text_content = 'This is an important message.'
        
        for recipient in recipients:
            html_content = render_to_string('newsletter.html', {'recipient_name': recipient.name})
            email = EmailMultiAlternatives(subject, text_content, from_email, [recipient.email])
            email.attach_alternative(html_content, "text/html")
            email.send(fail_silently=False)
        
        return redirect('success_page')

    return render(request, 'send_email.html')


def success_page(request):
    return render(request, 'success.html')


def base_page(request):
    return render(request, 'base.html')





  