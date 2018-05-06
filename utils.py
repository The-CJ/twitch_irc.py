import asyncio

async def send_pong(self):
	self.connection_writer.write(bytes("PONG :tmi.twitch.tv\r\n", 'UTF-8'))

async def send_nick(self):
	self.connection_writer.write(bytes("NICK {0}\r\n".format(self.nickname), 'UTF-8'))

async def send_pass(self):
	self.connection_writer.write(bytes("PASS {0}\r\n".format(self.token), 'UTF-8'))

async def req_membership(self):
	self.connection_writer.write(bytes("CAP REQ :twitch.tv/membership\r\n", 'UTF-8'))

async def req_commands(self):
	self.connection_writer.write(bytes("CAP REQ :twitch.tv/commands\r\n", 'UTF-8'))

async def req_tags(self):
	self.connection_writer.write(bytes("CAP REQ :twitch.tv/tags\r\n", 'UTF-8'))

