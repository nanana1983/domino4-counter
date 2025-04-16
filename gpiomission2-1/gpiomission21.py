from gpiozero import LED, Button
from signal import pause

led = LED(17)       # GPIO 17번에 LED 연결
button = Button(12)  # GPIO 2번에 버튼 연결

led.source = button.values  # 버튼 상태를 LED에 바로 전달

pause()  # 프로그램을 계속 실행 상태로 유지
