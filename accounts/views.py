from django.core.paginator import Paginator
from django.shortcuts import render
from django.db.models import Q
from django.shortcuts import redirect, reverse
from django.contrib.auth import login, get_user_model
from django.views.generic import CreateView, DetailView, UpdateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.forms import MyUserCreationForm, UserChangeForm, SearchForm
from django.contrib.auth.views import PasswordChangeView
from webapp.models import Ads


class RegisterView(CreateView):
    model = get_user_model()
    form_class = MyUserCreationForm
    template_name = 'user_create.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(self.get_success_url())

    def get_success_url(self):
        next_page = self.request.GET.get('next')
        if not next_page:
            next_page = self.request.POST.get('next')
        if not next_page:
            next_page = reverse('webapp:index')

        return next_page


class UserDetailView(LoginRequiredMixin, DetailView):
    model = get_user_model()
    template_name = 'user_detail.html'
    context_object_name = 'user_obj'


class UserChangeView(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = UserChangeForm
    template_name = 'user_change.html'
    context_object_name = 'user_obj'

    def get_queryset(self):
        return super().get_queryset().filter(id=self.request.user.id)

    def get_success_url(self):
        return reverse('accounts:user_detail', kwargs={'pk': self.object.pk})


class UserPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    template_name = 'user_password_change.html'

    def get_success_url(self):
        return reverse('accounts:user_detail', kwargs={'pk': self.request.user.pk})


class UserSearchView(LoginRequiredMixin, ListView):
    template_name = 'user_list_search.html'
    model = get_user_model()
    context_object_name = 'users'

    def get_queryset(self):
        queryset = super().get_queryset()
        form = SearchForm(self.request.GET)
        if form.is_valid():
            queryset = queryset.filter(Q(first_name__icontains=form.cleaned_data['search']) |
                                       Q(last_name__icontains=form.cleaned_data['search']) |
                                       Q(email__icontains=form.cleaned_data['search']) |
                                       Q(username__icontains=form.cleaned_data['search']))
        return queryset
