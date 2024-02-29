# from django.shortcuts import render
from typing import Any
from django.http import HttpResponse


def home(request) -> HttpResponse:
    '''define a home'''
    return HttpResponse('home')


def contato(request: Any) -> HttpResponse:
    return HttpResponse('contato')


def sobre(request: Any) -> HttpResponse:
    return HttpResponse('sobre')
