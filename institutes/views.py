from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView

from institutes.models import Institute


class CreateInstitute(LoginRequiredMixin, CreateView):
    template_name = 'institutes/create.html'
    model = Institute
    fields = ('name', 'type', 'address', 'phone', 'mobile', 'email', 'objective', 'bord', 'ownership', 'documents',
              'tan', 'license', 'accreditation', 'approvals', 'declaration')

    def get_success_url(self):
        messages.success(self.request, 'Institute registered successfully')
        return reverse_lazy('accounts:profile')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class InstituteListView(ListView):
    model = Institute
    context_object_name = 'institutes'

    def get_queryset(self):
        return self.model.objects.filter(created_by=self.request.user)


class ManageInstitute(LoginRequiredMixin, TemplateView):
    template_name = 'institutes/manage.html'

    def get_context_data(self, ins_identifier, **kwargs):
        context = super().get_context_data()
        try:
            context['institute'] = Institute.objects.get(identifier=ins_identifier, created_by=self.request.user)
        except Institute.DoesNotExist:
            context['institute'] = None
            raise Http404
        return context
