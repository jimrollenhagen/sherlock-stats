from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
	"""Extra settings for the user, e.g. time zone, preferences, etc"""

	user = models.ForeignKey(User, unique=True)
	whatcd_id = models.IntegerField(default=0)
	whatcd_username = models.CharField(max_length=32, default='')

	def __unicode__(self):
		return '%s: %s on What.CD' % (self.user.username, self.whatcd_username)

class TorrentSite(models.Model):
	"""Details of a torrent site"""
	
	name = models.CharField(max_length=128)
	url = models.URLField(max_length=200)

	def __unicode__(self):
		return self.name
