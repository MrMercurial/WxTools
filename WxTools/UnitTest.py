#encoding=utf-8
'''
Created on 2016年6月21日

@author: Ant
'''
from wxTools import wxTools
import urllib,urllib2
import json
import pycurl

appid='wxbf844f771df2017d'
secret='d4624c36b6795d1d99dcf0547af5443d'
wxtest=wxTools(appid,secret)

token=wxtest.getToken(appid=appid,appsecret=secret)
p=urllib.urlencode({"access_token":token})
print token
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

# pvar=urllib.urlencode({"access_token":token,"type":"image"})
# c={'media':{'filename':'/home/ant/01.jpg','Content-length':'940','Content-Type':'image/jpeg'}}
# # c={'media':r'D:\01.jpg'}
# data={'file':()}
# t=urllib.urlencode(c)
# request= urllib2.Request('https://api.weixin.qq.com/cgi-bin/media/upload?%s'%pvar,t)
# f=urllib2.urlopen(request)
# #f=urllib.urlopen('https://api.weixin.qq.com/cgi-bin/media/upload?%s'%pvar,t)
c=pycurl.Curl()
url="https://api.weixin.qq.com/cgi-bin/media/upload?access_token=%s&type=%s"%(token,"image")
c.setopt(c.URL,url)
c.setopt(c.SSL_VERIFYPEER,False)
c.setopt(c.SSL_VERIFYHOST,False)
c.setopt(c.CUSTOMREQUEST,"POST")
c.setopt(c.POST,1)
c.setopt(c.POSTFIELDS,urllib.urlencode({"media":'D:\01.jpg'}))
f=c.perform()

print f
# print f.read()