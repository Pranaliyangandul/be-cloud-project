import sys
import json
import time
import requests
import threading
from .notifier import emailsend, dummySend


def User_check(user):
    while True:
        time.sleep(3)
        api = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode="+user.pincd+"&date="+user.date
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        print(api)
        response = requests.get(api, headers=headers)
        op = json.loads(response.text)
        if op['sessions'] == []:
            pass
        else:
            dummySend(user, op)
            sys.exit()


def subcription(rcvr):
    thr = threading.Thread(target=User_check, args=(rcvr,))
    thr.start()