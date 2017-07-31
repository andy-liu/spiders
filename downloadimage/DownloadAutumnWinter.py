#-*- coding:utf-8 -*-
import re
import requests

def dowmload_image(html):
    image_url = re.findall('<img .*? data-src="(.*?)"', html, re.S)
    i = 0
    print('现在开始下载图片...')
    for each in image_url:
        print('正在下载第'+str(i+1)+'张图片，图片地址:'+str(each))
        try:
            image= requests.get(each, timeout=20)
            image_path = 'D:\\spider_result\\image005\\'+ 'image' + '-' + str(i) + ".jpg"
            with open(image_path,'wb') as fp:
                fp.write(image.content)
            i += 1
        except Exception:
            print('【错误】当前图片无法下载')
            continue
    print('下载完成')
    
        
if __name__ == '__main__':
    url = 'http://www.vogue.co.uk/shows/autumn-winter-2015-ready-to-wear/westminster-university/collection/'
    Response = requests.get(url)
    print(Response.status_code)
    dowmload_image(Response.text)