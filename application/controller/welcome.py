import datetime

from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext import db
from google.appengine.ext.webapp import template

from gaeo.controller import BaseController

from model.event import Event
from model.comment import Comment
from model.category import Category
from model.profile import Profile
from model.participant import Participant


class WelcomeController(BaseController):
    """The default Controller

    You could change the default route in main.py
    """
    def index(self):
        now = datetime.datetime.now() #up and coming fixtures
        user = users.get_current_user()
        
        comments = Comment.all() 
        comments.order('-commented_at')
        self.comments = comments.fetch(10)
        # profile = models.Profile.load(user)
        # profile = web.getuserprofile(self)
        events = Event.all()
        events.order('-event_start')
        self.events = events.fetch(10)
        
        categorys = db.GqlQuery("SELECT * FROM Category ORDER BY type ASC") #sorted all sports
        self.categorys = categorys.fetch(10)
        # leagues = None
        # teams = None
        totalusers = db.GqlQuery("SELECT * FROM Profile") #total profiles
        totalusercount = totalusers.count()
        topusers = db.GqlQuery("SELECT * FROM Profile")