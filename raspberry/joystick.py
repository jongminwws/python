import spidev  # SPI 통신을 위한 spidev 라이브러리 임포트
import time  # 딜레이를 주기 위한 time 라이브러리 임포트

# 변수 초기화
delay = 0.5  # 다음 읽기 사이의 대기 시간 설정 (0.5초)
sw_channel = 0  # 스위치가 연결된 ADC 채널 설정 (채널 0)
vrx_channel = 1  # 조이스틱 X축이 연결된 ADC 채널 설정 (채널 1)
vry_channel = 2  # 조이스틱 Y축이 연결된 ADC 채널 설정 (채널 2)

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
    vrx_pos = readadc(vrx_channel)  # 조이스틱 X축 값을 읽어옴
    vry_pos = readadc(vry_channel)  # 조이스틱 Y축 값을 읽어옴
    sw_val = readadc(sw_channel)  # 스위치 값을 읽어옴

    # 읽은 값을 형식에 맞게 출력
    print("X{} Y:{}".format(vrx_pos, vry_pos, sw_val))
    
    # 다음 읽기 전에 0.5초 대기
    time.sleep(delay)
