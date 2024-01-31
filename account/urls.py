from django.urls import path
from account.views import *

urlpatterns = [
    path('group/add', GroupCreateView.as_view(), name='group_create'),
    path('group/index', GroupListView.as_view(), name='group_index'),
    path('group/<int:pk>/detail', GroupDetailView.as_view(), name='group_detail'),
    path('group/<int:pk>/edit', GroupUpdateView.as_view(), name='group_edit'),
    path('group/<int:pk>/permission/edit', group_permission_view, name='group_permission'),
    path('group/<int:pk>/delete', GroupDeleteView.as_view(), name='group_delete'),

    path('login', user_sign_in_view, name='login'),
    path('logout', user_sign_out_view, name='logout'),
    path('reset-password', user_reset_password_view, name='reset_password'),
    path('change-password', user_change_password_view, name='change_password'),
    path('user-profile', user_profile_view, name='user_profile'),

]
