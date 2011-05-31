import cgi

from google.appengine.ext import db

from gaeo.controller import BaseController

from model.comment import Comment

class CommentController(BaseController):
    def create(self):
        pass

    def index(self):
        query = Comment.all()
        self.result = query.fetch(limit=1000)

    def new(self):
        pass

    def show(self):
        r = Comment.get(self.params.get('id'))
