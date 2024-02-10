from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.shortcuts import render, reverse, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, View
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
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
        contex = super().get_context_data(**kwargs)
        ads = self.get_object()
        contex['comments'] = ads.comments.order_by('-created_at')
        return contex

class AdsCreateView(CreateView):
    model = Ads
    template_name = 'ads/create_ads.html'
    form_class = AdsForm

    def form_valid(self, form):
        self.ads = form.save(commit=False)
        self.ads.author = self.request.user
        self.ads.save()
        form.save_m2m()
        return redirect('webapp:list')

class AdsUpdateView(UpdateView):
    model = Ads
    template_name = 'ads/update_ads.html'
    form_class = AdsForm

    def get_success_url(self):
        return reverse_lazy('webapp:list')

class DeleteAdsView(View):
    def post(self, request, *args, **kwargs):
        ads = Ads.objects.get(pk=kwargs['pk'])
        ads.status = 'on_delete'
        ads.save()
        return redirect('webapp:list')



