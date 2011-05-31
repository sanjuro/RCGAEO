import cgi

from google.appengine.ext import db

from gaeo.controller import BaseController

from model.profile import Profile

class ProfileController(BaseController):
    def create(self):
        pass

    def index(self):
        query = Profile.all()
        self.result = query.fetch(limit=1000)

    def new(self):
        pass

    def show(self):
        r = Profile.get(self.params.get('id'))
