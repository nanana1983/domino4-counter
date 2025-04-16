# 🔁 버튼을 누르면 도미노처럼 LED가 순차 점등 (gpiozero, Raspberry Pi)

이 프로젝트는 Raspberry Pi에서 `gpiozero` 라이브러리를 사용하여  
**버튼을 누르면 4개의 LED가 도미노처럼 순차적으로 켜졌다가 꺼지는** 동작을 구현한 예제입니다.

youtube 링크 : https://youtube.com/shorts/mlJwSHOjDMU?si=p8mA0b8CjGhDhT9O

---

## ✨ 주요 기능

- 버튼을 누르면 4개의 LED가 순차적으로 켜짐 → 꺼짐
- `sleep()`을 이용한 지연으로 도미노 효과 구현
- `button.when_pressed`를 이용한 트리거
- `gpiozero.LED` 리스트로 간결한 제어 구조

---
## 📸 LED 작동 예시

| 버튼 상태 | LED 작동 흐름                           |
|------------|------------------------------------------|
| 버튼 누름  | LED1 → LED2 → LED3 → LED4 순으로 켜짐    |
|            | LED1 → LED2 → LED3 → LED4 순으로 꺼짐    |
| 손 뗌      | 동작 없음 (대기 상태)                   |

---

## ⚙️ GPIO 핀 구성

| 구성 요소 | 역할                | GPIO 번호 | 물리 핀 번호 | 연결 설명                                 |
|------------|---------------------|------------|----------------|---------------------------------------------|
| LED 1      | 도미노 시작 (LSB)     | GPIO 5     | 29번           | LED 양극에 연결 (330Ω 저항 권장)            |
| LED 2      | 중간                 | GPIO 27    | 13번           | LED 양극에 연결                              |
| LED 3      | 중간                 | GPIO 17    | 11번           | LED 양극에 연결                              |
| LED 4      | 도미노 마지막 (MSB)  | GPIO 22    | 15번           | LED 양극에 연결                              |
| 버튼       | 입력 트리거          | GPIO 12    | 32번           | 버튼 한쪽을 GPIO에 연결                      |
| GND        | 공통 그라운드         | -          | 6번, 9번 등     | 버튼 및 LED 음극(짧은 다리)을 GND에 연결      |

![image](https://github.com/user-attachments/assets/e8310f55-a19c-46df-b0f1-5dfa27545d58)

