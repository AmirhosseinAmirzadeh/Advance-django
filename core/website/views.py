from django.shortcuts import render
from django.views.generic import FormView
from website.forms import ContactForm

# Create your views here.

class ContactCreateView(FormView):
    """
    A class for contact form view
    """
    template_name = 'website/contact.html'
    form_class = ContactForm
    success_url = '/contact/'
    