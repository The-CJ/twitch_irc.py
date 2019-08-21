# Twitch irc Client

Simple to use IRC connection for Twitch optimited for the PhaazeOS project
but usable to any purpose


> Inspired by the code of Rapptz's Discord library (function names and usage)

## Usage

```
import twitch_irc

class MyBot(twitch_irc.Client):

  async def on_ready(self):
    await self.join_channel('my_channel_name')

  async def on_message(self, message):
    print(message.content)

    # do more with your code


x = MyBot()
x.run(token="oauth:supersecret", nickname="cool_username")
```
:copyright: 2018-2019 The_CJ
