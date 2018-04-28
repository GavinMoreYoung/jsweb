from django.core.paginator import Paginator
from django.shortcuts import render
from dyy.models import *


def index(request):
    o = Dy.objects.all().filter(dyclass=1)[:6]
    i = Dy.objects.all().filter(dyclass=2)[:6]
    return render(request, 'index.html', {'o': o, 'i': i})


def list(request):
    lb = request.GET.get("lb", "1")
    if (lb == "1"):
        clb = "院线热映"
    else:
        clb = "人生必看"
    page = request.GET.get('p', '1')
    o = Dy.objects.all().filter(dyclass=lb)
    i = Paginator(o, 9).get_page(page)
    return render(request, 'list.html', {'i': i, 'lb': lb, 'clb': clb})


def info(request):
    dyid = request.GET.get("id", "1")
    dy = Dy.objects.get(id=dyid)
    return render(request, 'info.html', {'dy': dy})


def wz(request):
    page = request.GET.get('p', '1')
    i = Wz.objects.all()
    o = Paginator(i, 11).get_page(page)
    return render(request, 'wzlist.html', {'o': o})


def wzinfo(request, nid):
    i = Wz.objects.get(id=nid)
    return render(request, 'wzinfo.html', {'i': i})


def finddy(request):
    dyname = request.GET.get('dyname', '极速蜗牛')
    print(dyname)
    i = Dy.objects.all().filter(dybt=dyname)
    print(i)
    if (i.exists()):
        page = "info.html"
    else:
        page = "NFind.html"
    return render(request, page, {'dy': i})
