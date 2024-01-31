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
from subscription.models import *
from subscription.forms import *


class FeatureCreateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    model = FeatureModel
    permission_required = 'subscription.add_featuremodel'
    form_class = FeatureForm
    success_message = 'Subscription Feature Added Successfully'
    template_name = 'subscription/feature/index.html'

    def get_success_url(self):
        return reverse('feature_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['feature_list'] = FeatureModel.objects.all()
        return context


class FeatureListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = FeatureModel
    permission_required = 'subscription.view_Featuremodel'
    fields = '__all__'
    template_name = 'subscription/feature/index.html'
    context_object_name = "feature_list"

    def get_queryset(self):
        return FeatureModel.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = FeatureForm
        return context


class FeatureUpdateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = FeatureModel
    permission_required = 'subscription.change_featuremodel'
    form_class = FeatureForm
    success_message = 'Feature Updated Successfully'
    template_name = 'subscription/feature/index.html'

    def get_success_url(self):
        return reverse('feature_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['feature_list'] = FeatureModel.objects.all()
        return context


class FeatureDeleteView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, DeleteView):
    model = FeatureModel
    permission_required = 'subscription.delete_featuremodel'
    success_message = 'Feature Deleted Successfully'
    fields = '__all__'
    template_name = 'subscription/feature/delete.html'
    context_object_name = "feature"

    def get_success_url(self):
        return reverse('feature_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ModuleCreateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    model = ModuleModel
    permission_required = 'subscription.add_modulemodel'
    form_class = ModuleForm
    success_message = 'Module Added Successfully'
    template_name = 'subscription/module/index.html'

    def get_success_url(self):
        return reverse('module_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['module_list'] = ModuleModel.objects.all()
        return context


class ModuleListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = ModuleModel
    permission_required = 'subscription.view_modulemodel'
    fields = '__all__'
    template_name = 'subscription/module/index.html'
    context_object_name = "module_list"

    def get_queryset(self):
        return ModuleModel.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ModuleForm
        return context


class ModuleUpdateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = ModuleModel
    permission_required = 'subscription.change_modulemodel'
    form_class = ModuleForm
    success_message = 'Module Updated Successfully'
    template_name = 'subscription/module/index.html'

    def get_success_url(self):
        return reverse('module_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['module_list'] = ModuleModel.objects.all()
        return context


class ModuleDeleteView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, DeleteView):
    model = ModuleModel
    permission_required = 'subscription.delete_modulemodel'
    success_message = 'Module Deleted Successfully'
    fields = '__all__'
    template_name = 'subscription/module/delete.html'
    context_object_name = "module"

    def get_success_url(self):
        return reverse('module_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class PlanCreateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    model = PlanModel
    permission_required = 'subscription.add_planmodel'
    form_class = PlanForm
    success_message = 'Plan Added Successfully'
    template_name = 'subscription/plan/index.html'

    def get_success_url(self):
        return reverse('plan_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['plan_list'] = PlanModel.objects.all()
        return context


class PlanListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = PlanModel
    permission_required = 'subscription.view_planmodel'
    fields = '__all__'
    template_name = 'subscription/plan/index.html'
    context_object_name = "plan_list"

    def get_queryset(self):
        return PlanModel.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = PlanForm
        return context


class PlanUpdateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = PlanModel
    permission_required = 'subscription.change_planmodel'
    form_class = PlanForm
    success_message = 'Plan Updated Successfully'
    template_name = 'subscription/plan/edit.html'

    def get_success_url(self):
        return reverse('plan_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['plan'] = self.object
        return context


class PlanDeleteView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, DeleteView):
    model = PlanModel
    permission_required = 'subscription.delete_planmodel'
    success_message = 'Plan Deleted Successfully'
    fields = '__all__'
    template_name = 'subscription/plan/delete.html'
    context_object_name = "plan"

    def get_success_url(self):
        return reverse('plan_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class OnlinePaymentCreateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    model = OnlinePaymentModel
    permission_required = 'subscription.add_onlinepaymentmodel'
    form_class = OnlinePaymentForm
    success_message = 'Payment Method Added Successfully'
    template_name = 'subscription/online_payment/index.html'

    def get_success_url(self):
        return reverse('online_payment_index')
        # return reverse('online_payment_detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['online_payment_list'] = OnlinePaymentModel.objects.all().order_by('name')

        return context


class OnlinePaymentListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = OnlinePaymentModel
    permission_required = 'subscription.view_onlinepaymentmodel'
    fields = '__all__'
    template_name = 'subscription/online_payment/index.html'
    context_object_name = "online_payment_list"

    def get_queryset(self):
        return OnlinePaymentModel.objects.all().order_by('name')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = OnlinePaymentForm

        return context


class OnlinePaymentDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = OnlinePaymentModel
    permission_required = 'subscription.view_onlinepaymentmodel'
    fields = '__all__'
    template_name = 'subscription/online_payment/detail.html'
    context_object_name = "method"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        key = self.object.key
        fernet = Fernet(key)
        context['public_key'] = fernet.decrypt(self.object.public_key.encode()).decode()
        context['private_key'] = fernet.decrypt(self.object.private_key.encode()).decode()
        return context


class OnlinePaymentUpdateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = OnlinePaymentModel
    permission_required = 'finance.change_feegroupmodel'
    form_class = OnlinePaymentForm
    success_message = 'Online Payment Method Updated Successfully'
    template_name = 'subscription/online_payment/index.html'

    def get_success_url(self):
        return reverse('online_payment_index')
        # return reverse('fee_group_detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['online_payment_list'] = OnlinePaymentModel.objects.all().order_by('name')

        return context


class OnlinePaymentDeleteView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, DeleteView):
    model = OnlinePaymentModel
    permission_required = 'subscription.delete_onlinepaymentmodel'
    success_message = 'Online Payment Method Deleted Successfully'
    fields = '__all__'
    template_name = 'subscription/online_payment/delete.html'
    context_object_name = "online_payment"

    def get_success_url(self):
        return reverse("online_payment_index")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
