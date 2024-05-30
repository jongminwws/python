import spidev  # SPI 통신을 위한 spidev 라이브러리 임포트
import time  # 딜레이를 주기 위한 time 라이브러리 임포트

# 변수 초기화
delay = 0.5  # 다음 읽기 사이의 대기 시간 설정 (0.5초)
ldr_channel = 0  # LDR이 연결된 ADC 채널 설정 (채널 0)

# SPI 설정
spi = spidev.SpiDev()  # SPI 객체 생성
spi.open(0, 0)  # SPI 버스 0과 장치 0을 엽니다 (SPI0, CE0)
spi.max_speed_hz = 100000  # SPI 통신 속도 설정 (100kHz)

# ADC 값을 읽는 함수 정의
def readadc(adcnum):
    # ADC 채널 번호가 유효한지 확인 (0에서 7 사이여야 함)
    if adcnum > 7 or adcnum < 0:
        return -1  # 유효하지 않은 경우 -1 반환
    
    # SPI를 통해 데이터 전송 및 수신
    # 1: 시작 비트
    # 8 + adcnum << 4: 단일 종료 비트와 ADC 채널을 선택하는 비트
    # 0: 의미 없는 비트 (데이터 수신을 위한 자리)
    r = spi.xfer2([1, 8 + adcnum << 4, 0])
    
    # 수신된 3바이트의 데이터를 10비트 정수로 변환
    data = ((r[1] & 3) << 8) + r[2]
    return data  # 변환된 10비트 데이터를 반환

# 무한 루프
while True:
    ldr_value = readadc(ldr_channel)  # LDR 값을 읽어옴
    print("-----------------")  # 구분선 출력
    print("POT Value: %d" % ldr_value)  # 읽은 LDR 값 출력
    time.sleep(delay)  # 다음 읽기 전에 0.5초 대기
