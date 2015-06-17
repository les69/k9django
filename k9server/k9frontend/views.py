from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response, render
from django.template.context import RequestContext
from django.conf import settings
from k9models.models import Message
from k9models.forms import LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
import json
import simplejson
from k9frontend.helpers import *


def index(request):
    return render_to_response("index.html", context_instance=RequestContext(request))

@login_required
def home(request):
    user_list = User.objects.exclude(username="admin")
    return render(request, 'mainPage.html', {'users': user_list})



def login(request):

    if request.method == "GET":
        return render_to_response("login.html", context_instance=RequestContext(request))
    else:
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)

            if user is not None:
                return HttpResponseRedirect(reverse('home'))
            else:
                return render_to_response("login.html", context_instance=RequestContext(request))
        else:
            return render_to_response("login.html", context_instance=RequestContext(request))


@login_required
def get_user_details(request, username):
    user = User.objects.filter(username=username)[0]
    messages = Message.objects.filter(user=user)

    jDict = {}
    jDict['user'] = username
    dictArray = []

    for message in messages:
        messDict = {}
        messDict['id'] = message.pk
        messDict['text'] = message.message_text
        messDict['date'] = convert_date(str(message.recv_date))
        messDict['polarity'] = get_polarity(message.message_text)
        dictArray.append(messDict)

    jDict['messages'] = dictArray
    return render(request, 'user_messages.html', jDict)

@login_required
def get_user_chart(request, username):
    dates = get_message_dates_by_user(User.objects.filter(username=username)[0])

    polarityDict = {}
    subjDict = {}

    for date in dates:
        polarityDict[str(date)] = get_daily_polarity(date)
        subjDict[str(date)] = get_daily_subjectivity(date)

    return render(request, 'chart.html', {'subj':json.dumps(subjDict), 'pol':json.dumps(polarityDict)})


@csrf_exempt
def add_message(request):

    if request.method == 'POST':
        jsonDict = json.loads(request.body)

        message = jsonDict["message"]
        username = jsonDict["user"]

        user = User.objects.filter(username=username)[0]
        m = Message.objects.create(message_text=message, user=user)
        m.save()

    return render_to_response("index.html", context_instance=RequestContext(request))

# Create your views here.
