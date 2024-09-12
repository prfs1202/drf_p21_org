from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from root import settings

urlpatterns = [
                  path('', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
                  path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
                  path('admin/', admin.site.urls),
                  path('api/v1/', include('apps.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
