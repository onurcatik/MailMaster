from django.shortcuts import render, redirect
from .tasks import send_mass_email
from .forms import PersonForm
from .models import Person
from django.http import HttpResponse

def send_email_view(request):
    if request.method == 'POST':
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        from_email = request.POST.get('from_email')
        recipient_list = request.POST.getlist('recipient_list')
        
        send_mass_email.delay(subject, message, from_email, recipient_list)
        return redirect('success_page')

    return render(request, 'send_email.html')

def schedule_email(request):
    return render(request, 'schedule_email.html')

def success_page(request):
    return render(request, 'success.html')

"""

def add_person(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('person_list')  # Redirect to a view that lists persons
    else:
        form = PersonForm()
    return render(request, 'add_person.html', {'form': form})

"""

def add_person(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_page')
    else:
        form = PersonForm()
    return render(request, 'add_person.html', {'form': form})

def person_list(request):
    persons = Person.objects.all()
    return render(request, 'person_list.html', {'persons': persons})