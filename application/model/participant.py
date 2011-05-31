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

"""Participant model implementation.

This model will represent the Participant object that extends
the Expando class as it will have dynamic properties
"""
from google.appengine.ext import db
from gaeo.model import BaseModel, SearchableBaseModel

from model.profile import Profile
from model.event import Event

class Participant(BaseModel):
    profile = db.ReferenceProperty(Profile, collection_name='profile')
    registered = db.DateTimeProperty(auto_now_add=True)
    name = db.StringProperty()
    description = db.StringProperty()
    country = db.StringProperty()
    city = db.StringProperty()
    facebookid = db.StringProperty()
    twitterid = db.StringProperty()
    user = db.UserProperty(required=True)
    
Participant.belongs_to(Event)