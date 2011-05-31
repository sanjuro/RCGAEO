from django import template
from google.appengine.ext import webapp
import models

register = webapp.template.create_template_register()

def getprofilefromuser(value):
    profile = models.Profile.load(value)
    return profile

def getprofileavatarfromuser(value):
    profile = models.Profile.load(value)
    return profile.avatar

def getprofilegenderfromuser(value):
    profile = models.Profile.load(value)
    return profile.gender

def getprofilekeyfromuser(value):
    profile = models.Profile.load(value)
    value = profile.key
    return value

def getprofilealiasfromkey(value):
    profile = models.Profile.get(value)
    return profile.alias

def commentlikecheck(value, comment):
    keyfound = "false"
    comment = models.Comment.get(comment)
    for like in comment.likes:
        if like == value:
            keyfound = "true"
            break
    return keyfound

register.filter(getprofilefromuser)
register.filter(getprofileavatarfromuser)
register.filter(getprofilegenderfromuser)
register.filter(getprofilekeyfromuser)
register.filter(getprofilealiasfromkey)
register.filter(commentlikecheck)