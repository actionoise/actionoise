from gpiozero import CPUTemperature
from datetime import datetime    
from threading import Timer
import pymysql.cursors
import Adafruit_DHT
cpu=CPUTemperature()
internal=(cpu.temperature)
sensor=Adafruit_DHT.DHT11
pin=17
humidity,temperature = Adafruit_DHT.read_retry(sensor,pin)

db=pymysql.connect(host="",port=,user="",password="",db="",charset="")

cursor=db.cursor()
data1=datetime.now()

    #time.sleep(0.1)
#sql= "insert into users (datetime,temp,hum) values (%s,%s,%s)"
#cursor.execute(sql,(data1,temperature,humidity))
#sql="SELECT * FROM users"
        
def tira():
    canc="delete from users"
    cursor.execute(canc)
    db.commit()
    quit()
    #Timer(5.0, rimbalzo).start()

def rimbalzo():
    humidity,temperature = Adafruit_DHT.read_retry(sensor,pin)
    data1=datetime.now()
    sql= "insert into users (datetime,temp,hum,password) values (%s,%s,%s,%s)"
    cursor.execute(sql,(data1,temperature,humidity,internal))
    db.commit()
    Timer(10.0, tira).start()
    
rimbalzo()



#db.commit()
#cursor.execute(sql)
#result=cursor.fetchall()

#for r in result:
      #print(r)

