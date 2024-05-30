import RPi.GPIO as GPIO  # RPi.GPIO 라이브러리를 GPIO라는 이름으로 가져옵니다.
import time  # time 모듈을 가져옵니다.

# GPIO 설정
GPIO.setwarnings(False)  # GPIO 관련 경고 메시지를 비활성화합니다.
GPIO.setmode(GPIO.BCM)   # GPIO 핀 번호 모드를 BCM 모드로 설정합니다.

# GPIO 18번 핀을 출력으로 설정
GPIO.setup(18, GPIO.OUT)
# pwm 인스턴스 p를 만들고 GPIO 18번을 pwm 핀으로 설정, 주파수 = 50hz
p = GPIO.PWM(18,50)

p.start(0) # pwm 시작, 듀티비 = 0

try:
    while 1:
        for dc in range(0,101,5):  # dc의 값은 0에서 100 까지 5 만큼 증가
            p.ChangeDutyCycle(dc)  # dc의 값으로 듀티비 변경
            time.sleep(0.1)        # 0.1 초 딜레이
        for dc in range(100,-1,-50): # dc의 값은 100에서 0 까지 5만큼 감소
            p.ChangeDutyCycle(dc)    # dc 의 값으로 듀티비 변경
            time.sleep(0.1)          # .01 초 딜레이 
            
except KeyboardInterrupt: # 키보드 crtl+c 눌렀을 때 예외 발생
    pass                  # 무한반복을 빠져나와 아래의 코드를 실행
p.stop()                  # pwm을 종료
GPIO.cleanup()            # GPIO 설정을 초기화

