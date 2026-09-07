# 🐍 파이썬 알고리즘 공부 환경

Python으로 알고리즘 문제를 풀고 테스트할 수 있는 환경입니다. ([`~/algorithm`](../algorithm) JS 버전의 Python 버전)

## 📁 폴더 구조

```
algorithm-python/
├── problems/           # 카테고리별 정답 저장소 (풀이 코드 포함)
│   ├── array/         # 배열
│   ├── string/        # 문자열
│   ├── hash/          # 해시
│   ├── stack/         # 스택
│   ├── queue/         # 큐
│   ├── linked_list/   # 연결 리스트
│   ├── tree/          # 트리
│   ├── graph/         # 그래프
│   ├── sorting/       # 정렬
│   ├── search/        # 탐색 (이분 탐색 등)
│   ├── two_pointer/   # 투 포인터
│   ├── greedy/        # 그리디
│   ├── backtracking/  # 백트래킹
│   ├── dp/            # 동적 프로그래밍
│   ├── math/          # 수학
│   └── etc/           # 기타
├── practice/           # scripts/practice.py로 자동 생성되는 복습용 파일 (정답 없음)
├── utils/              # 유틸리티 함수 (테스트 러너)
├── scripts/
│   └── practice.py     # problems/의 정답을 지운 복습용 파일 생성 스크립트
└── template.py          # 새 문제 풀 때 복사해서 쓰는 템플릿
```

## 🎯 사용 방법

### 1. 새 문제 풀기 (정답 저장)

`template.py`를 복사해서 사용하세요:

```bash
cp template.py problems/array/two_sum.py
```

복사한 파일을 열어서 `solution` 함수를 작성하고, 테스트를 돌려 통과를 확인합니다. 이 파일이 정답 원본이 됩니다.

```bash
python3 problems/array/two_sum.py
```

### 2. 나중에 복습하기 (정답 숨기고 재도전)

`scripts/practice.py`가 저장된 정답에서 `solution` 함수 본문만 지운 파일을 `practice/`에 만들어줍니다. 문제 설명과 테스트 케이스는 그대로 남아있어서 그 자리에서 바로 다시 풀고 채점할 수 있습니다.

```bash
python3 scripts/practice.py array/two_sum       # practice/array/two_sum.py 생성
python3 practice/array/two_sum.py               # 다시 풀고 테스트

python3 scripts/practice.py array/two_sum --force  # 이미 있어도 초기화하고 다시 생성
python3 scripts/practice.py --all                 # 지금까지 푼 문제 전체를 한번에 복습용으로 생성 (기존 파일은 건너뜀)
```

막히면 같은 경로의 `problems/`에서 정답을 확인하세요.

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
