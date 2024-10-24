from django import forms


class ContactForm(forms.Form):
    """
    A class for contact form
    """
    name = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)