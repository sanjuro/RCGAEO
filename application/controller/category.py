import cgi

from google.appengine.ext import db

from gaeo.controller import BaseController

from model.category import Category

class CategoryController(BaseController):
    def create(self):
        pass

    def index(self):
        query = Category.all()
        self.result = query.fetch(limit=1000)

    def new(self):
        pass

    def show(self):
        r = Category.get(self.params.get('id'))
