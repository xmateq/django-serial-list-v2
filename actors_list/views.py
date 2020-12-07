import requests
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


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
    fields = ('title', 'number_of_seasons')
    login_url = '/login/'


class SerialDetails(DetailView):
    queryset = Serial.objects.all()
    template_name = 'actors_list/serial_details.html'





    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['actors'] = Actor.objects.filter(serials=context['object'])
        context['comments'] = Comment.objects.filter(serial=context['object'])
        context['avg_score'] = Comment.objects.filter(serial=context['object']).aggregate(Avg('rate'))
        return context


class CommentCreate(LoginRequiredMixin, CreateView):
    model = Comment
    template_name = 'actors_list/create_comment.html'
    success_url = reverse_lazy('shows_list')
    fields = ('com', 'rate')
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




