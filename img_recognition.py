#coding:utf8
'''python识别简单验证码图片
1、pip install Pillow
2、pip install pytesseract
3、安装tesseract-OCR
如果无法正常运行，再进行第4步。
4、然后在C盘C:\Python27\Lib\site-packages\pytesseract  找到pytesseract.py用pytharm打开
将tesseract_cmd = 'tesseract'   更改为tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'
'''
import pytesseract
from PIL import Image
image = Image.open('code.jpg')  #打开图片1
# image = Image.open('test.png')  #打开图片2
code = pytesseract.image_to_string(image)  #识别图片
print(code)  #打印识别字符串
