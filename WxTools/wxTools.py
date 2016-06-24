#encoding=utf-8
'''
Created on 2016年6月20日

@author: Ant
'''
import urllib,urllib2
import json
#from _mysql import NULL

class wxTools():
    def __init__(self,appid,appsecret):
        self.wxid=appid
        self.wxsecret=appsecret
    
    #获取token方法
    #token获取默认以实例属性作为参数
    def getToken(self,appid='',appsecret=''):
        if appid=='':
            appid=self.wxid
        if appsecret=='':
            appsecret=self.wxsecret
        
        if False:
            pass
        else:
            wxParams=urllib.urlencode({"grant_type":'client_credential',"appid":appid,"secret":appsecret})
            f=urllib.urlopen("https://api.weixin.qq.com/cgi-bin/token?%s"%wxParams)
            wxToken=json.loads(f.read())
            try:
                #print wxToken
                return wxToken["access_token"]
            except:
                return "token获取失败"
            #return wxToken
    
    #菜单设置
    def setMenu(self,token):
        pass
    
    #消息发送
    #
    def sendMessage(self,token):
        pass
           