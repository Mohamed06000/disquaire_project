from django.shortcuts import render
from django.http import HttpResponse
from . import models


def index(request):
    message = "Hello World!"
    return HttpResponse(message)


def listing(request):
    albums = [f'<li>{album["name"]} : {artists["name"]}</li>' for album in models.ALBUMS for artists in album['artists']]
    message = """<ul>{}</ul>""".format("\n".join(albums))
    return HttpResponse(message)