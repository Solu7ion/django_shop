
from django.contrib import admin
from django.urls import path, include

admin.site.site_header = 'Онлайн магазин'
admin.site.site_title = 'Онлайн магазин'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('backend.urls'))
]
