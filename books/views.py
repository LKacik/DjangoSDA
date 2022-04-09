from uuid import uuid4

from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render


# Create your views here.


def get_hello(request: WSGIRequest) -> HttpResponse:
    return HttpResponse("<h1>hello world</h1>")


def get_uuids_a(request: WSGIRequest) -> HttpResponse:
    uuids = [f"{uuid4()}" for _ in range(10)]
    return HttpResponse(f"{uuids}")


def get_uuids_b(request: WSGIRequest) -> JsonResponse:
    uuids = [f"{uuid4()}" for _ in range(10)]
    return JsonResponse({"uuids": uuids})


def get_image(request: WSGIRequest) -> HttpResponse:
    return HttpResponse('<img src="https://images.pexels.com/photos/9197509/pexels-photo-9197509.jpeg" width="800" height="600">')


def get_button(request: WSGIRequest) -> HttpResponse:
    return HttpResponse('<button type="button">Click Me!</button>')
