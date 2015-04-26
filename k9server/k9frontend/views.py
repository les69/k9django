from django.shortcuts import render

from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.http import HttpResponse
from ajaxutils.decorators import ajax
from django.db.models import Count

def index(request):
    return render_to_response("index.html", context_instance=RequestContext(request))

# Create your views here.
