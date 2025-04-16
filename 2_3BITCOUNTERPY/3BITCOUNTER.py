from gpiozero import LED
from time import sleep

# GPIO 핀 배열 (하위 비트부터): GPIO 5, 27, 22
pins = [LED(5), LED(27), LED(22)]

while True:
    for i in range(8):  # 0부터 7까지
        # 모든 LED 끄기
        for led in pins:
            led.off()

        # i 값을 이진수로 표현하여 해당 비트가 1이면 LED 켜기
        for bit in range(3):
            if (i >> bit) & 1:
                pins[bit].on()

        sleep(1)
