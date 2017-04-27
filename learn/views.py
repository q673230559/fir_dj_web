__author__ = 'Administrator'


# coding:utf-8
from django.http import HttpResponse
import django


def index(request):
    return HttpResponse(u"欢迎光临 自强学堂!" + django.get_version())