from django.db import models
from django.contrib.auth.models import User

from sherlock.registration.models import TorrentSite

class Statistic(models.Model):
	"""A snapshot of the user's statistics"""

	created_at = models.DateTimeField(auto_now_add=True)

	site = models.ForeignKey(TorrentSite)
	user = models.ForeignKey(User)

	upload = models.BigIntegerField(null=True, blank=True)
	download = models.BigIntegerField(null=True, blank=True)
	snatched = models.IntegerField(null=True, blank=True)
	seeding = models.IntegerField(null=True, blank=True)
