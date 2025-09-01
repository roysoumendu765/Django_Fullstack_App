import json
import urllib.request
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from newsapi import NewsApiClient
from django.views.decorators.csrf import csrf_exempt
from random import randint
from . models import videoList
from . models import Playlist

def index(request):
    return render(request, 'index.html')


def weather(request):
    if request.method == 'POST':
        city = request.POST['city']
        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&appid=080a537b43257f067c420cc7a8437680').read()
        datalist = json.loads(source)

        data = {
            "a" : str(datalist['sys']['country']),
            "b": str(datalist['coord']['lon']) + ',' + str(datalist['coord']['lat']),
            "c": str(datalist['main']['temp']) + '°C',
            "d": str(datalist['main']['pressure']),
            "e": str(datalist['main']['humidity']),
            "f": str(datalist['weather'][0]['main']),
            "g": str(datalist['weather'][0]['description']),
            "icon": datalist['weather'][0]['icon'],
        }
        print(data)
    else:
        data = {}

    return render(request, "weather.html", data)


def news(request):
    newsApi = NewsApiClient(api_key='17af1b67e52a44fa85a60b1f052df07d')
    headLines = newsApi.get_top_headlines(sources='ign, cnn')
    articles = headLines['articles']
    desc = []
    news = []
    img = []

    for i in range(len(articles)):
        article = articles[i]
        desc.append(article['description'])
        news.append(article['title'])
        img.append(article['urlToImage'])
    mylist = zip(news, desc, img)

    return render(request, "news.html", context={"mylist": mylist})


def music(request):
    paginator= Paginator(Playlist.objects.all(),1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context={"page_obj":page_obj}
    return render(request,"music.html",context)


def videoplayer(request):
    paginator= Paginator(videoList.objects.all(),1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context={"page_obj":page_obj}
    return render(request,"videoplayer.html",context)

def chatroom(request):
    return render(request, 'chatroom.html', {})

def room(request, room_name):
    return render(request, 'room.html', {
        'room_name': room_name
    })

    

#####################################################GAME#############################################
secret = randint(0, 100)
turn = 0
success = False

@csrf_exempt
def guess_game(request):
    global secret , turn, success
    context = {}
    hint = ''
    user_number = None

    if request.method == 'POST' and request.POST.get('guess_number'):
        user_number = int(request.POST['guess_number'])
        turn +=1
        if user_number == secret:
            success = True
        else:
            if(user_number > secret):
                hint = 'lower'
            else:
                hint = 'higher'
        
    else:
        secret = randint(0,100)
        turn = 0
        success = False
        hint = ''
        user_number = None
    
    context['success'] = success
    context['turn'] = turn
    context['hint'] = hint
    context['user_number'] = user_number

    return render(request, 'guess_game.html', context)