from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.core.mail import send_mail, BadHeaderError
from django.views import View

from .forms import ContactForm

# Create your views here.# Create your views here.
class IndexView(View):
    template_name = 'pages/index.html'
    success_url = 'home' # dummy view
    context = {"form": ContactForm()}
    # myform is the definition/class of your form which contains all attrs.

    def get(self, request):
        context = self.context
        # context['form'] = form # fill out your data here for get request
        return render(request, self.template_name, context)

    def post(self, request):
        context=self.context
        # self.context certain that you're using exact form which you defined in class-scope
        form=context['form']
        # Form Validation
        if form.is_valid():
            #perform any logical validations here and save the form if required
            return redirect(self.success_url)

        context = self.context
        context['form'] = form # just to show you that you can access that form anywhere
        return render(request, self.template_name, context)

def successView(request):
    return HttpResponse('Success! Thank you for your message.')
