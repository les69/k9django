from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.conf import settings
from k9models.models import Message
from django.contrib.auth.models import User
import json


def index(request):
    return render_to_response("index.html", context_instance=RequestContext(request))

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
