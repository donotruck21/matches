from __future__ import unicode_literals

from django.db import models
from datetime import datetime
from django.utils import timezone


class User(models.Model):
	alias = models.TextField(max_length=50)
	email = models.TextField(max_length=50)
	# password = 
	skill_level = models.IntegerField()
	created_at = models.DateTimeField(datetime.now())

	def __str__(self):
		return self.alias

	class Meta:
		db_table = 'users'



class Post(models.Model):
	SKILL_PREF = (
		('B','Beginner'),
		('I','Intermediate'),
		('A','Advanced'),
	)

	user = models.ForeignKey(User)
	description = models.TextField(max_length=200)
	skill_pref = models.CharField(max_length=1, choices=SKILL_PREF)
	# zipcode = 
	# time_start = 
	# time_end =
	created_at = models.DateTimeField(datetime.now())

	def __str__(self):
		return self.description

	class Meta:
		db_table = 'posts'



class Message(models.Model):
	user = models.ForeignKey(User)
	post = models.ForeignKey(Post)
	content = models.TextField(max_length=200)
	created_at = models.DateTimeField(datetime.now())

	def __str__(self):
		return self.content

	class Meta:
		db_table = 'messages'




class Comment(models.Model):
	user = models.ForeignKey(User)
	message = models.ForeignKey(Message)
	content = models.TextField(max_length=200)
	created_at = models.DateTimeField(datetime.now())

	def __str__(self):
		return self.content

	class Meta:
		db_table = 'comments'













