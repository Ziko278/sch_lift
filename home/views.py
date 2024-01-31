from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'home/index.html'


class ContactView(TemplateView):
    template_name = 'home/contact.html'




