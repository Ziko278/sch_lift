from django.urls import path
from subscription.views import *

urlpatterns = [

    path('feature/create', FeatureCreateView.as_view(), name='feature_create'),
    path('feature/index', FeatureListView.as_view(), name='feature_index'),
    path('feature/<int:pk>/edit', FeatureUpdateView.as_view(), name='feature_edit'),
    path('feature/<int:pk>/delete', FeatureDeleteView.as_view(), name='feature_delete'),

    path('module/create', ModuleCreateView.as_view(), name='module_create'),
    path('module/index', ModuleListView.as_view(), name='module_index'),
    path('module/<int:pk>/edit', ModuleUpdateView.as_view(), name='module_edit'),
    path('module/<int:pk>/delete', ModuleDeleteView.as_view(), name='module_delete'),

    path('plan/create', PlanCreateView.as_view(), name='plan_create'),
    path('plan/index', PlanListView.as_view(), name='plan_index'),
    path('plan/<int:pk>/edit', PlanUpdateView.as_view(), name='plan_edit'),
    path('plan/<int:pk>/delete', PlanDeleteView.as_view(), name='plan_delete'),

    path('online-payment-method/create', OnlinePaymentCreateView.as_view(), name='online_payment_create'),
    path('online-payment-method/index', OnlinePaymentListView.as_view(), name='online_payment_index'),
    path('online-payment-method/<int:pk>/detail', OnlinePaymentDetailView.as_view(), name='online_payment_detail'),
    path('online-payment-method/<int:pk>/edit', OnlinePaymentUpdateView.as_view(), name='online_payment_edit'),
    path('online-payment-method/<int:pk>/delete', OnlinePaymentDeleteView.as_view(), name='online_payment_delete'),

]

