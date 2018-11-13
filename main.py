#!/usr/bin/env python
import sys
from twython import Twython
import time

apiKey = "" #redacted
apiSecret = "" #redacted
accessToken = "" #redacted
accessTokenSecret = "" #redacted
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
