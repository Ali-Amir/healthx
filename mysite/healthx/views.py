from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
import healthx.athenaapi

def index(request):
  template = loader.get_template('index.html')
  context = RequestContext(request, {
    'latest_poll_list': None
  })
  return HttpResponse(template.render(context))

def getPatientData(request):
  return HttpResponse(healthx.athenaapi.getPatientData())
