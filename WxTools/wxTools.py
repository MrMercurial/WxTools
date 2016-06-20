#encoding=utf-8
'''
Created on 2016年6月20日

@author: Ant
'''
import urllib,urllib2

class wxTools():
    def getToken(self,appid='',appsceret=''):
        if False:
            pass
        else:
            wxParams=urllib.urlencode({"grant_tpye":"client_credential","appid":appid,"secret":appsceret})
            f=urllib.urlopen("https://api.weixin.qq.com/cgi-bin/token?%s"%wxParams)
            