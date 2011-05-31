import cgi

from google.appengine.ext import db

from gaeo.controller import BaseController

from model.commentindex import Commentindex

class CommentindexController(BaseController):
    def create(self):
        pass

    def index(self):
        query = Commentindex.all()
        self.result = query.fetch(limit=1000)

    def new(self):
        pass

    def show(self):
        r = Commentindex.get(self.params.get('id'))
