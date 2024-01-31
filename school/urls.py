from django.urls import path
from school.views import *

urlpatterns = [

    path('school/create', SchoolCreateView.as_view(), name='school_create'),
    path('school/index', SchoolListView.as_view(), name='school_index'),
    path('school/<int:pk>/detail', SchoolDetailView.as_view(), name='school_detail'),
    path('school/<int:pk>/edit', SchoolUpdateView.as_view(), name='school_edit'),
    path('school/<int:pk>/delete', SchoolDeleteView.as_view(), name='school_delete'),

    path('school/account/generate-login', generate_school_logins_view, name='school_generate_login'),

    path('school/database/create', SchoolDBCreateView.as_view(), name='school_db_create'),
    path('school/database/<int:pk>/edit', SchoolDBUpdateView.as_view(), name='school_db_edit'),


    path('school/plan/change', change_subscription_plan, name='admin_change_plan'),
    path('school/subscription/payment', admin_subscription_payment, name='admin_subscription_payment'),

]

