from django.shortcuts import render
from mailengine.tasks import add, followup
from mailengine.models import EventLog
from django.http import HttpResponse

# Create your views here.

def celerytest(request):
    print("something should run here..")
    eventlog_obj = EventLog.objects.get(pk=1)
    # parse_eventlog(eventlog_obj)
    followup.delay("testing")
    print("testing")
    return HttpResponse("Executed")
