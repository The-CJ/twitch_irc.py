# -*- coding: utf-8 -*-

"""
##################
Twitch IRC wrapper
##################

Simple to use IRC connection for Twitch optimited for the PhaazeOS project
but usable to any purpose

:copyright: (c) 2018-2018 The_CJ
:license: eee dunno, gonna first finish it

- Inspired by the code of Rapptz's Discord library (function names and usage)

"""

import asyncio, time, re

class Client():
	from .utils import send_pong, send_nick, send_pass,	req_membership,	req_commands, req_tags
	from .commands import send_message,	join_channel, part_channel

	from .message import Message

	def __init__(self, token=None, nickname=None):

		self.running = False

		self.token = token
		self.nickname = nickname
		self.host = "irc.twitch.tv"
		self.port = 6667
		self.last_ping = time.time()

		self.connection_reader = None
		self.connection_writer = None
		self.channels = {}

		self.traffic = 0

	def stop(self):
		self.running = False
		self.connection.close()

	def run(self, **kwargs):
		self.running = True

		self.token = kwargs.get('token', None)
		self.nickname = kwargs.get('nickname', None)

		if self.token == None or self.nickname == None:
			raise AttributeError("'token' and 'nickname' must be provided")

		loop = asyncio.get_event_loop()
		loop.run_until_complete(self.start())

	async def start(self):
		self.last_ping = time.time()

		try:
			#init connection
			self.connection_reader, self.connection_writer = await asyncio.open_connection(host=self.host, port=self.port)
			#start listen

			#login
			await self.send_pass()
			await self.send_nick()

			#get infos
			await self.req_membership()
			await self.req_commands()
			await self.req_tags()

			self.last_ping = time.time()
			await self.listen()

		except:
			self.connection.close()
			self.last_ping = time.time()
			await asyncio.sleep(10)

	async def listen(self):

		#listen to twitch
		while self.running:

			payload = await self.connection_reader.readuntil()
			asyncio.ensure_future( self.on_raw_data(payload) )
			payload = payload.decode('UTF-8')

			#just to be sure
			if payload in ["", " ", None]: continue

			#response to PING
			elif re.match(r'^PING', payload) != None:
				self.last_ping = time.time()
				await self.send_pong()

			#on_ready
			elif re.match(r"^:tmi\.twitch\.tv 001.*", payload) != None:
				asyncio.ensure_future( self.on_ready() )

			#on_message
			elif re.match(r'^@.+\.tmi\.twitch\.tv PRIVMSG #.+', payload) != None:
				asyncio.ensure_future( self.on_message( self.Message(payload) ) )

			#on_member_join
			elif re.match(r"^:tmi.+\.twitch\.tv JOIN #.+", payload) != None:
				asyncio.ensure_future( self.on_member_join( self.User(payload) ) )

	#events
	async def on_raw_data(self, raw):
		"""
		Attributes:
		`raw`  =  type :: bytes

		called every time some bytes of data get received by the client
		"""
		pass

	async def on_ready(self):
		"""
		Attributes:
		None

		called when the client is connected to twitch and is ready to receive or send data
		"""
		pass

	async def on_message(self, message):
		"""
		Attributes:
		`message` = object :: Message

		called when the client received a message in a channel
		"""
		pass

	async def on_member_join(self, user):
		"""
		Attributes:
		`user` = object :: User

		called when a user joined a twitch channel
		[ issen't working on channel with more than 1000 user (twitch don't send normal events, only moderator joins) ]
		"""
		pass

	async def on_member_left(self, user):
		"""
		Attributes:
		`user` = object :: User

		called when a user left a twitch channel
		[ issen't working on channel with more than 1000 user (twitch don't send normal events, only moderator lefts) ]
		"""
		pass

