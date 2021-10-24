from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.core.mail import send_mail, BadHeaderError
from django.views import View
from django.conf import settings
import logging

from .forms import ContactForm

# Create your views here.# Create your views here.
class IndexView(View):
    template_name = 'pages/index.html'
    success_url = 'home' # dummy view
    context = {}
    # myform is the definition/class of your form which contains all attrs.

    def get(self, request):
        self.context['form'] = ContactForm() # fill out your data here for get request
        return render(request, self.template_name, self.context)

    def post(self, request):
        # create a variable to keep track of the form
        messageSent = False

        form = ContactForm(request.POST)
        # Form Validation
        print(form.errors)
        if form.is_valid():
            cd = form.cleaned_data
            subject = "Sending an email with Django"
            name = cd['name']
            email = cd['email']
            subject = cd['subject']
            message = 'name: '+name+'\n'
            message += 'From: '+email+'\n'

            message += cd['message']
            #perform any logical validations here and save the form if required
            send_mail(subject, message, email, ['chris.polanco2@gmail.com'])

            messageSent = True

        context = self.context
        context['form'] = form # just to show you that you can access that form anywhere
        context['messageSent'] = messageSent
        return render(request, self.template_name, context)

def successView(request):
    return HttpResponse('Success! Thank you for your message.')
