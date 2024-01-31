from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.db.models import Sum
import requests, json
from datetime import date, datetime, timedelta
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import PermissionDenied, ObjectDoesNotExist
from django.core.serializers.json import DjangoJSONEncoder
from django.core import serializers
from django.contrib.messages.views import SuccessMessageMixin, messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from admin_dashboard.models import *
from django.contrib.auth.models import Group, Permission
import math
from account.forms import *
from django.http import HttpResponse
import re
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from account.models import UserProfileModel


class GroupCreateView(SuccessMessageMixin, CreateView):
    model = Group
    form_class = GroupForm
    template_name = 'account/group/list.html'
    success_message = 'Group Added Successfully'

    def get_success_url(self):
        return reverse('group_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class GroupListView(ListView):
    model = Group
    fields = '__all__'
    template_name = 'account/group/index.html'
    context_object_name = "group_list"

    def get_queryset(self):
        return Group.objects.all().order_by('name')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = GroupForm
        return context


class GroupDetailView(DetailView):
    model = Group
    fields = '__all__'
    template_name = 'account/group/detail.html'
    context_object_name = "group"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class GroupUpdateView(SuccessMessageMixin, UpdateView):
    model = Group
    form_class = GroupForm
    template_name = 'account/group/index.html'
    success_message = 'Group Successfully Updated'

    def get_success_url(self):
        return reverse('group_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['group'] = self.object
        context['group_list'] = Group.objects.all().order_by('name')
        return context


class GroupPermissionView(SuccessMessageMixin, UpdateView):
    model = Group
    form_class = GroupForm
    template_name = 'account/group/permission.html'
    success_message = 'Group Permission Successfully Updated'

    def get_success_url(self):
        return reverse('group_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['group'] = self.object
        context['permission_list'] = Permission.objects.all()
        return context


def group_permission_view(request, pk):
    group = Group.objects.get(pk=pk)
    if request.method == 'POST':
        permissions = request.POST.getlist('permissions[]')
        group.permissions.set(permissions)
        messages.success(request, 'Group Permission Successfully Updated')
        return redirect(reverse('group_index'))
    context = {
        'group': group,
        'permission_list': Permission.objects.all()

    }
    return render(request, 'account/group/permission.html', context)


class GroupDeleteView(DeleteView):
    model = Group
    fields = '__all__'
    template_name = 'account/group/delete.html'
    context_object_name = "group"

    def get_success_url(self):
        return reverse('group_index')

    def dispatch(self, *args, **kwargs):
        if self.request.POST.get('name') in ['student', 'superadmin', 'teacher', 'parent']:
            messages.error(self.request, 'Restricted Group, Permission Denied')
            return redirect(reverse('group_index'))
        return super(GroupDeleteView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def user_sign_in_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            intended_route = request.POST.get('next')
            if not intended_route:
                intended_route = request.GET.get('next')

            remember_me = request.POST.get('remember_me')
            if not remember_me:
                remember_me = request.GET.get('remember_me')

            if user.is_superuser:
                login(request, user)
                messages.success(request, 'welcome back {}'.format(user.username.title()))
                if remember_me:
                    request.session.set_expiry(3600 * 24 * 30)
                else:
                    request.session.set_expiry(0)
                if intended_route:
                    return redirect(intended_route)
                return redirect(reverse('admin_dashboard'))
            try:
                user_role = UserProfileModel.objects.get(user=user)
            except UserProfileModel.DoesNotExist:
                messages.error(request, 'Unknown Identity, Access Denied')
                return redirect(reverse('login'))

            if user_role.is_schoollift:
                login(request, user)
                messages.success(request, 'welcome back {}'.format(user.username))
                if remember_me:
                    request.session.set_expiry(3600 * 24 * 30)
                else:
                    request.session.set_expiry(0)
                if intended_route:
                    return redirect(intended_route)
                return redirect(reverse('admin_dashboard'))

            elif user_role.school:
                login(request, user)
                messages.success(request, 'welcome back {}'.format(user_role.school.short_name.title()))
                if remember_me:
                    request.session.set_expiry(3600 * 24 * 30)
                else:
                    request.session.set_expiry(0)

                return redirect(reverse('school_dashboard'))

            else:
                messages.error(request, 'Unknown Identity, Access Denied')
                return redirect(reverse('login'))
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect(reverse('login'))

    return render(request, 'account/user/sign_in.html')


def user_sign_out_view(request):
    logout(request)
    return redirect(reverse('login'))


def user_reset_password_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        user = User.objects.filter(username=username).first()
        if not user:
            messages.error(request, 'Incorrect Username Provided')
            return redirect(reverse('reset_password'))

        if user.profile:
            default_password = user.profile.default_password
            user.password = make_password(default_password)
            user.save()

            user_type = user.profile.type
            if user.profile.staff:
                email = user.profile.staff.email
                full_name = user.profile.staff
            elif user.profile.student:
                email = user.profile.student.email
                full_name = user.profile.student
            elif user.profile.parent:
                email = user.profile.parent.email
                full_name = user.profile.parent
            else:
                email = full_name = user.email
            if email:
                # mail = send_user_password_reset_mail(request, email, full_name, default_password, user_type)
                messages.error(request, 'Your Password has been changed back to default')
            return redirect(reverse('login'))

        messages.error(request, 'Error updating password, contact admin')

    return render(request, 'account/user/reset_password.html')


@login_required
def user_change_password_view(request):
    if request.method == 'POST':
        current_password = request.POST['current_password']
        new_password1 = request.POST['new_password1']
        new_password2 = request.POST['new_password2']

        # Verify the current password
        if not request.user.check_password(current_password):
            messages.error(request, 'Incorrect current password.')
            if 'route' in request.POST:
                return redirect(reverse('user_profile'))
            return redirect(reverse('change_password'))

        # Check if the new passwords match
        if len(new_password1) < 8:
            messages.error(request, 'Password must have at least 8 characters.')
            if 'route' in request.POST:
                return redirect(reverse('user_profile'))
            return redirect(reverse('change_password'))

        if not re.match("^(?=.*[a-zA-Z])(?=.*\d)[a-zA-Z\d]+$", new_password1):
            messages.error(request, 'Password must contain both letters and numbers.')
            if 'route' in request.POST:
                return redirect(reverse('user_profile'))
            return redirect(reverse('change_password'))

        if new_password1 != new_password2:
            messages.error(request, 'New passwords do not match.')
            if 'route' in request.POST:
                return redirect(reverse('user_profile'))
            return redirect(reverse('change_password'))

        # Update the user's password
        user = request.user
        user.set_password(new_password1)
        user.save()

        # Update the user's session with the new password
        update_session_auth_hash(request, user)

        logout(request)

        messages.success(request, 'Password successfully changed. Please log in with the new password.')
        return redirect('login')

    return render(request, 'user_management/change_password.html')


@login_required
def user_profile_view(request):
    if request.user.is_superuser or request.user.profile.staff:
        return render(request, 'user_management/profile/staff_profile.html')
    if request.user.profile.student:
        return render(request, 'user_management/profile/student_profile.html')
    if request.user.profile.parent:
        return render(request, 'user_management/profile/parent_profile.html')

