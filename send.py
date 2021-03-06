# -*- coding:utf-8 -*-

import requests
import json
import time

from weather import *
from regex import *

# richthofen
# corp = {'CorpID': 'wx5268515d01bdd54b',
#         'corpsecret': 'bvba0n64Hn-MxPCkzQ6kHre6puvLCDvMxJdZIIijqwhbDgzUy_UORHtv1_cs3UEX', }

# ValarDohaeris
corp = {'CorpID': 'wxb6bffdb6811c3034',
        'corpsecret': 'vxc4fROTxzTmPJEfsYQCOrMGMNi66EYy6wk36D_zmAqY_3BFIL6Sy2BKFAvRSqUO', }

def get_token():
    url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken'
    req = requests.post(url, params = corp)
    data = json.loads(req.text)
    return data["access_token"]

def send_msg(msg):
    url = "https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=" + get_token()
    local_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    print(local_time)
    msg = msg + "\\n@" + str(local_time)
    payload = """{"touser":"@all", "toparty":"@all", "agentid":"3", "msgtype":"text", "safe":"0", "text":{"content":"%s"}}""" % (msg)

    data = json.loads(payload)
    print(data)

    req = requests.post(url, payload)
    print(req.text)


if __name__ == '__main__':
    re_test()
    # get_weather1d('101060101')

    # weather_code = {'北京' : '101010100', '长春' : '101060101'}
    # msg = get_weather1d(weather_code['长春'])
    # print(msg)
    # msg = msg.replace('\n', '\\n')
    # msg = str(msg).encode('utf-8').decode('latin1')
    # send_msg(msg)

    # data = str('中文测试\\n@').encode('utf-8').decode('latin1')
    # send_msg(data)
