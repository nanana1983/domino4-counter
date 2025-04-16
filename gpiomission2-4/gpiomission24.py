from gpiozero import LED, Button
from signal import pause

# GPIO 핀 번호에 따라 LED 리스트 (하위 비트부터)
leds = [LED(5), LED(27), LED(17), LED(22)]

button = Button(12)

counter = 0  # 초기 카운터 값

def update_leds():
    for i in range(4):
        if (counter >> i) & 1:
            leds[i].on()
        else:
            leds[i].off()

def increase_counter():
    global counter
    counter = (counter + 1) % 16  # 0~15 반복
    update_leds()

button.when_pressed = increase_counter

pause()
