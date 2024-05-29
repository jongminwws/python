import RPi.GPIO as GPIO  # RPi.GPIO 라이브러리를 GPIO라는 이름으로 가져옵니다.
import time  # time 모듈을 가져옵니다.

# 버튼과 LED 핀 번호를 설정합니다.
button_pin = 15  # 버튼이 연결된 GPIO 핀 번호
led_pin = 4     # LED가 연결된 GPIO 핀 번호

# GPIO 설정
GPIO.setwarnings(False)  # GPIO 관련 경고 메시지를 비활성화합니다.
GPIO.setmode(GPIO.BCM)   # GPIO 핀 번호 모드를 BCM 모드로 설정합니다.
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # 버튼 핀을 입력 모드로 설정하고 풀다운 저항을 활성화합니다.
GPIO.setup(led_pin, GPIO.OUT)  # LED 핀을 출력 모드로 설정합니다.

# LED 상태를 나타내는 변수
light_on = False

try:
    print("Press the button...")  # 사용자에게 버튼을 누르라고 안내합니다.
    while True:
        if GPIO.input(button_pin) == GPIO.HIGH:  # 버튼이 눌렸는지 확인합니다.
            time.sleep(0.05)  # 디바운싱을 위해 잠시 대기합니다.
            if GPIO.input(button_pin) == GPIO.HIGH:  # 버튼이 여전히 눌려 있는지 확인합니다.
                light_on = not light_on  # LED 상태를 반전시킵니다.
                GPIO.output(led_pin, GPIO.HIGH if light_on else GPIO.LOW)  # LED를 켜거나 끕니다.
                print("LED ON!" if light_on else "LED OFF!")  # 현재 LED 상태를 출력합니다.
                while GPIO.input(button_pin) == GPIO.HIGH:  # 버튼이 눌린 상태가 유지되는 동안 대기합니다.
                    time.sleep(0.1)  # 100ms 대기합니다.
        time.sleep(0.1)  # 루프를 빠르게 돌지 않도록 100ms 대기합니다.

except KeyboardInterrupt:
    print("Cleaning up GPIO...")  # 사용자가 프로그램을 종료하면 GPIO 핀을 정리합니다.
    GPIO.cleanup()  # 모든 GPIO 설정을 초기화합니다.
