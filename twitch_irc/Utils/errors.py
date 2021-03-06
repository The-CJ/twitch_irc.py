class InvalidAuth(Exception):
	"""
	Raised when twitch gives us an error login response.
	Don't get confused with `InvalidCredentials`, where twitch don't even takes with us.
	"""

class InvalidCredentials(Exception):
	"""
	Raised when twitch refuses to talk with us.
	This only happens when the credentials are in a invalid syntax.
	Most likely it a space in oauth or so:

	Wrong:
	oauth: 895463214654235456

	Right:
	oauth:895463214654235456
	"""

class PingTimeout(Exception):
	"""
	Raised when twitch didn't responded with a PING in some time.
	Most likely means something on twitch site is broken.
	"""

class EmptyPayload(Exception):
	"""
	Raised when twitch sent empty data.
	Most likely means we lost connection without getting a event for it.
	"""
