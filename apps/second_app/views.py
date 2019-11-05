from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string


def index(request):
    return HttpResponse("Welcome!")


def random_word(request):
    context = {
        'random_string': get_random_string(length=14)
    }
    if 'counter' not in request.session:
        request.session['counter'] = 0
    else:
        request.session['counter'] += 1
    return render(request,'second_app/index.html', context)


def random_word_reset(request):
    request.session.clear()
    return redirect('/random_word')
