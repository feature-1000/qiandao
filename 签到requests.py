# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 14:20:58 2021

@author: 10232
"""

import requests
import time
import datetime
headers={'User-Agent':"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"}
data={'ZGH': '2019072207',
      'MM': 'dongwei0922'}
url='https://jkxxcj.zjhu.edu.cn/yhb/login'
session=requests.Session()
time.sleep(1)
response = session.post(url,headers=headers,data=data)
if response.text.find("用户登录成功") > 0:
    print('登录成功')
else:
    print('登录失败')

def getYesterday(): 
    today=datetime.date.today() 
    oneday=datetime.timedelta(days=1) 
    yesterday=today-oneday
    yesterdays = str(yesterday).replace("-","")
    return yesterdays
   
data2 ={'healthAnswers':'[{"wtid":"9EEE614EAF6278BDE055BAF66D78638E","hdnr":"9EEFBB53CB4FF262E055000000000001","bcsm":"","zgh":"Base64MjAxOTA3MjIwNw==","hdsj":"20210319","wtlx":"1"},{"wtid":"9E1F1911F0961B0EE055BAF66D78638E","hdnr":"3-3243","zgh":"Base64MjAxOTA3MjIwNw==","hdsj":"20210319","wtlx":"4"},{"wtid":"9E1F1911F0971B0EE055BAF66D78638E","hdnr":"湖州师范学院","zgh":"Base64MjAxOTA3MjIwNw==","hdsj":"20210319","wtlx":"0"},{"wtid":"9E1F1911F0981B0EE055BAF66D78638E","hdnr":"9E1F1911F0A71B0EE055BAF66D78638E","bcsm":"","zgh":"Base64MjAxOTA3MjIwNw==","hdsj":"20210319","wtlx":"1"},{"wtid":"9E1F1911F0991B0EE055BAF66D78638E","hdnr":"9E1F1911F0A91B0EE055BAF66D78638E","bcsm":"","zgh":"Base64MjAxOTA3MjIwNw==","hdsj":"20210319","wtlx":"1"},{"wtid":"9E1F1911F09A1B0EE055BAF66D78638E","hdnr":"9E1F1911F0AC1B0EE055BAF66D78638E","bcsm":"","zgh":"Base64MjAxOTA3MjIwNw==","hdsj":"20210319","wtlx":"1"},{"wtid":"9E1F1911F09B1B0EE055BAF66D78638E","hdnr":"9E1F1911F0B21B0EE055BAF66D78638E","bcsm":"","zgh":"Base64MjAxOTA3MjIwNw==","hdsj":"20210319","wtlx":"1"},{"wtid":"9E1F1911F09C1B0EE055BAF66D78638E","hdnr":"0","bcsm":"","zgh":"Base64MjAxOTA3MjIwNw==","hdsj":"20210319","wtlx":"3"},{"wtid":"9E1F1911F09D1B0EE055BAF66D78638E","hdnr":"9E1F1911F0B41B0EE055BAF66D78638E","bcsm":"","zgh":"Base64MjAxOTA3MjIwNw==","hdsj":"20210319","wtlx":"1"},{"wtid":"9E1F1911F09E1B0EE055BAF66D78638E","hdnr":"0","bcsm":"","zgh":"Base64MjAxOTA3MjIwNw==","hdsj":"20210319","wtlx":"3"},{"wtid":"9E1F1911F09F1B0EE055BAF66D78638E","hdnr":"0","bcsm":"","zgh":"Base64MjAxOTA3MjIwNw==","hdsj":"20210319","wtlx":"3"},{"wtid":"9E1F1911F0A01B0EE055BAF66D78638E","hdnr":"0","bcsm":"","zgh":"Base64MjAxOTA3MjIwNw==","hdsj":"20210319","wtlx":"3"},{"wtid":"9E1F1911F0A11B0EE055BAF66D78638E","hdnr":"0","bcsm":"","zgh":"Base64MjAxOTA3MjIwNw==","hdsj":"20210319","wtlx":"3"},{"wtid":"9E1F1911F0A21B0EE055BAF66D78638E","hdnr":"0","bcsm":"","zgh":"Base64MjAxOTA3MjIwNw==","hdsj":"20210319","wtlx":"3"},{"wtid":"9E1F1911F0A31B0EE055BAF66D78638E","hdnr":"0","bcsm":"","zgh":"Base64MjAxOTA3MjIwNw==","hdsj":"20210319","wtlx":"3"},{"wtid":"9E1F1911F0A41B0EE055BAF66D78638E","hdnr":"9E1F1911F0B61B0EE055BAF66D78638E","bcsm":"","zgh":"Base64MjAxOTA3MjIwNw==","hdsj":"20210319","wtlx":"1"},{"wtid":"9E1F1911F0A51B0EE055BAF66D78638E","hdnr":"9E1F1911F0B91B0EE055BAF66D78638E","bcsm":"","zgh":"Base64MjAxOTA3MjIwNw==","hdsj":"20210319","wtlx":"1"},{"wtid":"9E1F1911F0A61B0EE055BAF66D78638E","hdnr":"9E1F1911F0BC1B0EE055BAF66D78638E","bcsm":"","zgh":"Base64MjAxOTA3MjIwNw==","hdsj":"20210319","wtlx":"1"},{"wtid":"A3B606FBBA8B791AE0538713470A587B","hdnr":"36.5","zgh":"Base64MjAxOTA3MjIwNw==","hdsj":"20210319","wtlx":"0"},{"wtid":"A3B606FBBA8C791AE0538713470A587B","hdnr":"36.5","zgh":"Base64MjAxOTA3MjIwNw==","hdsj":"20210319","wtlx":"0"},{"wtid":"333333","hdnr":"333333no","bcsm":"","zgh":"Base64MjAxOTA3MjIwNw==","hdsj":"20210319","wtlx":"1"}]',
        'zgh:':'Base64MjAxOTA3MjIwNw=='}

now = str(datetime.date.today())
n_ = now.replace('-','')

data2['healthAnswers']=data2['healthAnswers'].replace(getYesterday(),n_)

response2 = requests.post('https://jkxxcj.zjhu.edu.cn/healthanswer/answerQuestion',data=data2)
if response2.text.find("success") > 0:
    print('签到成功')
else:
    print('签到失败')