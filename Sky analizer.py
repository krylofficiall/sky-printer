import cv2
import os
import time
import datetime
from PIL import Image, ImageDraw
import shutil
count = 0
x = 0
y = 0
now = datetime.datetime.now()
print("Now current time:", now.strftime("%H:%M"))
f_time = str(now.strftime("%H:%M"))
print("Enter your time range:")
l_time = str(input())

while f_time != l_time:
    print('Module cam activated')
    now = datetime.datetime.now()
    f_time = str(now.strftime("%H:%M"))
    count += 1
    count_t = str(count)
    # Включаем первую камеру
    cap = cv2.VideoCapture(0)
    
    # "Прогреваем" камеру, чтобы снимок не был тёмным
    for i in range(40):
        cap.read()
    
    # Делаем снимок    
    ret, frame = cap.read()
    # Записываем в файл
    cv2.imwrite('sight'+ count_t +'.png', frame)
    name1 = 'sight'+ count_t +'.png'
    name = 'sight'+ count_t + '_mono' + '.png'
    print('Photo from cam 1 shot successfully:', name1)
    img = Image.open('sight' + count_t + '.png')
    obj = img.load()
    color = obj[200, 100]
    img = Image.new("RGB", (100, 100), color)
    img.save(name, "PNG")
    
    print('---')
    time.sleep(10)
    print('!--')
    time.sleep(100)
    print('!!-')
    time.sleep(100)
    print('!!!')    

    
print('Your time reached')
cap.release()