from django.http import JsonResponse
from .producer import send_message


def my_view(request):
    data = {"message": "Hello Kafka"}
    send_message(data)
    return JsonResponse({"status": "Message sent"})
