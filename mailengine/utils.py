def parse_eventlog(eventlog_object):
    sleepvalue = eventlog_object.event_lead.status.followup_wait
    event_id = eventlog_object.id
    recepient = [eventlog_object.event_lead.assigned_to.first().manager.first()]
    message = f"Followup on Lead : {eventlog_object.event_lead.first_name}"
    subject = f"Followup on Lead : {eventlog_object.event_lead.first_name}"
    



