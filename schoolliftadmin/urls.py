from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('site-admin/', include('admin_dashboard.urls')),
    path('site-admin/subscription/', include('subscription.urls')),
    path('site-admin/school/', include('school.urls')),
    path('site-admin/account/', include('account.urls')),
    path('school/', include('school_dashboard.urls')),
    path('', include('home.urls')),
    path('django-admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


