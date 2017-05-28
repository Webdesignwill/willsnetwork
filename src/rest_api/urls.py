from django.conf.urls import url
from rest_api.views import api_root
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = format_suffix_patterns([
    url(r'^(?P<version>1\.0)/$', api_root, name='root'),
])
