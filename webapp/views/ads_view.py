from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.shortcuts import render, reverse, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from webapp.models import Ads
from webapp.forms import AdsForm

def index(request):
    return render(request, 'index.html')

class HomeView(ListView):
    model = Ads
    template_name = 'ads/list.html'
    context_object_name = 'ads'

    def get_queryset(self):
        return Ads.objects.filter(status='published').order_by('-published_at')

class AdsDetailView(DetailView):
    model = Ads
    template_name = 'ads/detail_ads.html'
    context_object_name = 'ads'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['ads'] = Ads.objects.filter(status='published')
        return context

class AdsCreateView(LoginRequiredMixin, CreateView):
    model = Ads
    template_name = 'ads/create_ads.html'
    form_class = AdsForm

    def form_valid(self, form):
        self.ads = form.save(commit=False)
        self.ads.author = self.request.user
        self.ads.save()
        form.save_m2m()
        return redirect('webapp:list')
