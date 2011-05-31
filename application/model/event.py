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

"""Event model implementation.

This model will represent the Event object that extends
the PolyModel class as it will be used as a base that will
be the main super class for all event classes
"""
import datetime

from google.appengine.ext import db
from google.appengine.ext.db import polymodel

class Event(polymodel.PolyModel):
    category = db.StringProperty()
    title = db.StringProperty()
    description = db.StringProperty()
    comment_count = db.IntegerProperty()
    period = db.StringProperty()# 1st / 2nd half
    event_start = db.DateTimeProperty(auto_now_add=False)
    event_end = db.DateTimeProperty(auto_now_add=False) #to calculate the estimated match time to show whether match live
    country = db.StringProperty()
    city = db.StringProperty()
    venue = db.StringProperty()
    
"""
Events are classified into two main categories
Competitive and Non-Compeitve they are then further
broken down into the related types
"""

class CompetitveEvent(Event):
    scores = db.ListProperty(db.Key)
    
class NonCompetitiveEvent(Event):
    league = db.StringProperty()  
  
"""
Each event will now be furht classifed to the specific type 
they relate too
"""  
class RugbyEvent(CompetitveEvent):
    league = db.StringProperty()    
    
class ConcertEvent(NonCompetitiveEvent):
    capacity = db.IntegerProperty()
    
class CarnivalEvent(NonCompetitiveEvent):
    theme = db.StringProperty()
    
RugbyEvent( title='Super 14 Semi Fnal', description='This is the semi-final that will be played at Lofties', city='Cape Town', venue='Newlands', event_start=datetime.datetime.now(), league="Super 14").put()
ConcertEvent( title='30STM Cape Town Concert', description='The last stop on the 30 Seconds to Mars World Tour', city='Cape Town', venue='Grand West', event_start=datetime.datetime.now(),  capacity=30000).put()

