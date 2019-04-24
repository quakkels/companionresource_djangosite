from django.forms import ModelForm
from .models import ContactForm

class ContactFormForm(ModelForm):
    class Meta:
        model = ContactForm
        fields = ('name', 'email', 'comments', 'how_did_you_hear_about_us')