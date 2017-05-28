from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(('GET',))
def api_root(request, version, format=None):
    return Response({
        'version': '1.0',
    })
