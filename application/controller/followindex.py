import cgi

from google.appengine.ext import db

from gaeo.controller import BaseController

from model.followindex import Followindex

class FollowindexController(BaseController):
    def create(self):
        pass

    def index(self):
        query = Followindex.all()
        self.result = query.fetch(limit=1000)

    def new(self):
        pass

    def show(self):
        r = Followindex.get(self.params.get('id'))
