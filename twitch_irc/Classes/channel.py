from typing import Any, Dict, List, NewType
UserName = NewType("UserName", str)

import re
from .message import Message
from .user import User
from .stores import UserStore
from .undefined import UNDEFINED

ReEmoteOnly:"re.Pattern" = re.compile(r"[@; ]emote-only=(1|0)[; ]")
ReFollowersOnly:"re.Pattern" = re.compile(r"[@; ]followers-only=(\d*?|-1)[; ]")
ReR9k:"re.Pattern" = re.compile(r"[@; ]r9k=(1|0)[; ]")
ReRituals:"re.Pattern" = re.compile(r"[@; ]rituals=(1|0)[; ]")
ReRoomID:"re.Pattern" = re.compile(r"[@; ]room-id=(\d*?)[; ]")
ReSlow:"re.Pattern" = re.compile(r"[@; ]slow=(\d*?)[; ]")
ReSubsOnly:"re.Pattern" = re.compile(r"[@; ]subs-only=(1|0)[; ]")
ReRoomName:"re.Pattern" = re.compile(r"[@; ]ROOMSTATE #(\S*)")

class Channel(object):
	"""
	This class is generated when the bot join's a chat room or some kind of channel update happen,
	into a usable class and adds it to the bots channels dict

	if emergency is True, a message must be given, to create a minimalistic channel class
	"""
	def __repr__(self):
		return f"<{self.__class__.__name__} name='{self.name}'>"

	def __str__(self):
		return self.name or ""

	def __init__(self, raw:str or None, emergency:bool=False, Msg:Message=None):

		# self.broadcaster_lang:str = None
		self._emote_only:bool = UNDEFINED
		self._followers_only:int = UNDEFINED
		self._r9k:bool = UNDEFINED
		self._rituals:int = UNDEFINED
		self._room_id:str = UNDEFINED
		self._slow:int = UNDEFINED
		self._subs_only:bool = UNDEFINED
		self._name:str = UNDEFINED

		self._viewers:Dict[UserName, User] = UserStore()

		if (raw != None) or (Msg != None):
			try:
				if emergency: self.buildFromMessage(Msg)
				else: self.buildFromEvent(raw)

			except:
				raise AttributeError(raw)

	# utils
	def buildFromEvent(self, raw:str) -> None:
		"""
		generated by a ROOMSTATE event, gives us all informations

		@emote-only=0;followers-only=-1;r9k=0;rituals=0;room-id=94638902;slow=0;subs-only=0 :tmi.twitch.tv ROOMSTATE #phaazebot
		"""

		#emote_only
		search = re.search(ReEmoteOnly, raw)
		if search != None:
			self._emote_only = True if search.group(1) == "1" else False

		#followers_only
		search = re.search(ReFollowersOnly, raw)
		if search != None:
			self._followers_only = int( search.group(1) )

		#r9k
		search = re.search(ReR9k, raw)
		if search != None:
			self._r9k = True if search.group(1) == "1" else False

		#rituals
		search = re.search(ReRituals, raw)
		if search != None:
			self._rituals = True if search.group(1) == "1" else False

		#room_id | id
		search = re.search(ReRoomID, raw)
		if search != None:
			self._room_id = search.group(1)

		#slow
		search = re.search(ReSlow, raw)
		if search != None:
			self._slow = int( search.group(1) )

		#subs_only
		search = re.search(ReSubsOnly, raw)
		if search != None:
			self._subs_only = True if search.group(1) == "1" else False

		#room_name | name
		search = re.search(ReRoomName, raw)
		if search != None:
			self._name = search.group(1)

	def buildFromMessage(self, Msg:Message) -> None:
		"""
		! emergency function

		generated by a message if no channel was found, only gives a minimum of data
		can maybe get called at the start of the bot, but hopefully not
		"""

		self._channel_id = Msg.room_id
		self._name = Msg.room_name

	def update(self, New:"Channel") -> Dict[str, Any]:
		"""
		together with a new channel object, it updates all attributes that are not None
		"""
		if type(New) != Channel:
			raise AttributeError( f'channel must be "{self.__class__.__name__}" not "{type(New)}"' )

		changes:Dict[str, Any] = {}
		changeable:List[str] = [attr for attr in dir(New) if attr.startswith('_') and not attr.startswith("__")]
		for attr in changeable:

			new_value:Any = getattr(New, attr, None)
			if (new_value == None) or (new_value == UNDEFINED): continue
			old_value:Any = getattr(self, attr, None)

			if new_value == old_value: continue

			setattr(self, attr, new_value)
			changes[attr.lstrip('_')] = new_value

		return changes

	def getViewer(self, **search:dict) -> User or None:
		"""
		get a user from the channel viewers based on the given kwargs,
		returns the first user all kwargs are valid, or None if 0 valid
		"""

		# yeah name based, because its the only thing we always get, no matter if message, join or leave
		for user_name in self.users:
			Viewer:User = self.users[user_name]

			valid:bool = True

			for key in search:
				if getattr(Viewer, key, object) != search[key]:
					valid = False
					break

			if valid: return Viewer

		return None

	# props
	@property
	def emote_only(self) -> bool:
		return bool(self._emote_only)

	@property
	def followers_only(self) -> int:
		return int(self._followers_only or 0)

	@property
	def rituals(self) -> bool:
		return bool(self._rituals)

	@property
	def room_id(self) -> str:
		return str(self._room_id or "")
	@property
	def channel_id(self) -> str:
		return str(self._room_id or "")

	@property
	def slow(self) -> int:
		return int(self._slow or 0)

	@property
	def subs_only(self) -> bool:
		return bool(self._subs_only)

	@property
	def users(self) -> Dict[UserName, User]:
		return self._viewers
	@property
	def viewers(self) -> Dict[UserName, User]:
		return self._viewers

	@property
	def name(self) -> str:
		return str(self._name or "")

	@property
	def broadcaster_lang(self) -> Exception: # depricated
		raise DeprecationWarning("broadcaster_lang is no longer given as a tag from twitch")
