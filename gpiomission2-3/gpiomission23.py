from gpiozero import LED, Button
from signal import pause
from time import sleep

# LED 연결 (도미노 순서대로)
leds = [LED(5), LED(27), LED(17), LED(22)]

# 버튼 연결
button = Button(12)

# 도미노 동작 함수
def run_domino():
    for led in leds:
        led.on()
        sleep(0.2)  # 순차적으로 켜짐
    for led in leds:
        led.off()
        sleep(0.2)  # 순차적으로 꺼짐

# 버튼이 눌릴 때 도미노 동작 실행
button.when_pressed = run_domino

pause()  # 계속 실행 유지
