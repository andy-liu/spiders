#-*- coding:utf-8 -*-
import re
import requests


def dowmload_image(html):
    image_url = re.findall('<img .*? data-original="(.*?)"', html, re.S)
    print(len(image_url))
#     for each in image_url:
#         print (each)
    i = 0
    print('现在开始下载图片...')
    for each in image_url:
        print('正在下载第'+str(i+1)+'张图片，图片地址:'+str(each))
        try:
            image= requests.get(each, timeout=20)
        except Exception:
            print('【错误】当前图片无法下载')
            continue
        image_path = 'D:\\spider_result\\image003\\'+ 'image' + '-' + str(i) + ".jpg"
        with open(image_path,'wb') as fp:
            fp.write(image.content)
            i += 1
    print('下载完成')

if __name__ == '__main__':
    url = 'http://www.mafengwo.cn/photo/12700/scenery_6870266_1.html'
    Response = requests.get(url)
    print(Response.status_code)
    dowmload_image(Response.text)
    