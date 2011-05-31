import cgi

from google.appengine.ext import db
from gaeo.controller import BaseController
from model.participant import Participant

class ParticipantController(BaseController):
    def create(self):
        pass

    def index(self):
        query = Participant.all()
        self.result = query.fetch(limit=1000)

    def new(self):
        pass

    def show(self):
        r = Participant.get(self.params.get('id'))
