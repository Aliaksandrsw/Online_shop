from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from Online_shop import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls',  namespace='store')),
    path('', include('users.urls',  namespace='users')),
    path('accounts/', include('allauth.urls')),
    path('orders/', include('orders.urls', namespace='orders')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)