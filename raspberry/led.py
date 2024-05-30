# 필요한 모듈을 불러온다
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
# 사용할 gpio핀의 번호를 선정한다
LED=8

GPIO.setup(LED,GPIO.OUT,initial=GPIO.LOW)
# 반복문
try:
	while 1:
		GPIO.output(LED,GPIO.HIGH)
		time.sleep(0.1) # 0.1초동안 불이 켜진다
		
		GPIO.output(LED,GPIO.LOW)
		time.sleep(0.1) # 0.1초 동안 불이 꺼진다  즉 불이 0.1초 단위로 계속 깜빡거림
except KeyboardInterrupt:
	pass
	
GPIO.cleanup()