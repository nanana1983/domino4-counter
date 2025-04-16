from gpiozero import LED
from time import sleep

# GPIO 핀 배열: 순서대로 점등할 GPIO 핀 번호
pins = [LED(22), LED(17), LED(27), LED(5)]

while True:
    for led in pins:
        # 모든 LED 끄기
        for l in pins:
            l.off()

        # 현재 LED 켜기
        led.on()

        sleep(1)

