import RPi.GPIO as GPIO  # RPi.GPIO 라이브러리를 GPIO라는 이름으로 가져옵니다.
import time  # time 모듈을 가져옵니다.

# GPIO 설정
GPIO.setwarnings(False)  # GPIO 관련 경고 메시지를 비활성화합니다.
GPIO.setmode(GPIO.BCM)   # GPIO 핀 번호 모드를 BCM 모드로 설정합니다.

# GPIO 18번 핀을 출력으로 설정
GPIO.setup(18, GPIO.OUT)
# pwm 인스턴스 p를 만들고 GPIO 18번을 pwm 핀으로 설정, 주파수 = 50hz
p = GPIO.PWM(18, 100)

# 캐리비안의 해적 OST 주파수 (Hz)
Frq = [261, 294, 329, 349, 392, 440, 493, 523, 587, 659, 698, 784]

speed = 0.5  # 음과 음 사이 연주시간 설정 (0.5) 초

p.start(10)  # pwm 시작, 듀티비 = 0
volume = 5  # 듀티 사이클을 이용한 볼륨 설정 (0 ~ 100)
try:
    while 1:
        for fr in Frq:
            p.ChangeDutyCycle(fr)  # 주파수를 fr로 변경
            time.sleep(speed)  # speed 초만큼 딜레이 (0.5)
except KeyboardInterrupt:  # 키보드 crtl+c 눌렀을 때 예외 발생
    pass  # 무한반복을 빠져나와 아래의 코드를 실행
p.stop()  # pwm을 종료
GPIO.cleanup()  # GPIO 설정을 초기화
