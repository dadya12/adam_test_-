from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, View
from webapp.forms import CommentForm
from webapp.models import Comment, Ads


class CommentCreateView(CreateView):
    model = Comment
    template_name = 'comments/comments_create.html'
    form_class = CommentForm

    def form_valid(self, form):
        ads = get_object_or_404(Ads, pk=self.kwargs.get('pk'))
        comment = form.save(commit=False)
        comment.ads = ads
        comment.author = self.request.user
        comment.save()
        return redirect('webapp:detail_ads', pk=self.kwargs.get('pk'))

class CommentDeleteView(View):
    def post(self, request, pk):
        comment = get_object_or_404(Comment, pk=pk)
        ads_id = comment.ads.pk
        if request.user == comment.ads.author:
            comment.delete()
            return redirect('webapp:detail_ads', pk=ads_id)
        else:
            return HttpResponseForbidden('Не удаляется чето')
