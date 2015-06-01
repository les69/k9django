from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response
from django.template.context import RequestContext


def index(request):

    return render_to_response("index.html", context_instance=RequestContext(request))

@csrf_exempt
def add_message(request):

    if request.method == 'POST':
        message = request.POST.get("message")




    return render_to_response("index.html", context_instance=RequestContext(request))

# Create your views here.
