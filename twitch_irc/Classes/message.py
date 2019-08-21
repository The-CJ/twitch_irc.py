import re
from ..Utils.regex import Message as Regex
from .emote import Emote
from .badge import Badge

class Message(object):
	"""
		This class is generated when a user is sending a message, it turns raw data like:

		@
		badges=moderator/1,premium/1;
		color=#696969;
		display-name=The__CJ;
		emotes=25:6-10;
		id=13e484e8-1d0d-44c0-8b1e-03d76b636688;
		mod=1;
		room-id=94638902;
		subscriber=0;
		tmi-sent-ts=1525706672840;
		turbo=0;
		user-id=67664971;
		user-type=mod
		:the__cj!the__cj@the__cj.tmi.twitch.tv
		PRIVMSG #phaazebot :Hello Kappa /

		into a usable class
	"""
	def __repr__(self):
		return f"<Message user-id='{'messageid'}'>"

	def __str__(self):
		return self.content

	def __init__(self, raw_data):
		self.raw = raw_data.strip('@')				# str

		self.badges_str = None						# str
		self.badges = [] 							# list :: Badge
		self.color = None 							# str
		self.display_name = None 					# str
		self.name = None 							# str
		self.emotes_str = None						# str
		self.emotes = [] 							# list :: Emote
		self.channel_id = None						# str
		self.channel_name = None					# str
		self.user_id = None 						# str
		self.user_type = None 						# str
		self.sub = False 							# bool
		self.mod = False 							# bool
		self.turbo = False 							# bool
		self.content = None 						# str

		self.channel = None							# object :: Channel
		self.author = None							# object :: User

		self.process()
		self.get_emotes()
		self.get_badges()
		del self.raw

	def process(self):
		#badges_str
		search = re.search(Regex.Message.badges_str, self.raw)
		if search != None:
			self.badges_str = search.group(1)

		#color
		search = re.search(Regex.Message.color, self.raw)
		if search != None:
			self.color = search.group(1)

		#display_name
		search = re.search(Regex.Message.display_name, self.raw)
		if search != None:
			self.display_name = search.group(1)

		#name
		search = re.search(Regex.Message.name, self.raw)
		if search != None:
			self.name = search.group(1)

		#emotes_str
		search = re.search(Regex.Message.emotes_str, self.raw)
		if search != None:
			self.emotes_str = search.group(1)

		#room_id | channel_id
		search = re.search(Regex.Message.room_id, self.raw)
		if search != None:
			self.channel_id = search.group(1)

		#room_name | channel_name
		search = re.search(Regex.Message.room_name, self.raw)
		if search != None:
			self.channel_name = search.group(1)

		#user_id
		search = re.search(Regex.Message.user_id, self.raw)
		if search != None:
			self.user_id = search.group(1)

		#user_type
		search = re.search(Regex.Message.user_type, self.raw)
		if search != None:
			self.user_type = search.group(1)

		#sub
		search = re.search(Regex.Message.sub, self.raw)
		if search != None:
			self.sub = True if search.group(1) == "1" else False

		#mod
		search = re.search(Regex.Message.mod, self.raw)
		if search != None:
			self.mod = True if search.group(1) == "1" else False

		#turbo
		search = re.search(Regex.Message.turbo, self.raw)
		if search != None:
			self.turbo = True if search.group(1) == "1" else False

		#content
		search = re.search(Regex.Message.content, self.raw)
		if search != None:
			self.content = search.group(1).strip('\r')

	def get_emotes(self):
		# 25:0-4,6-10,12-16,24-28/1902:18-22,30-34

		if self.emotes_str in [None, ""]: return

		emote_str_list = self.emotes_str.split("/")
		for emote_str in emote_str_list:
			e = Emote(emote_str, self.content)
			self.emotes.append(e)

	def get_badges(self):
		# moderator/1,premium/1

		if self.badges_str in [None, ""]: return

		badge_str_list = self.badges_str.split(",")
		for badge_str in badge_str_list:
			e = Badge(badge_str)
			self.badges.append(e)


