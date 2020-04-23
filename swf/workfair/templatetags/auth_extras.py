from django import template
from django.contrib.auth.models import Group

register = template.Library()

@register.filter(name = 'hasGroup')
def hasGroup(user, groupName):
	return user.groups.filter(name = groupName).exists()