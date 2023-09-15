from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from django.contrib import messages

from bio.models import Contact


class Home(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context.update({'page': 'Home'})
        return context


class ContactView(CreateView):
    template_name = 'contact.html'
    model = Contact
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context.update({'page': 'contact'})
        return context

    def get_success_url(self):
        messages.add_message(self.request, messages.INFO, "Will get back to you shortly.")
        return reverse_lazy('profile:contact')

class Resume(TemplateView):
    template_name = 'resume-v1.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context.update({'page': 'resume'})
        return context
