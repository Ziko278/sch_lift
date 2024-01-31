from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
# from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.messages.views import SuccessMessageMixin, messages
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from admin_dashboard.models import *
from admin_dashboard.forms import *


class AdminDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'admin_dashboard/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class SessionCreateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    model = SessionModel
    permission_required = 'admin_dashboard.add_sessionmodel'
    form_class = SessionForm
    success_message = 'Session Added Successfully'
    template_name = 'admin_dashboard/session/index.html'

    def get_success_url(self):
        return reverse('session_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['session_list'] = SessionModel.objects.all()
        return context


class SessionListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = SessionModel
    permission_required = 'admin_dashboard.view_sessionmodel'
    fields = '__all__'
    template_name = 'admin_dashboard/session/index.html'
    context_object_name = "session_list"

    def get_queryset(self):
        return SessionModel.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = SessionForm
        return context


class SessionUpdateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = SessionModel
    permission_required = 'admin_dashboard.change_sessionmodel'
    form_class = SessionForm
    success_message = 'Session Updated Successfully'
    template_name = 'admin_dashboard/session/index.html'

    def get_success_url(self):
        return reverse('session_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['session_list'] = SessionModel.objects.all()
        return context


class SessionDeleteView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, DeleteView):
    model = SessionModel
    permission_required = 'admin_dashboard.delete_sessionmodel'
    success_message = 'Session Deleted Successfully'
    fields = '__all__'
    template_name = 'admin_dashboard/session/delete.html'
    context_object_name = "session"

    def get_success_url(self):
        return reverse('session_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class AcademicSettingView(LoginRequiredMixin, TemplateView):
    template_name = 'admin_dashboard/academic_setting/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        academic_info = SchoolAcademicInfoModel.objects.first()

        if not academic_info:
            form = SchoolAcademicInfoForm
            is_academic_info = False
        else:
            form = SchoolAcademicInfoForm(instance=academic_info)
            is_academic_info = True
        context['form'] = form
        context['is_academic_info'] = is_academic_info
        context['academic_info'] = academic_info
        return context


class AcademicSettingCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = SchoolAcademicInfoModel
    form_class = SchoolAcademicInfoForm
    template_name = 'admin_dashboard/academic_setting/index.html'
    success_message = 'Academic Info Updated Successfully'

    def get_success_url(self):
        return reverse('academic_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class AcademicSettingUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = SchoolAcademicInfoModel
    form_class = SchoolAcademicInfoForm
    template_name = 'admin_dashboard/academic_setting/index.html'
    success_message = 'Academic Info Updated Successfully'

    def get_success_url(self):
        return reverse('academic_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context
