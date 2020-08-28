import re

# IRC events
RePing:"re.Pattern" = re.compile(r"^PING.*")
ReOnReady:"re.Pattern" = re.compile(r"^:tmi\.twitch\.tv 001.*")
ReGarbage:"re.Pattern" = re.compile(r"^.*tmi\.twitch\.tv (002|003|004|366|372|375|376|CAP).*")
ReUserList:"re.Pattern" = re.compile(r"^.*tmi\.twitch\.tv 353.*")
ReWrongAuth:"re.Pattern" = re.compile(r'^:tmi\.twitch\.tv NOTICE \* :Login.*$')
ReJoin:"re.Pattern" = re.compile(r"^.+tmi\.twitch\.tv JOIN #.+$")
RePart:"re.Pattern" = re.compile(r"^.+tmi\.twitch\.tv PART #.+$")
ReRoomState:"re.Pattern" = re.compile(r"^.+tmi\.twitch\.tv ROOMSTATE #.+$")
ReClearChat:"re.Pattern" = re.compile(r"^.+tmi\.twitch\.tv CLEARCHAT #.+$")
ReUserState:"re.Pattern" = re.compile(r"^.+tmi\.twitch\.tv USERSTATE #.+$")
ReClearMsg:"re.Pattern" = re.compile(r"^.+tmi\.twitch\.tv CLEARMSG #.+$")
RePrivMessage:"re.Pattern" = re.compile(r"^.+tmi\.twitch\.tv PRIVMSG #.+$")
ReUserNotice:"re.Pattern" = re.compile(r"^.+tmi\.twitch\.tv USERNOTICE #.+$")

# extended IRC Events
ReUserListData:"re.Pattern" = re.compile(r".*353 .* = #(\S+?) :(.*)$")

