#! /usr/bin/env python
# -*- coding: utf-8 -*-

import urllib, urllib2
import sys
import json

#有道翻译API申请成功
#API key：783927949
#keyfrom：youdao-for-command
#创建时间：2014-05-04
#网站名称：youdao-for-command
#网站地址：https://github.com/shunde/youdao-dict-command-version
def translate(txt):
    params = urllib.urlencode( {'keyfrom': 'youdao-for-command', 'key': '783927949', 'type': 'data', 'doctype': 'json', 'version': '1.1', 'q': txt })
    url = 'http://fanyi.youdao.com/openapi.do?%s' % params
    data = urllib2.urlopen(url).read()
    #print data
    return json.loads(data)

def main():
    txt = sys.argv[1]
    #print txt
    #print translate(txt)
    data = translate(txt)
    errorCode = data["errorCode"]
    if errorCode == 0:
        trans_txt = data["translation"]
        print ';'.join(trans_txt)
    elif errorCode == 20:
        print "要翻译的文本过长"
    elif errorCode == 30:
        print "无法进行有效的翻译"
    elif errorCode == 40:
        print "Error: 不支持的语言类型"
    else: # errorCode == 50
        print "Error: 无效的key"




if __name__ == "__main__":
    main()





