from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


from core.yasg import urlpatterns as yasg
urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('accounts.urls')),
    path('post/', include('posts.urls')),
] + yasg


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
