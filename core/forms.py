from django import forms
from django.core.mail import send_mail
from django.conf import settings


class ContactForms(forms.Form):
    name = forms.CharField(label='Nome')
    email = forms.EmailField(label='E-mail')
    message = forms.CharField(label='Mensagem', widget=forms.Textarea)

    def send_mail(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        message = self.cleaned_data['message']
        message = 'Nome: {}\n' \
                  'E-Mail: {}\n' \
                  '{}'.format(name, email, message)
        send_mail(
            'Contato do Django E-Commerce', message, settings.EMAIL_HOST_USER,
            settings.DEFAULT_FROM_EMAIL
        )
