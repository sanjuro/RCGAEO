#!/usr/bin/env python
#
# Copyright 2010 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

"""Comment model implementation.

This model will represent the Comment object, it is link to
a specific event and profile
"""
import datetime

from google.appengine.ext import db
from gaeo.model import BaseModel, SearchableBaseModel

from model.event import Event
from model.profile import Profile

class Comment(BaseModel):
  text = db.TextProperty(required=True)
  commented_at = db.DateTimeProperty(auto_now_add=True)
  # user = db.UserProperty(required=True)#make this a reference property to get user data for comment in html
  commenttype = db.StringProperty() #opinion (like a fb status or tweet) prediction, referree decision, armcharir coaching, facebook, twitter, google, foursquare, buzz
  likes = db.ListProperty(db.Key)
  
Comment.belongs_to(Event)
Comment.belongs_to(Profile)

Comment( text='Yaw, this is the fist cmment', commented_at=datetime.datetime.now()).put()