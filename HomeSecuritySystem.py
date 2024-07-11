import time
import glob
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import cv2
import numpy as np
import imutils
from timeit import default_timer as timer
import config
from email import Encoders

##import RPi.GPIO as GPIO
##GPIO.setmode(GPIO.BOARD)
##GPIO.setup(11,GPIO.IN)

global frame,found,w,h,fps,resolution,flag
global xA,yA,xB,yB
xA,yA,xB,yB = None,None,None,None

cap = cv2.VideoCapture(0)
##cap.set(cv2.cv.CV_CAP_PROP_FPS,5)
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

frame = None
thresh = 10.0
fps = 20
resolution = (640,480)
w = 640
h = 480

fourcc = cv2.VideoWriter_fourcc(*'MJPG')
out = cv2.VideoWriter('output.avi',fourcc,fps,(w,h))

def VideMail(VidFileName):
    msg = MIMEMultipart()
    msg['Subject'] = 'Subject'
    msg['From'] =config.DATA_Username
    msg['To'] = 'vinitpimpale@hotmail.com'
    part = MIMEBase('application','octet-stream')
    part.set_payload(open(VidFileName,'rb').read())
    Encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(VidFileName))
    msg.attach(part)
    s = smtplib.SMTP('smtp.gmail.com',587)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(config.DATA_Username,config.DATA_Password)
    s.sendmail(config.DATA_Username,'vinitpimpale@hotmail.com',msg.as_string())
    s.quit()
    
    
def ImgMail(ImgFileName):
    img_data = open(ImgFileName,'rb').read()
    msg = MIMEMultipart()
    msg['Subject'] = 'Subject'
    msg['From'] = config.DATA_Username
    msg['To'] = 'vinitpimpale@hotmail.com'
    image = MIMEImage(img_data,name=os.path.basename(ImgFileName))
    msg.attach(image)
    s = smtplib.SMTP('smtp.gmail.com',587)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(config.DATA_Username,config.DATA_Password)
    s.sendmail(config.DATA_Username,'vinitpimpale@hotmail.com',msg.as_string())
    s.quit()
    

def SendMail():
    msg = MIMEMultipart()
    msg['Subject'] = 'Subject'
    msg['From'] = config.DATA_Username
    msg['To'] = 'vinitpimpale@hotmail.com'
    text = MIMEText('Warning! Someone just entered in your house')
    msg.attach(text)
    s = smtplib.SMTP('smtp.gmail.com',587)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(config.DATA_Username,config.DATA_Password)
    s.sendmail(config.DATA_Username,'vinitpimpale@hotmail.com',msg.as_string())
    s.quit()

i = int(input('Enter the input'))
flag= True
found = True
while True:
##    i = GPIO.input(11)
    if i == 0:
        print ('No Intruder')
        time.sleep(5)

    elif i == 1:
        print('Intruder Alert, Photo is also captured')
        ret,frame = cap.read()
##        frame = imutils.resize(frame,width = min(400,frame.shape[1]))
        orig = frame.copy()
        out.write(orig)
        rects,weights = hog.detectMultiScale(frame,winStride=(4,4),padding=(1,1),scale=1.05)

        for (x,y,w,h) in rects:
            cv2.rectangle(orig,(x,y),(x+w,y+h),(0,0,255),2)
            
            
        
        rects = np.array([[x,y,x+w,y+h] for (x,y,w,h) in rects])
        for(xA,yA,xB,yB) in rects:
            cv2.rectangle(frame,(xA,yA),(xB,yB),(0,0,255),2)
            
        start = timer()
        
        if flag:
            flag = False
            SendMail()
        out.write(orig)
        if (start>thresh):
            crop_image = orig[yA:yB,xA:xB]
            cv2.imwrite('Cropped.png',crop_image)
            thresh = thresh*3
            ImgMail('Cropped.png')
            VideMail('output.avi')
            break

cap.release()
out.release()
cv2.destroyAllWindows()
     


        
        
