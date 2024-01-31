from django.urls import path
from home.views import *

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),

]

