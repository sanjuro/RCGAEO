from django import template
from google.appengine.ext import webapp
import datetime
import time
from datetime import timedelta

register = webapp.template.create_template_register()

def convertusertimezone(datetimevalue, zone):
    formattedtime = ""
    #formattedtime = datetime.datetime(datetimevalue.year, datetimevalue.month, datetimevalue.day, datetimevalue.hour, datetimevalue.minute, datetimevalue.second, datetimevalue.microsecond, tz_helper.timezone(zone))
    #formattedtime = time.gmtime()
    #formattedtime = time.timezone / -(60*60)
    return formattedtime

def gettimediff(commentdatetime):
    datedifference = datetime.datetime.now() - commentdatetime
    return timedifftext(datedifference)

#evaluate which message to show user according to the time difference
def timedifftext(td):
    text = ""
    if td.days > 1:
        text = str(td.days) + " days ago "
    elif td.days == 1:
        text = str(td.days) + " day ago "
    elif (td.days < 1) and (td.seconds > 3600):
        text = str(td.seconds / 3600) + " hours ago "
    elif (td.seconds < 3600) and (td.seconds > 60):
        text = str(td.seconds / 60) + " minutes ago "
    elif (td.days < 1) and (td.seconds < 60):
        text = str(td.seconds) + " seconds ago "
    else:
        text = str(td.seconds) + " error "
    return text

register.filter(convertusertimezone)
register.filter(gettimediff)