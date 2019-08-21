from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..Classes.client import Client

import asyncio

async def addTraffic(cls:"Client"):
	"""
		should be called after every write counting action (PRIVMSG, JOIN, MSG...)
		Increases traffic value for 30 sec
	"""
	cls.traffic += 1
	await asyncio.sleep(30)
	cls.traffic -= 1

async def trafficQuery(cls:"Client"):
	"""
		get started on Cient.start(),
		a coro thats takes all requests that would be over the limit
		and send them later
	"""
	while cls.running and cls.query_running:
		if cls.traffic <= (cls.request_limit-1) and len(cls.stored_traffic) > 0:
			req = cls.stored_traffic.pop(0)
			await cls.sendContent( req )
		else:
			await asyncio.sleep(0.05)

# # # # #

def update_channel_infos(self, channel):
	"""
	used to update channel infos in self.channels
	it will update all non None attributes in a existing object or create a new entry in self.channels

	returns updated channel
	"""

	if type(channel) != Channel:
		raise AttributeError(f'channel must be "{str(Channel)}" not "{type(channel)}"')

	if type(channel.id) != str:
		raise AttributeError(f'channel id "{str(channel.id)}" type "{type(channel.id)}" is invalid')

	current_state = self.channels.get( channel.id, None )
	if current_state == None:
		self.channels[channel.id] = channel
		return self.channels[channel.id]

	else:
		self.channels[channel.id].update( channel )

	return self.channels[channel.id]

def update_channel_viewer(self, user, operation=None):
	"""
	used to add or remove user in a channel.users object from self.channels
	- for some reason twitch sends joins double or don't send a leave
	  so it's not 100% clear that channel.users contains all viewers
	  #ThanksTwitch
	"""

	if operation not in ['add', 'rem']:
		raise AttributeError('only supports "add" and "rem"')

	if user.channel != None:
		chan = user.channel
	else:
		chan = self.get_channel(name = user.channel_name)

	if chan == None: return

	if operation == 'add':
		if chan.users.get(user.name, None) != None:
			return
		chan.users[user.name] = user

	if operation == 'rem':
		if chan.users.get(user.name, None) == None:
			return
		del chan.users[user.name]

def get_channel(self, **search):
	""" get a channel based on the given kwargs, returns the first channel all kwargs are valid, or None if 0 valid"""
	for chan_id in self.channels:
		chan = self.channels[chan_id]

		valid = True

		for key in search:
			if getattr(chan, key, object) != search[key]:
				valid = False
				break

		if valid:
			return chan


	return None