from django.contrib.auth import get_user_model
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, TemplateView, UpdateView, FormView
from django.urls import reverse_lazy

from .forms import UserAdminCreationForm

# from .models import User
User = get_user_model()


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'account/account.html'
#    login_url = 'account:login' # está definido em settings


class UpdateUserView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'account/update_user.html'
    fields = ['name', 'username', 'email']
    success_url = reverse_lazy('account:index')

    def get_object(self, queryset=None):
        return self.request.user


class UpdatePasswordView(LoginRequiredMixin, FormView):
    template_name = 'account/update_password.html'
    success_url = reverse_lazy('account:index')
    form_class = PasswordChangeForm

    def get_form_kwargs(self):
        kwargs = super(UpdatePasswordView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.save()
        return super(UpdatePasswordView, self).form_invalid(form)


class RegisterViews(CreateView):
    model = User
    template_name = 'account/register.html'
    form_class = UserAdminCreationForm
    success_url = reverse_lazy('account:login')


index = IndexView.as_view()
update_user = UpdateUserView.as_view()
update_password = UpdatePasswordView.as_view()
register = RegisterViews.as_view()
