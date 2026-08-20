# 콜라츠 추측
독일의 수학자 로타르 콜라츠(Lothar Collatz)가 제기한 추측으로 임의의 자연수가 짝수면 2로 나누고, 홀수면 3을 곱하고 1을 더하는 과정을 반복하면 결국 모두 1이 된다는 단순한 규칙 이지만 현재까지 증명되지 않은 난제이다.


<img src="./assets/collatz.svg" width="200" height="200">

### 짝수 연산
현재 수가 짝수이면 2로 나눈다.

### 홀수 연산
현재 수가 짝수이면 3을 곱하고 1을 더한다.

## 구현
```python
while a > 1:
    i = i + 1
    if a % 2 == 0:
        a = a // 2
    else:
        a = 3 * a + 1
```

## 결과

| 42 |
| :---: |
| 21 |
| 64 |
| 32 |
| 16 |
| 8 |
| 4 |
| 2 |
| 1 |

## 사용법
```bash
pip install openpyxl
python Collatz.py
```

# Google Colab
https://colab.research.google.com/drive/1wpSz5LI4A4hLZ1CCnZANH2fKwBKQXZTJ?usp=sharing