#-*- coding:utf-8 -*-
import re
import requests
import string
import os
import random

def dowmload_image(html, path):
    image_url = re.findall('"objURL":"(.*?)",', html, re.S)
    print(len(image_url))
    i = 0
    print('现在开始下载图片...')
    for each in image_url:
        print('正在下载第'+str(i+1)+'张图片，图片地址:'+str(each))
        try:
            image= requests.get(each, timeout=10)
        except requests.exceptions.ConnectionError:
            print('【错误】当前图片无法下载')
            continue
        image_path = path + '/' + 'image' + '-' + str(i) + ".jpg"
        with open(image_path,'wb') as fp:
            # pic.content, You can also access the response body as bytes, for non-text requests
            fp.write(image.content)
        i += 1
    print('下载完成')

if __name__ == '__main__':
    word = '青海湖'
    url = 'http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word='+word+'&ct=201326592&v=flip'
    cur_dir = 'D:\spider_result'
    folder_name = 'image' + '_'+ ''.join(random.sample(string.ascii_letters + string.digits, 8))
    image_save_path = os.path.join(cur_dir, folder_name)
    if not os.path.exists(image_save_path):
        os.mkdir(image_save_path)
    Response = requests.get(url)
    print(Response.status_code)
    # Response.text, read the content of the server's response
    dowmload_image(Response.text, image_save_path)
    print('图片保存在：' + image_save_path)

