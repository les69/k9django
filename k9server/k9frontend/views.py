from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.conf import settings
from k9models.models import Message
from k9models.forms import LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
import json


def index(request):
    return render_to_response("index.html", context_instance=RequestContext(request))


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
                return  render_to_response("mainPage.html", context_instance=RequestContext(request))
            else:
                return render_to_response("login.html", context_instance=RequestContext(request))
        else:
            return render_to_response("login.html", context_instance=RequestContext(request))



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
