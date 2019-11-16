from google.appengine.api import images
from google.appengine.ext import ndb
import time

class User(ndb.Model):
    firstName = ndb.StringProperty(required=True)
    lastName = ndb.StringProperty(required=True)
    score = ndb.StringProperty(required=True, default=0)
    # email = ndb.StringProperty(required=True)
    # friends = ndb.KeyProperty(repeated = True)
    # likedPosts = ndb.KeyProperty(repeated=True)
    # userPosts = ndb.KeyProperty(repeated=True)
    # postImage = ndb.BlobProperty(required = False)
