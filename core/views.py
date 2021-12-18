from django.http import HttpResponse
from datetime import date
import requests
import json
from django.http import JsonResponse
from django.views import View
from django.conf import settings


# from bot.models import Events


def index(request):
    return HttpResponse(status=201)


class WebhookView(View):
    def post(self, request, *args, **kwargs):
        t_body = request.body
        t_data = json.loads(t_body.decode("utf-8"))



        u = getUpdate(t_data)
        text = u["text"]
        id = u["id"]

        и
        if text == "/all":
            result = Events.objects.all()
            for e in result:
                message = formatMessage(e)
                self.send_message(message, id)

        if text == "/today":
            today = date.today()
            today_filter = Events.objects.filter(
                date__month=today.month, date__day=today.day
            )
            for e in today_filter:
                message = formatMessage(e)
                self.send_message(message, id)

        return JsonResponse({"Ok": "POST request processed"})

    @staticmethod
    def send_message(message, chat_id):
        data = {
            "chat_id": chat_id,
            "text": message,
            "parse_mode": "Markdown",
        }
        requests.post(
            f"{settings.TELEGRAM_URL}{settings.TOKEN}/sendMessage", data=data
        )


