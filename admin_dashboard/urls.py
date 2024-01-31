from django.urls import path
from admin_dashboard.views import *

urlpatterns = [
    path('', AdminDashboardView.as_view(), name='admin_dashboard'),
    
    path('session/create', SessionCreateView.as_view(), name='session_create'),
    path('session/index', SessionListView.as_view(), name='session_index'),
    path('session/<int:pk>/edit', SessionUpdateView.as_view(), name='session_edit'),
    path('session/<int:pk>/delete', SessionDeleteView.as_view(), name='session_delete'),

    path('academic-info', AcademicSettingView.as_view(), name='academic_index'),
    path('academic-info/create', AcademicSettingCreateView.as_view(), name='academic_info_create'),
    path('academic-info/<int:pk>/update', AcademicSettingUpdateView.as_view(), name='academic_info_update'),

]

