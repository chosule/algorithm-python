# 🐍 파이썬 알고리즘 공부 환경

Python으로 알고리즘 문제를 풀고 테스트할 수 있는 환경입니다. ([`~/algorithm`](../algorithm) JS 버전의 Python 버전)

## 📁 폴더 구조

```
algorithm-python/
├── problems/           # 문제별 폴더
│   ├── array/         # 배열 관련
│   ├── string/        # 문자열 관련
│   ├── sorting/       # 정렬 관련
│   ├── search/        # 탐색 관련
│   ├── dp/            # 동적 프로그래밍
│   ├── graph/         # 그래프
│   └── etc/           # 기타
├── utils/             # 유틸리티 함수
└── template.py        # 문제 템플릿
```

## 🎯 사용 방법

### 1. 새 문제 시작하기

`template.py`를 복사해서 사용하세요:

```bash
cp template.py problems/array/two_sum.py
```

### 2. 문제 풀기

복사한 파일을 열어서 `solution` 함수를 작성합니다.

### 3. 테스트 실행

```bash
python3 problems/array/two_sum.py
```

## ✨ 기능

- ✅ 테스트 케이스 자동 검증
- ⏱️ 실행 시간 측정
- 🎨 컬러 출력 (성공/실패 구분)
- 📊 상세한 결과 비교

## 📝 예제

`problems/array/two_sum.py` 참고.

```python
def solution(nums, target):
    seen = {}
    for i, n in enumerate(nums):
        complement = target - n
        if complement in seen:
            return [seen[complement], i]
        seen[n] = i
    return []
```

## 🔧 팁

- 각 문제에 출처와 링크를 주석으로 남기세요
- 시간복잡도와 공간복잡도를 분석해보세요
- 여러 솔루션을 작성하고 비교해보세요
- `input`이 여러 인자면 `TestCase(input=(a, b), ...)`처럼 tuple로 전달하세요
