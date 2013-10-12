#!/usr/bin/env python
import os
import requests
import sys

import conf

def jabber(message):
    """Sends POST to HipChat Room Message API.

    Keyword arguments:
    message -- String representing the message you want to post.

    """
    message_room_url = 'https://api.hipchat.com/v1/rooms/message'

    payload = {
        'from': conf.SENDER,
        'room_id': conf.ROOM_ID,
        'message': message,
        'message_format': 'text',
        'notify': 1,
        'color': conf.COLOR
    }

    params = {
        'auth_token': conf.AUTH_TOKEN,
        'format': conf.FORMAT
    }

    r = requests.post(message_room_url, params=params, data=payload)
    return r

if __name__ == '__main__':
    r = jabber(sys.argv[1])
    print r.text
