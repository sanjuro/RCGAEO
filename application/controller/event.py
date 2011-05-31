import cgi

from google.appengine.ext import db

from gaeo.controller import BaseController

from model.event import Event

class EventController(BaseController):
    def create(self):
        pass

    def index(self):
        query = Event.all()
        self.result = query.fetch(limit=1000)

    def new(self):
        pass

    def show(self):
        self.event = Event.get(self.params.get('id'))
