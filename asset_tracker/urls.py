from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/employees/', include('employees.urls')),
    path('api/assets/', include('assets.urls')),
    path('submission/', include('submissions.urls')),
]
 