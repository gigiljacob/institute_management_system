from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, PasswordResetView
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView

from accounts.forms import ImsUserCreationForm
from institutes.views import InstituteListView


class UserRegister(FormView):
    form_class = ImsUserCreationForm
    template_name = 'accounts/register.html'

    def get_success_url(self):
        messages.success(self.request, 'Account created successfully')
        return reverse_lazy('accounts:login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(self.request)


class ImsLoginView(LoginView):
    template_name = 'accounts/login.html'

    def get_success_url(self):
        messages.success(self.request, f'Welcome back {self.request.user.email}')
        return reverse_lazy('accounts:profile')


class ImsProfileView(LoginRequiredMixin, InstituteListView):
    template_name = 'accounts/profile.html'


class ResetPasswordView(PasswordResetView):
    template_name = 'accounts/password_reset.html'

    def get_success_url(self):
        messages.success(self.request, 'Account created successfully')
        return reverse_lazy('accounts:login')
