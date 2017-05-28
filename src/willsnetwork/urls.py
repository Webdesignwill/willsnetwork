from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import RedirectView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('rest_api.urls', namespace='rest_api')),
    url(r'^favicon\.ico$', RedirectView.as_view(
        url=settings.FAVICON_PATH, permanent=True), name='favicon'),
]
