import RPi.GPIO as GPIO  # RPi.GPIO 라이브러리를 GPIO라는 이름으로 가져옵니다.
import time  # time 모듈을 가져옵니다.

#서브모터를 pm으로 제어할 핀 번호 설정
SERVO_PIN = 18

#불필요한 warning 제거
GPIO.setwarnings(False)

#GPIO핀의 번호 모드 설정
GPIO.setmode(GPIO.BCM)

#서보핀의 출력 설정
GPIO.setup(SERVO_PIN,GPIO.OUT)

#pwm 인스턴스 servo 생성, 주파수 50으로 설정
servo = GPIO.PWM(SERVO_PIN,50)

#pwm 듀티비 0으로 시작
servo.start(0)


try:
    while True:
        #듀티비를 변경하여 서보모터를 원하는 만큼 움직임
        servo.ChangeDutyCycle(7.5) #90도
        time.sleep(1)
        servo.ChangeDutyCycle(12.5) #180도
        time.sleep(1)
        servo.ChangeDutyCycle(2.5) #0도
        time.sleep(1)
        
except KeyboardInterrupt:
    servo.stop()
    GPIO.cleanup()