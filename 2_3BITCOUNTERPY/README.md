
# 🔢 3비트 LED 이진 카운터 (Raspberry Pi + gpiozero)

## 🎥 시연 영상  
[🔗 YouTube 링크] https://youtube.com/shorts/8ZWOMymVAoQ?si=EWAtAlz8FFdfsMEc

---

## 🧾 프로젝트 개요  
이 프로젝트는 Raspberry Pi의 GPIO 핀 3개를 이용해 **0부터 7까지의 숫자**를 **이진수 형태로 LED로 표현**하는 3비트 카운터입니다.  
Python과 [gpiozero](https://gpiozero.readthedocs.io/) 라이브러리를 사용해 구현하였으며, **1초 간격으로 LED 상태가 변경**됩니다.

---

## ✨ 주요 기능
- 0~7까지 이진수 카운팅 (총 3비트)
- 각 비트를 LED로 표현
- 1초 간격으로 자동 증가
- `gpiozero`를 이용한 간단한 GPIO 제어

---

## 🖼️ LED 작동 예시

| 십진수 | 이진수 | LED 3 (2²) | LED 2 (2¹) | LED 1 (2⁰) |
|--------|--------|-------------|-------------|-------------|
| 0      | 000    | 꺼짐        | 꺼짐        | 꺼짐        |
| 1      | 001    | 꺼짐        | 꺼짐        | 켜짐        |
| 2      | 010    | 꺼짐        | 켜짐        | 꺼짐        |
| 3      | 011    | 꺼짐        | 켜짐        | 켜짐        |
| 4      | 100    | 켜짐        | 꺼짐        | 꺼짐        |
| 5      | 101    | 켜짐        | 꺼짐        | 켜짐        |
| 6      | 110    | 켜짐        | 켜짐        | 꺼짐        |
| 7      | 111    | 켜짐        | 켜짐        | 켜짐        |

---

## ⚙️ GPIO 핀 구성

| 비트 위치 | LED 번호 | GPIO 번호 | 물리 핀 번호 |
|-----------|-----------|-------------|----------------|
| 2⁰        | LED 1     | GPIO 5     | 29번           |
| 2¹        | LED 2     | GPIO 27    | 13번           |
| 2²        | LED 3     | GPIO 22    | 15번           |

- 각 GPIO는 **330Ω 저항**을 거쳐 LED의 긴 다리(양극)에 연결
- 짧은 다리(음극)는 **GND (예: 핀 6, 9, 14번)**에 연결
- ![image](https://github.com/user-attachments/assets/24aa32a5-c6ec-414b-8ce0-5640ab47cec5)
![image](https://github.com/user-attachments/assets/bc9332ce-f10a-4e66-8af0-db17df3caa5b)


---

## 🐍 코드 예시 (`3bitcounter.py`)

```python
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
