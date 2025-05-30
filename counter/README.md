
# 🔢 3비트 LED 이진 카운터 (Raspberry Pi + pinctrl)

유튜브 링크 : https://youtu.be/8vyzvUJIZ4E

이 Bash 스크립트는 라즈베리파이의 GPIO 핀 3개를 사용해  
**0부터 7까지의 숫자를 이진수 형태로 LED로 표현**하는 3비트 카운터입니다.  
1초마다 숫자가 하나씩 올라가며 LED 상태가 변경됩니다.

---

## ✨ 주요 기능

- 0~7까지 이진수 카운팅 (총 3비트)
- 각 비트를 LED로 표현
- 1초 간격으로 자동 증가
- `pinctrl`을 이용한 GPIO 제어

---

## 🖼️ LED 작동 예시

| 십진수 | 이진수 | LED 3 (2²) | LED 2 (2¹) | LED 1 (2⁰) |
|--------|--------|------------|------------|------------|
| 0      | `000`  | 꺼짐       | 꺼짐       | 꺼짐       |
| 1      | `001`  | 꺼짐       | 꺼짐       | 켜짐       |
| 2      | `010`  | 꺼짐       | 켜짐       | 꺼짐       |
| 3      | `011`  | 꺼짐       | 켜짐       | 켜짐       |
| 4      | `100`  | 켜짐       | 꺼짐       | 꺼짐       |
| 5      | `101`  | 켜짐       | 꺼짐       | 켜짐       |
| 6      | `110`  | 켜짐       | 켜짐       | 꺼짐       |
| 7      | `111`  | 켜짐       | 켜짐       | 켜짐       |

---

## ⚙️ GPIO 핀 구성

| 비트 위치 | LED 번호 | GPIO 번호 | 핀 번호 |
|-----------|-----------|-------------|----------|
| 2⁰ (하위비트) | LED 1    | GPIO 5     | 29번     |
| 2¹          | LED 2    | GPIO 27    | 13번     |
| 2² (상위비트) | LED 3    | GPIO 22    | 15번     |

> 각 GPIO 핀은 **330Ω 저항을 거쳐 LED의 긴 다리(양극)**에 연결되며,  
> **짧은 다리(음극)**는 **GND(예: 핀 6, 9, 14번 등)**에 연결됩니다.
![image](https://github.com/user-attachments/assets/5f1d7552-6862-46b3-bfb4-6f455f629a46)
![image](https://github.com/user-attachments/assets/673b2d2c-b92f-4cb3-abff-b32586934df0)

---

