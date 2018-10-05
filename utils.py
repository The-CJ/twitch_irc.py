import asyncio
from .channel import Channel

async def send_content(self, content, ignore_limit=False):
	""" used to send content of any type to twitch """
	#request limit 20 / 30sec | even doh you can send 100 in channel with mod status
	if self.traffic <= 19 or ignore_limit:
		self.traffic += 1
		asyncio.ensure_future( self.add_traffic() )
		if type(content) != bytes:
			content = bytes(content, 'UTF-8')
		self.connection_writer.write(content)

	else:
		asyncio.ensure_future(self.on_limit())
		self.stored_traffic.append( content )

async def add_traffic(self):
	""" called after any send_content to reset the traffic """
	await asyncio.sleep(30)
	if self.traffic <= 0: self.traffic = 0
	else: self.traffic -= 1

async def send_query(self):
	""" get started on Cient.run(), a coro thats takes all requests that would be over the limit and send them later """
	while self.running and self.query_running:
		if self.traffic <= 18 and len(self.stored_traffic) > 0:
			req = self.stored_traffic.pop(0)
			await self.send_content( req )
		else:
			await asyncio.sleep(0.05)

# # # # #

async def send_pong(self):
	await self.send_content( "PONG :tmi.twitch.tv\r\n", ignore_limit=True )

async def send_nick(self):
	await self.send_content( "NICK {0}\r\n".format(self.nickname), ignore_limit=True )

async def send_pass(self):
	await self.send_content( "PASS {0}\r\n".format(self.token), ignore_limit=True )

async def req_membership(self):
	await self.send_content( "CAP REQ :twitch.tv/membership\r\n", ignore_limit=True )

async def req_commands(self):
	await self.send_content( "CAP REQ :twitch.tv/commands\r\n", ignore_limit=True )

async def req_tags(self):
	await self.send_content( "CAP REQ :twitch.tv/tags\r\n", ignore_limit=True )

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

	if user.channel_name.lower() == self.nickname.lower(): return
	if operation not in ['add', 'rem']:
		raise AttributeError('only supports "add" and "rem"')

	if user.channel != None:
		chan = user.channel
	else:
		chan = self.get_channel(name = user.channel_name)

	if chan == None: return

	if operation == 'add':
		if chan.users.get(user.name, None) != None:
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