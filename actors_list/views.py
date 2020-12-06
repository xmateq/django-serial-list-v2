import requests
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .forms import SerialForm, CommentForm
from .models import Serial, Actor, Comment
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView, TemplateView
from django.db.models import Avg


class IndexView(ListView):
    queryset = Serial.objects.all()
    template_name = 'actors_list/seriale.html'


class SerialCreate(LoginRequiredMixin, CreateView):
    model = Serial
    template_name = 'actors_list/create_serial.html'
    fields = ('title', 'number_of_seasons')
    success_url = reverse_lazy('shows_list')
    login_url = '/login/'


class SerialDelete(LoginRequiredMixin, DeleteView):
    model = Serial
    template_name = 'actors_list/delete_serial.html'
    success_url = reverse_lazy('shows_list')
    login_url = '/login/'


class SerialUpdate(LoginRequiredMixin, UpdateView):
    model = Serial
    template_name = 'actors_list/update_serial.html'
    success_url = reverse_lazy('shows_list')
    fields = ['title', 'number_of_seasons']
    login_url = '/login/'


class SerialDetails(DetailView):
    queryset = Serial.objects.all()
    template_name = 'actors_list/serial_details.html'

    def call_api(self):
        search = Serial.objects.get(pk=self.kwargs.get('pk'))
        url = "https://api.trakt.tv/search/show?query={}"

        r = requests.get(url.format(search), headers = {
            'Content_type':'application/json',
            'trakt-api-version': '2',
            'trakt-api-key': '6b3819e58b6b2b8b317bb2ee99988c2dab6e4ff3e2e865743cc0069b19d3b45f'
        })
        d = r.json()
        return d[0]


    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['actors'] = Actor.objects.filter(serials=context['object'])
        context['comments'] = Comment.objects.filter(serial=context['object'])
        context['avg_score'] = Comment.objects.filter(serial=context['object']).aggregate(Avg('rate'))
        context['year'] = self.call_api()['show']['year']
        context['slug'] = self.call_api()['show']['ids']['slug']
        context['imdb'] = self.call_api()['show']['ids']['imdb']
        context['apititle'] = self.call_api()['show']['title']
        return context


class CommentCreate(LoginRequiredMixin, CreateView):
    model = Comment
    template_name = 'actors_list/create_comment.html'
    success_url = reverse_lazy('shows_list')
    form_class = CommentForm
    login_url = '/login/'

    def form_valid(self, form):
        get_object_or_404(Serial, pk=self.kwargs.get('pk'))
        form.instance.serial = Serial.objects.get(pk=self.kwargs.get('pk'))
        return super().form_valid(form)


class Profile(LoginRequiredMixin, TemplateView):
    template_name = 'actors_list/profile.html'
    login_url = '/login/'


class SignUpView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'




