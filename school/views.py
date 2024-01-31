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
from school.models import *
from account.models import *
from school.forms import *
from subscription.forms import SubscriptionPaymentForm


class SchoolCreateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    model = SchoolInfoModel
    permission_required = 'school.add_schoolinfomodel'
    form_class = SchoolForm
    success_message = 'School Registered Successfully'
    template_name = 'school/school/index.html'

    def get_success_url(self):
        return reverse('school_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['school_list'] = SchoolInfoModel.objects.all()
        return context


class SchoolListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = SchoolInfoModel
    permission_required = 'school.view_schoolinfomodel'
    fields = '__all__'
    template_name = 'school/school/index.html'
    context_object_name = "school_list"

    def get_queryset(self):
        return SchoolInfoModel.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = SchoolForm
        return context


class SchoolDetailView(DetailView):
    model = SchoolInfoModel
    fields = '__all__'
    template_name = 'school/school/detail.html'
    context_object_name = "school"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        school_db = SchoolDBModel.objects.filter(school=self.object).first()
        if school_db:
            school_form = SchoolDBForm(instance=school_db)
        else:
            school_form = SchoolDBForm
        context['school_form'] = school_form
        context['school_db'] = school_db
        context['plan_list'] = PlanModel.objects.all().order_by('price_per_term')
        context['academic_info'] = SchoolAcademicInfoModel.objects.first()
        return context


class SchoolUpdateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = SchoolInfoModel
    permission_required = 'school.change_schoolinfomodel'
    form_class = SchoolForm
    success_message = 'School Updated Successfully'
    template_name = 'school/school/edit.html'

    def get_success_url(self):
        return reverse('school_detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['school'] = self.object
        return context


class SchoolDeleteView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, DeleteView):
    model = SchoolInfoModel
    permission_required = 'school.delete_schoolinfomodel'
    success_message = 'School Deleted Successfully'
    fields = '__all__'
    template_name = 'school/school/delete.html'
    context_object_name = "school"

    def get_success_url(self):
        return reverse('school_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def generate_school_logins_view(request):
    if request.method == 'POST':
        username = request.POST.get('username').strip().lower()
        password = request.POST.get('password')
        email = request.POST.get('email').strip().lower()
        school_id = request.POST.get('school_id')
        school = SchoolInfoModel.objects.get(pk=school_id)

        if password == '':
            password = User.objects.make_random_password(length=8)

        if len(password) < 8:
            messages.error(request, "password must be up to 8 characters")
            return redirect(reverse('school_detail', kwargs={'pk': school.pk}))

        any_user = User.objects.filter(username=username)
        if len(any_user) > 0:
            messages.error(request, "Username Already Used")
            return redirect(reverse('school_detail', kwargs={'pk': school.pk}))

        user = User.objects.create_user(username=username, email=email, password=password)
        if user.id:
            profile = UserProfileModel.objects.create(user=user, is_schoollift=False, school=school)
            profile.save()

            if profile.id:
                messages.success(request,
                             "Account creation successful - Username: {} Password: {}".format(username, password))
            else:
                user.delete()
                messages.error(request, "Error Creating Account, Try Again!")
        else:
            messages.error(request, "Error Creating Account, Try Again!")
        return redirect(reverse('school_detail', kwargs={'pk': school.pk}))

    messages.error(request, "Method Not Allowed")
    return redirect(reverse('admin_dashboard'))


class SchoolDBCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = SchoolDBModel
    form_class = SchoolDBForm
    success_message = 'Database Setting Successfully Updated'
    template_name = 'school/school/detail.html'

    def get_success_url(self):
        return reverse('school_detail', kwargs={'pk': self.object.school.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class SchoolDBUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = SchoolDBModel
    form_class = SchoolDBForm
    success_message = 'Database Setting Successfully Updated'
    template_name = 'school/school/detail.html'

    def get_success_url(self):
        return reverse('school_detail', kwargs={'pk': self.object.school.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def change_subscription_plan(request):
    if request.method == 'POST':
        school_id = request.POST['school_id']
        school = SchoolInfoModel.objects.get(pk=school_id)
        plan_id = request.POST['plan_id']
        plan = PlanModel.objects.get(pk=plan_id)

        school_profile = UserProfileModel.objects.get(school=school)
        school_profile.current_plan = plan
        school_profile.save()

        messages.success(request, 'School Plan Updated Successfully')
        return redirect(reverse('school_detail', kwargs={'pk': school.id}))

    messages.error(request, 'Method Not Allowed')
    return redirect(reverse('admin_dashboard'))


def admin_subscription_payment(request):
    if request.method == 'POST':
        form = SubscriptionPaymentForm(request.POST)
        if form.is_valid():
            school_id = request.POST['school']
            amount = request.POST['amount']

            payment = form.save()
            if payment.id:
                messages.success(request, "Payment of N{} successfully recorded".format(amount))
                return redirect(reverse('school_detail', kwargs={'pk': school_id}))

        messages.error(request, 'Error Processing Payment, Try Later')

    messages.error(request, 'Method Not Allowed')
    return redirect(reverse('admin_dashboard'))
