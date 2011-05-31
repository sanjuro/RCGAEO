from google.appengine.ext import webapp

from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import login_required
from google.appengine.ext.webapp.util import run_wsgi_app
import models
import web
from google.appengine.ext import db
import datetime

register = webapp.template.create_template_register()

def truncate(value,maxsize,stopper = '...'):
    """ truncates a string to a given maximum
        size and appends the stopper if needed """
    value = test(value)

    stoplen = len(stopper)
    if len(value) > maxsize and maxsize > stoplen:
       return value[:(maxsize-stoplen)] + stopper
    else:
       return value[:maxsize]

def test(input):
    output = ""
    profile = models.Profile.load(input)
    output = profile.avatar
    
    return output

def replacestringspace(value, replace):
    return value.replace(' ', replace)
#{{ somevariable|replacestringspace:" " }}

register.filter(truncate)
register.filter(replacestringspace)