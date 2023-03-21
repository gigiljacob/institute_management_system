from django.contrib import messages
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView

from home.models import Contact


class HomeView(TemplateView):
    """Home page
    This is the first page of my personal website.
    From here one can redirect to different aspects of my life.
    """
    template_name = "home/home.html"

    def get_context_data(self, **kwargs: any) -> dict[str, any]:
        context = super().get_context_data(**kwargs)
        context.update({"home": True})
        return context


class ContactMe(CreateView):
    """Contact page
    If someone needs to contact can submit details on this page.
    """
    model = Contact
    fields = "__all__"
    template_name = "home/contact.html"
    success_url = reverse_lazy("home:contact")

    def get_context_data(self, **kwargs: any) -> dict[str, any]:
        context = super().get_context_data(**kwargs)
        context.update({"contact": True})
        return context

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        messages.add_message(self.request, messages.SUCCESS, "Thank you, will check and respond soon.")
        return super().form_valid(form)


class AboutMe(TemplateView):
    """About page
    About me details will be populated into this page.
    """
    template_name = "home/about.html"

    def get_context_data(self, **kwargs: any) -> dict[str, any]:
        context = super().get_context_data(**kwargs)
        context.update({"about": True})
        return context
