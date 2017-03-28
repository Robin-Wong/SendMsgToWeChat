# -*- coding:utf-8 -*-

import requests
import json
import time

# richthofen
corp = {'CorpID': 'wx5268515d01bdd54b',
        'corpsecret': 'bvba0n64Hn-MxPCkzQ6kHre6puvLCDvMxJdZIIijqwhbDgzUy_UORHtv1_cs3UEX', }

# ValarDohaeris
#corp = {'CorpID': 'wxb6bffdb6811c3034',
#        'corpsecret': '7z4TVpC8UH_r1P5CJ4V4v3JqKuBMaYptgAKryMe5UGMQ1Pyns6BwHuEctucSd191', }

def get_token():
    url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken'
    req = requests.post(url, params = corp)
    data = json.loads(req.text)
    return data["access_token"]

def send_msg(msg):
    url = "https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=" + get_token()
    local_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    print(local_time)
    msg = msg + str(local_time)
    payload = """{"touser":"@all", "toparty":"@all", "agentid":"3", "msgtype":"text", "safe":"0", "text":{"content":"%s"}}""" % (msg)

    data = json.loads(payload)
    print(data)

    req = requests.post(url, payload)
    print(req.text)


if __name__ == '__main__':
    data = str('中文测试\\n@').encode('utf-8').decode('latin1')
    send_msg(data)
