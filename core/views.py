from django.shortcuts import render
from django.views.generic import TemplateView

from .forms import ContactForms


class IndexView(TemplateView):
    template_name = 'index.html'


index = IndexView.as_view()


def contact(request):
    success = False
    form = ContactForms(request.POST or None)
    if form.is_valid():
        form.send_mail()
        success = True
        form = ContactForms(None)
    context = {
        'form': form,
        'success': success
    }
    return render(request=request, template_name='contact.html', context=context)
