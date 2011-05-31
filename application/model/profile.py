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

"""Profile model implementation.

This model will represent the Profile object that extends
the Model Class
"""
from google.appengine.ext import db
from gaeo.model import BaseModel, SearchableBaseModel

from model.category import Category

class Profile(BaseModel):
  user = db.UserProperty(required=True)
  registered = db.DateTimeProperty(auto_now_add=True)
  userType = db.StringProperty() #can be an administrator, fan, sport player, sport club, sport team
  name = db.StringProperty()
  description = db.StringProperty()
  email = db.StringProperty()
  mobile = db.StringProperty()
  username = db.StringProperty()
  password = db.StringProperty()
  alias = db.StringProperty()
  categoryPreference = db.ReferenceProperty(Category, collection_name='categoryPreference') #make default None
  city = db.StringProperty()
  state = db.StringProperty()
  country = db.StringProperty()
  profilePicture = db.StringProperty() #user photobucket.com pic
  avatar = db.BlobProperty()
  gender = db.StringProperty()
  facebookid = db.StringProperty()
  twitterid = db.StringProperty()
  loginMechanism = db.StringProperty() #matchcomment, gmail, facebook, twitter
  #alias = db.StringProperty() #to browse a user profile e.g. matchcomment.com/fanname
