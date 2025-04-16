from gpiozero import LED, Button
from signal import pause

led = LED(17)       # GPIO 17번에 LED 연결
button = Button(12)  # GPIO 2번에 버튼 연결

def toggle_led():
    led.toggle()  # LED 상태 반전 (켜져 있으면 끄고, 꺼져 있으면 켬)

button.when_pressed = toggle_led  # 버튼 눌릴 때 실행

pause()  # 프로그램을 계속 실행 상태로 유지
