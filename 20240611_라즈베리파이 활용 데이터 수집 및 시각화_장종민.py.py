import time
import pymysql
import Adafruit_BMP.BMP085 as BMP085


conn = pymysql.connect(host='localhost', user='root', password='1234', db='mydb', charset='utf8')
cursor = conn.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS sensor_data (
        id INT AUTO_INCREMENT PRIMARY KEY,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
        temperature FLOAT,
        pressure FLOAT,
        altitude FLOAT
    )
''')
conn.commit()


sensor = BMP085.BMP085(busnum=1)

while True:
    
    temp = sensor.read_temperature()
    pressure = sensor.read_pressure()
    altitude = sensor.read_altitude()

    print('Temp = {0:0.2f} *C'.format(temp))
    print('Pressure = {0:0.2f} Pa'.format(pressure))
    print('Altitude = {0:0.2f} m'.format(altitude))

    cursor.execute('''
        INSERT INTO sensor_data (temperature, pressure, altitude)
        VALUES (%s, %s, %s)
    ''', (temp, pressure, altitude))
    conn.commit()

    
    print("저장완료")

    time.sleep(30)


conn.close()
