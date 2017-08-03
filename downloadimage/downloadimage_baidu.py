#-*- coding:utf-8 -*-
import os
import re
import urllib
import json
import string
import socket
import urllib.request
import requests
import random

def spider(page_number, key_world):
    pn = 0
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    search = urllib.parse.quote(key_world)
    cur_dir = 'D:\spider_result'
#     cur_dir = 'E:\saving images'
    folder_name = 'image' + '_'+ ''.join(random.sample(string.ascii_letters + string.digits, 8))
    image_save_path = os.path.join(cur_dir, folder_name)
    if not os.path.exists(image_save_path):
        os.mkdir(image_save_path)
        
    for each in range(int(page_number)):
        print('正在下载第' + str(each+1)+ '页的图片')
        url = 'http://image.baidu.com/search/avatarjson?tn=resultjsonavatarnew&ie=utf-8&word=' + search + '&cg=girl&pn=' + str(
                pn) + '&rn=60&itg=0&z=0&fr=&width=&height=&lm=-1&ic=0&s=0&st=-1&gsm=1e0000001e'
        try:
            req = urllib.request.Request(url=url, headers=headers)
            page = urllib.request.urlopen(req)
            data = page.read().decode('utf8')
            json_data = json.loads(data)
            save_image(json_data, image_save_path)
            pn = pn + 60
        except Exception:
            print('哎呀，出错了！')
            continue

def save_image(json, image_save_path):
    i = 0
    random_string = ''.join(random.sample(string.ascii_letters + string.digits, 8))
    for info in json['imgs']:
        print('正在下载第' + str(i+1) + '张图片：图片地址为'+ info['objURL'])
        try:
            image= requests.get(info['objURL'], timeout=20)
        except Exception:
            print('【不好意思，出错了】当前图片无法下载')
            continue
        image_path = image_save_path+ '/' + 'image' + '_'+ random_string + '_' + str(i) + ".jpg"
        with open(image_path,'wb') as fp:
            fp.write(image.content)
        i += 1
        
key_world = input("请输入要搜索的关键字，输入后回车！ \n")
page_number = input("请输入要爬取的图片页数！ \n")
spider(page_number, key_world)






