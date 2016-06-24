#encoding=utf-8
'''
Created on 2016年6月21日

@author: Ant
'''
from wxTools import wxTools
import urllib,urllib2
import json

appid='wxbf844f771df2017d'
secret='d4624c36b6795d1d99dcf0547af5443d'
wxtest=wxTools(appid,secret)

token=wxtest.getToken(appid=appid,appsecret=secret)
p=urllib.urlencode({"access_token":token})

#########################################
##消息推送测试###########################
# c=json.dumps({
#    "filter":{
#         "is_to_all":True,
#         "group_id":0
#    },
#    "text":{
#       "content":"CONTENT"
#    },
#     "msgtype":"text"
# })
# f=urllib.urlopen('https://api.weixin.qq.com/cgi-bin/message/mass/sendall?%s'%p,c)
# print f.read()
#########################################

##################测试图片上传#######################
# print('测试git上传代码')
# print('第二次')
# print('test')

c={'media':{'filename':'','filelength':'','content-type':'image/jpeg'}}