from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from .forms import ContactForm


def index(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid:
            name = request.POST.get('full_name')
            email = request.POST.get('email_address')
            subject = request.POST.get('subject')
            message = request.POST.get('message')
            try:
                # send mail to admin email using django mail server
                send_mail(subject, message, email, ['rhn.swl@gmail.com'])
            except BadHeaderError:
                return HttpResponse(request, "Invalid header found")
            return HttpResponse(request, "Message sent successfully")

    else:
        form = ContactForm()

    return render(request, 'resume/index.html', {'form': form})
