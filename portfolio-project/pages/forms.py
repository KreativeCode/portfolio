from django import forms
from django.core.mail import send_mail

class ContactForm(forms.Form):
    name = forms.CharField(required=True, widget=forms.TextInput
                            (attrs={'class':'form-control',
				                    'id':'name',
                                    'placeholder': 'Name'}))
    email = forms.EmailField(required=True, widget=forms.TextInput
                            (attrs={'class':'form-control',
                                    'id':'email',
                                    'placeholder': 'Email'}))
    subject = forms.CharField(required=False, widget=forms.TextInput
                             (attrs={'class':'form-control',
                                     'id':'subject',
                                     'placeholder': 'Subject'}))
    message = forms.CharField(required=True, widget=forms.Textarea
                             (attrs={'class':'form-control',
                                     'id':'message',
                                     'placeholder': 'Message',
                                     'cols': 30,
                                     'rows': 8}))
