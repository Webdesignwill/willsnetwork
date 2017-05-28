from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response
from rest_framework.reverse import reverse

from rest_api import serializers
from contacts import models


@api_view(('GET',))
def api_root(request, version, format=None):
    return Response({
        'version': '1.0',
        'contacts': reverse('rest_api:contact-list', request=request,
                            kwargs={'version': version}),
    })


class ContactViewSet(CreateModelMixin, viewsets.GenericViewSet):
    queryset = models.Contact.objects.all()
    serializer_class = serializers.ContactSerializer

    def perform_create(self, serializer):
        serializer.save(created_ip_address=self.request.META['REMOTE_ADDR'])
