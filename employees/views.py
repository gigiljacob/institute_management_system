from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from accounts.forms import ImsUserCreationForm
from employees.models import Employee
from institutes.models import Institute


class EmployeeList(LoginRequiredMixin, ListView):
    template_name = 'employees/list.html'
    model = Employee
    context_object_name = 'employees'

    def get_queryset(self):
        return self.model.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()

        # Institute which the employee belongs to
        try:
            identifier = self.kwargs.get('ins_identifier', None)
            institute = Institute.objects.get(identifier=identifier)
        except Institute.DoesNotExist:
            institute = None

        context.update({'institute': institute, 'ins_identifier': identifier})
        return context


class EmployeeCreate(LoginRequiredMixin, CreateView):
    template_name = 'employees/create.html'
    model = get_user_model()
    form_class = ImsUserCreationForm

    def get_success_url(self):
        return reverse_lazy('employees:list', args=[self.kwargs.get('ins_identifier')])

    def form_valid(self, form):
        valid_form = super().form_valid(form)
        import pdb
        pdb.set_trace()
        print(valid_form)
        return valid_form

