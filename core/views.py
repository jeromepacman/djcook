
from django.http import JsonResponse
import logging

logger = logging.getLogger(__name__)


def index(request):
    return JsonResponse("Bad request", safe=False)


def webhook_view(request):
    if request.method == 'POST':
        return JsonResponse({"ok": "processed"}, safe=False)
    elif request.method == 'GET':
        return JsonResponse({"invalid : request"}, safe=False)
