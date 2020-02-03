from __future__ import absolute_import, unicode_literals

from celery import shared_task
import time
from mailengine.models import EventLog
from django.core.mail import send_mail
from crmtest.settings import EMAIL_HOST_USER


@shared_task
def add(x, y):
    time.sleep(10)
    return x + y


@shared_task
def followup(eventlog_object):
    print("inside followup")
    time.sleep(2)
    # sleepvalue = eventlog_object.event_lead.status.followup_wait
    # time.sleep(sleepvalue)
    # if EventLog.objects.filter(id=eventlog_object.id).last().id == eventlog_object.id:
    #     print("True executing..")
    # else:
    #     print("False executing..")
    recepient = ['jithinjkumar@gmail.com']
    message = f"from celery sending a mail with a sleep value"
    subject = f"Testing from followup with delay"
    send_mail(subject, message, EMAIL_HOST_USER, recepient, fail_silently=False)
    return

    # if EventLog.objects.filter(eventlog_object.id).last().event_created_on >= eventlog_object.event_created_on:
    #     # to_address =  eventlog_object.event_lead.assigned_to.first().manager.first().email
    #     # cc_address = "jithin.k@byteacademy.co"
    #     print("inside if")
    #     send_mail('Testing',
    #               'Here is the message.',
    #               'tempbytedeveloper@gmail.com',
    #               ['jithinjkumar@gmail.com'],
    #               fail_silently=False,)
    #     new_event_log = EventLog(event_lead=eventlog_object.event_lead, event_type="Escalation",  salesperson=eventlog_object.event_lead.assigned_to.first(), manager=eventlog_object.event_lead.assigned_to.first().manager.first())
    #     print("Escalalation")
    #     followup(new_event_log)
    #     return
    # elif eventlog_object.event_lead.status=="Proposal":
    # return


# subject = f"Django Mail"
# message = f"Unable to Parse Request. Form - 1 \n {obj_dict}"
# recepient = ["jithinjkumar@gmail.com", "adityateng@gmail.com",
#              "ashravi7@gmail.com", "prince.shaji@byteacademy.co", "shettyakash1997@gmail.com"]
# send_mail(subject, message, EMAIL_HOST_USER,
#           recepient, fail_silently=False)
