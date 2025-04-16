
# 🔁 4비트 LED 순차 점등기 (Raspberry Pi + gpiozero)

## 🎥 시연 영상  
[🔗 YouTube 링크] https://youtube.com/shorts/hTBdwhxxYsM?si=CTUly_AnDhOpGkLr

---

## 🧾 프로젝트 개요  
이 프로젝트는 Raspberry Pi의 GPIO 핀 4개를 활용하여 LED를 순차적으로 점등하는 간단한 **LED 시퀀서**입니다.  
Python과 [gpiozero](https://gpiozero.readthedocs.io/) 라이브러리를 사용하여 직관적이고 간단하게 구현되었습니다.

---

## ✨ 주요 기능
- 4개의 LED를 1초 간격으로 순차 점등
- `gpiozero`를 이용한 간편한 GPIO 제어
- 무한 루프를 통한 반복 동작
- 코드 구조가 간단해 초보자에게 적합

---

## 🧠 작동 원리

| 순서 | 켜지는 LED (GPIO) |
|------|------------------|
| 1    | GPIO 22          |
| 2    | GPIO 17          |
| 3    | GPIO 27          |
| 4    | GPIO 5           |

> 각 루프마다 하나의 LED만 켜지고, 나머지는 꺼집니다.

---

## ⚙️ GPIO 핀 구성

| LED 번호 | 비트 순서 | GPIO 번호 | 물리 핀 번호 |
|----------|-----------|-------------|----------------|
| LED 1    | 1번째      | GPIO 22    | 15번          |
| LED 2    | 2번째      | GPIO 17    | 11번          |
| LED 3    | 3번째      | GPIO 27    | 13번          |
| LED 4    | 4번째      | GPIO 5     | 29번          |

- 각 GPIO 핀은 **330Ω 저항을 거쳐 LED의 긴 다리(양극)**에 연결
- **짧은 다리(음극)**는 **GND (핀 6, 9, 14번 등)**에 연결됩니다
- ![image](https://github.com/user-attachments/assets/70fc3376-afe2-40df-b0a2-7e1f98f31d7e)
![Uploading image.png…]()



---

## 🐍 코드 예시

```python
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
