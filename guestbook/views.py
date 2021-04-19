from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from guestbook.models import Guestbook


def index(request):
    guestbook_list = Guestbook.objects.all().order_by('-regdate')

    data = {'guestbook_list': guestbook_list}
    return render(request, 'guestbook/list.html', data)


def add(request):
    guestbook = Guestbook()
    guestbook.name = request.POST['name']
    guestbook.password = request.POST['password']
    guestbook.message = request.POST['message']

    guestbook.save()

    return HttpResponseRedirect('/guestbook')


def deleteform(request):
    return render(request, 'guestbook/deleteform.html')


def delete(request):
    guestbook = Guestbook.objects.filter(id=request.POST['no']).filter(password=request.POST['password'])
    guestbook.delete()

    return HttpResponseRedirect('/guestbook')


