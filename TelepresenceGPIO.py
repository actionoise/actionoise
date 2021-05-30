import pymysql.cursors
import RPi.GPIO as GPIO
import time
from threading import Timer

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(22,GPIO.OUT)   #GPIO Pins connected to driver L298n
GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)
GPIO.setup(5,GPIO.OUT)
GPIO.output(22,GPIO.LOW)
GPIO.output(23,GPIO.LOW)
GPIO.output(24,GPIO.LOW)
GPIO.output(5,GPIO.LOW)
#date of access to your db
db=pymysql.connect(host="",port=,user="",password="",db="",charset="utf8mb4") 
cursor=db.cursor()
sql="SELECT comandi FROM pilotino"     #table and row
cur=cursor.execute(sql)
result=cursor.fetchone()

   
def check():
    if(cur > 0):
         for x in result:
             if(x=="h"):
                    print("right")
                    GPIO.output(22,GPIO.HIGH)  #destro
                    GPIO.output(23,GPIO.LOW)
                    GPIO.output(24,GPIO.HIGH)
                    GPIO.output(5,GPIO.LOW)
                    time.sleep(1/4)           
                    GPIO.output(22,GPIO.LOW)
                    GPIO.output(23,GPIO.LOW)
                    GPIO.output(24,GPIO.LOW)
                    GPIO.output(5,GPIO.LOW)
                    
                    via()
                    #Timer(5, via).start()
                    
                        
                    
             if(x=="g"):
                    print("left")
                    GPIO.output(22,GPIO.LOW)  #sinistro
                    GPIO.output(23,GPIO.HIGH)
                    GPIO.output(24,GPIO.LOW)
                    GPIO.output(5,GPIO.HIGH)
                    time.sleep(1/4)
                    GPIO.output(22,GPIO.LOW)
                    GPIO.output(23,GPIO.LOW)
                    GPIO.output(24,GPIO.LOW)
                    GPIO.output(5,GPIO.LOW)
                    via()
              
              
             if(x=="s"):
                    print("stop")
                    GPIO.output(22,GPIO.LOW)   #stop
                    GPIO.output(23,GPIO.LOW)
                    GPIO.output(24,GPIO.LOW)
                    GPIO.output(5,GPIO.LOW)
                    Timer(0.50, via).start() 
              
              
              
             if(x=="b"):
                    print("bottom")
                    GPIO.output(22,GPIO.LOW)  #indietro
                    GPIO.output(23,GPIO.HIGH)
                    GPIO.output(24,GPIO.HIGH)
                    GPIO.output(5,GPIO.LOW)
                    time.sleep(1/4)
                    GPIO.output(22,GPIO.LOW)
                    GPIO.output(23,GPIO.LOW)
                    GPIO.output(24,GPIO.LOW)
                    GPIO.output(5,GPIO.LOW)
                    via()
              
                    
                    
                    
                    
             if(x=="y"):
                    print("go")
                    GPIO.output(22,GPIO.HIGH) #avanti
                    GPIO.output(23,GPIO.LOW)
                    GPIO.output(24,GPIO.LOW)
                    GPIO.output(5,GPIO.HIGH)
                    time.sleep(1/4)
                    GPIO.output(22,GPIO.LOW)
                    GPIO.output(23,GPIO.LOW)
                    GPIO.output(24,GPIO.LOW)
                    GPIO.output(5,GPIO.LOW)
                    via()
              
                    Timer(2.0, via).start()
                    
                    
                                          
                                        
                    
    if(cur==0): 
          print("no command inserted) 
          quit()
     
    via(     
           
def via():
    canc="delete from pilotino"
    cursor.execute(canc)
    db.commit()
    quit()         


  
check() 
   
  
