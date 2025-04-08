
# 🁢 LED 도미노 효과 (Raspberry Pi + pinctrl)

유튜브 링크 : https://youtu.be/q9rkVwIB0Yc?si=TCF4KMKnaLINxfkB

이 Bash 스크립트는 라즈베리파이의 GPIO 핀 4개를 사용하여  
LED에 **도미노처럼 순차적으로 불이 들어오는** 효과를 구현합니다.  
LED는 하나씩 차례대로 1초 간격으로 켜졌다가 꺼지며, 다음 LED로 넘어갑니다.

---

## ✨ 주요 기능

- 4개의 LED가 1초 간격으로 순차 점등
- 한 번에 **하나의 LED만 ON**
- 도미노처럼 아래 방향으로 떨어지는 느낌 구현
- `pinctrl`을 이용한 간편한 GPIO 제어

---

## 🧠 작동 방식

1. 모든 LED를 꺼줍니다 (`dl`)
2. 배열 순서에 따라 현재 LED를 하나만 켭니다 (`dh`)
3. 1초간 대기 후 다음 LED로 이동
4. 무한 반복 (`while true`)

---

## ⚙️ GPIO 핀 구성

| 순서 | GPIO 번호 | 핀 번호 | LED 위치 예시 |
|------|-----------|---------|----------------|
| 1    | GPIO 22   | 15번    | 가장 위 LED |
| 2    | GPIO 17   | 11번    | 두 번째 LED |
| 3    | GPIO 27   | 13번    | 세 번째 LED |
| 4    | GPIO 5    | 29번    | 가장 아래 LED |

> 각 GPIO는 330Ω 저항을 통해 LED 양극(긴 다리)에 연결되고,  
> 음극(짧은 다리)은 GND 핀에 연결됩니다.
> ![image](https://github.com/user-attachments/assets/d399c4b5-d6dc-4ffc-bfb6-4f42befd79fe)
![image](https://github.com/user-attachments/assets/a3d78016-bc37-46c9-bf61-e37d78e5c50f)


---


