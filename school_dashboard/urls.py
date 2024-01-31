from django.urls import path
from school_dashboard.views import *

urlpatterns = [
    path('dashboard', SchoolDashboardView.as_view(), name='school_dashboard'),

]
