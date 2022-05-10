from django.shortcuts import render
from django.core.mail import send_mail
from django.template.loader import render_to_string


def index(request):
    if request.method == 'POST':


        name = request.POST.get('full-name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        ctx={
            'name' : name,
            'email' : email,
            'subject' : subject,
            'message' : message
        }

        message = render_to_string('mail.html', ctx)
        send_mail(
                  subject,
                  message,
                  email,
                  ['sergiomerdani@gmail.com'],
                  fail_silently=False, html_message=message)
        if message:
            return render(request,'success.html')
    return render(request, 'index.html')