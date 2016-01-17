from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render
#context of the template



def test(request):
    name = "Celeb"
    t = get_template('index.html')
    html = t.render(Context({'name': name}))
    return HttpResponse(html)

def index(request):
    return HttpResponse('This page shows a list of most recent posts.')
    # return HttpResponse('This page shows a list of most recent posts.')

def test2(request):
    return HttpResponse('meow')
   # return render_to_response('index.html')


def pretty(request):
    # name = "BOSSHawg"
    # t = get_template('pretty.html')
    # html = t.render(Context({'name': name}))
    return render_to_response('pretty.html')
    # return HttpResponse(html)