# twitch tags
ReBadgeInfo:"re.Pattern" = re.compile(r"[@; ]badge-info=(\S*?)[; ]")
ReBadges:"re.Pattern" = re.compile(r"[@; ]badges=(\S*?)[; ]")
ReBanDuration:"re.Pattern" = re.compile(r"[@; ]ban-duration=(\d*?)[; ]")
ReBits:"re.Pattern" = re.compile(r"[@; ]bits=(\S*?)[; ]")
ReColor:"re.Pattern" = re.compile(r"[@; ]color=#([0-9a-fA-F]*?)[; ]")
ReDisplayName:"re.Pattern" = re.compile(r"[@; ]display-name=(\S*?)[; ]")
ReEmoteOnly:"re.Pattern" = re.compile(r"[@; ]emote-only=(1|0)[; ]")
ReEmotes:"re.Pattern" = re.compile(r"[@; ]emotes=([0-9:,-]*?)[; ]")
ReFollowersOnly:"re.Pattern" = re.compile(r"[@; ]followers-only=(\d*?|-1)[; ]")
ReID:"re.Pattern" = re.compile(r"[@; ]id=([A-Za-z0-9-]*?)[; ]")
ReLogin:"re.Pattern" = re.compile(r"[@; ]login=(\S*?)[; ]")
ReMod:"re.Pattern" = re.compile(r"[@; ]mod=(0|1)[; ]")
ReMsgID:"re.Pattern" = re.compile(r"[@; ]msg-id=(\S*?)[; ]")
ReMsgParamDomain:"re.Pattern" = re.compile(r"[@; ]msg-param-domain=(\S*?)[; ]")
ReMsgParamGiftMounths:"re.Pattern" = re.compile(r"[@; ]msg-param-gift-months=(\d*?)[; ]")
ReMsgParamMassGiftCount:"re.Pattern" = re.compile(r"[@; ]msg-param-mass-gift-count=(\d*?)[; ]")
ReMsgParamMounths:"re.Pattern" = re.compile(r"[@; ]msg-param-months=(\d*?)[; ]")
ReMsgParamCumulativeMonths:"re.Pattern" = re.compile(r"[@; ]msg-param-cumulative-months=(\d*?)[; ]")
ReMsgParamPriorGifterAnonymous:"re.Pattern" = re.compile(r"[@; ]msg-param-prior-anonymous=(true|false)[; ]")
ReMsgParamPriorGifterDisplayName:"re.Pattern" = re.compile(r"[@; ]msg-param-prior-gifter-display-name=(\S*?)[; ]")
ReMsgParamPriorGifterID:"re.Pattern" = re.compile(r"[@; ]msg-param-prior-gifter-id=(\d*?)[; ]")
ReMsgParamPriorGifterUserName:"re.Pattern" = re.compile(r"[@; ]msg-param-prior-gifter-user-name=(\S*?)[; ]")
ReMsgParamProfileImageURL:"re.Pattern" = re.compile(r"[@; ]msg-param-profileImageURL=(\S*?)[; ]")
ReMsgParamRecipientDisplayName:"re.Pattern" = re.compile(r"[@; ]msg-param-recipient-display-name=(\S*?)[; ]")
ReMsgParamRecipientID:"re.Pattern" = re.compile(r"[@; ]msg-param-recipient-id=(\d*?)[; ]")
ReMsgParamRecipientUserName:"re.Pattern" = re.compile(r"[@; ]msg-param-recipient-user-name=(\S*?)[; ]")
ReMsgParamRitualName:"re.Pattern" = re.compile(r"[@; ]msg-param-ritual-name=(\S*?)[; ]")
ReMsgParamSelectedCount:"re.Pattern" = re.compile(r"[@; ]msg-param-selected-count=(\d*?)[; ]")
ReMsgParamShouldShareStreak:"re.Pattern" = re.compile(r"[@; ]msg-param-should-share-streak=(0|1)[; ]")
ReMsgParamStreakMonths:"re.Pattern" = re.compile(r"[@; ]msg-param-streak-months=(\d*?)[; ]")
ReMsgParamSenderCount:"re.Pattern" = re.compile(r"[@; ]msg-param-sender-count=(\d*?)[; ]")
ReMsgParamSenderLogin:"re.Pattern" = re.compile(r"[@; ]msg-param-sender-login=(\S*?)[; ]")
ReMsgParamSenderName:"re.Pattern" = re.compile(r"[@; ]msg-param-sender-name=(\S*?)[; ]")
ReMsgParamSubPlan:"re.Pattern" = re.compile(r"[@; ]msg-param-sub-plan=(\S*?)[; ]")
ReMsgParamSubPlanName:"re.Pattern" = re.compile(r"[@; ]msg-param-sub-plan-name=(\S*?)[; ]")
ReMsgParamTotalRewardCount:"re.Pattern" = re.compile(r"[@; ]msg-param-total-reward-count=(\d*?)[; ]")
ReMsgParamTriggerAmount:"re.Pattern" = re.compile(r"[@; ]msg-param-trigger-amount=(\d*?)[; ]")
ReMsgParamTriggerType:"re.Pattern" = re.compile(r"[@; ]msg-param-trigger-type=(\S*?)[; ]")
ReMsgParamViewerCount:"re.Pattern" = re.compile(r"[@; ]msg-param-viewerCount=(\d*?)[; ]")
ReR9k:"re.Pattern" = re.compile(r"[@; ]r9k=(1|0)[; ]")
ReRituals:"re.Pattern" = re.compile(r"[@; ]rituals=(1|0)[; ]")
ReRoomID:"re.Pattern" = re.compile(r"[@; ]room-id=(\d*?)[; ]")
ReSlow:"re.Pattern" = re.compile(r"[@; ]slow=(\d*?)[; ]")
ReSubscriber:"re.Pattern" = re.compile(r"[@; ]subscriber=(0|1)[; ]")
ReSubsOnly:"re.Pattern" = re.compile(r"[@; ]subs-only=(1|0)[; ]")
ReSystemMsg:"re.Pattern" = re.compile(r"[@; ]system-msg=(\S*?)[; ]")
ReTargetMsgID:"re.Pattern" = re.compile(r"[@; ]target-msg-id=([A-Za-z0-9-]*?)[; ]")
ReTargetUserID:"re.Pattern" = re.compile(r"[@; ]target-user-id=(\d*?)[; ]")
ReTMISendTS:"re.Pattern" = re.compile(r"[@; ]tmi-sent-ts=(\d*?)[; ]")
ReTurbo:"re.Pattern" = re.compile(r"[@; ]turbo=(0|1)[; ]")
ReUserID:"re.Pattern" = re.compile(r"[@; ]user-id=(\d*?)[; ]")
ReUserType:"re.Pattern" = re.compile(r"[@; ]user-type=(\S*?)[; ]")

# other
ReBadgeParts:"re.Pattern" = re.compile(r"^([^/]+)/?(\d+)?$")
ReUserName:"re.Pattern" = re.compile(r"(?:@|;| |^):(\S*?)!(\S*?)@(\S*?)\.tmi\.twitch\.tv[; ]")
ReRoomName:"re.Pattern" = re.compile(r"[@; ](JOIN|PART|CLEARMSG|CLEARCHAT|ROOMSTATE|USERSTATE|PRIVMSG|USERNOTICE) #(\S*?)([; ]|$)")
ReContent:"re.Pattern" = re.compile(r"[@; ](JOIN|PART|CLEARMSG|CLEARCHAT|ROOMSTATE|USERSTATE|PRIVMSG|USERNOTICE) #\S+? :(.+)")
