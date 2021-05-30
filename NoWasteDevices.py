import pymysql.cursors
import time
from threading import Timer
import pygame
pygame.mixer.init()

#date of access to your db
db=pymysql.connect(host="",user="",password="",db="",charset="") 
cursor=db.cursor()
sql="select YOURrOW from YOURtABLE"     
cur=cursor.execute(sql)
result=cursor.fetchone()

   
def check():
    if(cur > 0):
         for x in result:
             if(x=="h"):
                    print("right")
                    pygame.mixer.music.load('YOURaUDIOfOLDER.MP3')   //audioCommand 
                    pygame.mixer.music.play()                        //available
                    time.sleep(1)                                    //for download
                    via()                                            //in homepage
                    
             if(x=="nord"):
                    print("NordFrame")
                    pygame.mixer.music.load(YOURaUDIOfOLDER.MP3')
                    pygame.mixer.music.play()
                    time.sleep(1)
                    via()      
               
               
             if(x=="g"):
                    print("left")
                    pygame.mixer.music.load('YOURaUDIOfOLDER.mp3')
                    pygame.mixer.music.play()
                    time.sleep(1)
                    via()
                    
                    
             if(x=="sud"):
                     print("sud")
                     pygame.mixer.music.load('YOURaUDIOfOLDER.MP3')
                     pygame.mixer.music.play()
                     time.sleep(1)
                     via()
              
              
             if(x=="s"):
                    pygame.mixer.music.load('YOURaUDIOfOLDER.MP3')
                    pygame.mixer.music.play()
                    time.sleep(1)
                    print("stop")
                    via()              
              
              
             if(x=="b"):
                    print("bottom")
                    pygame.mixer.music.load('YOURaUDIOfOLDER.MP3')
                    pygame.mixer.music.play()
                    time.sleep(1)
                    via()
              
             if(x=="a"):
                    print("goNostop")
                    pygame.mixer.music.load('YOURaUDIOfOLDER.MP3')
                    pygame.mixer.music.play()
                    time.sleep(1)
                    via()     
                    
                    
                    
             if(x=="y"):
                    print("go")
                    pygame.mixer.music.load('YOURaUDIOfOLDER.MP3')
                    pygame.mixer.music.play()
                    time.sleep(1)
                    via()
              
                    
                    
                    
                                         
                                        
                    
    if(cur==0): 
          print("no command inserted") 
          quit()
          
     
    via

      
def via():
    canc="delete from YOUR-Table"
    cursor.execute(canc)
    db.commit()
    quit() 


        



check() 
   
