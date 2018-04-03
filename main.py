#!/usr/bin/env python
import sys
from twython import Twython
import time

apiKey = "bWj659T4CGMKeP5N2q9sBLJW4"
apiSecret = "CTgjgHsJl94cqdbAmQbpVjlAhiCWiHidUWSUbc0wyEU2vXeOo1"
accessToken = "832293691888918533-BRQOh6vTVKfj7J1OBG0nGv2A0kXplcj"
accessTokenSecret = "Kwt9SKhgZjqgITqtFRUrE6XU8YuCnFSxT8pRKNjRuDOll"
days=1050;
while True:
    print'_____________________________________________________________________________________'

    tweetStr='@KelenKeller38 @thestorysofarca @purenoiserecs It has been '+str(days)+' days since The Story So Far last put out a record. Where is it at?'
    api = Twython(apiKey,apiSecret,accessToken,accessTokenSecret)
    api.update_status(status=tweetStr)
    print ('Tweeted' + tweetStr)
    print'_____________________________________________________________________________________'
    days+=1
    time.sleep(86400)
