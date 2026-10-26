"""
문제: 주식가격
난이도: 보통 (Lv.2)
출처: 프로그래머스 42584
링크: https://school.programmers.co.kr/learn/courses/30/lessons/42584

문제 설명:
초 단위로 기록된 주식가격이 담긴 배열 prices가 주어질 때,
각 시점의 가격이 떨어지지 않은 기간은 몇 초인지를 배열로 리턴하라.
- prices = [1, 2, 3, 2, 3] 이면 [4, 3, 1, 1, 0]
  - 1초 시점의 1은 끝까지 안 떨어진다 → 4초
  - 3초 시점의 3은 1초 뒤 2로 떨어진다 → 1초
  - 5초 시점의 3은 뒤에 아무것도 없다 → 0초

제약 조건:
- prices의 각 가격은 1 이상 10,000 이하인 자연수
- prices의 길이는 2 이상 100,000 이하

예제:
입력: prices = [1, 2, 3, 2, 3]
출력: [4, 3, 1, 1, 0]
"""

import sys
from pathlib import Path

_here = Path(__file__).resolve().parent
for _parent in (_here, *_here.parents):
    if (_parent / "utils" / "test_helper.py").exists():
        sys.path.insert(0, str(_parent))
        break

from utils.test_helper import TestCase, run_tests  # noqa: E402


def solution(prices):
    result = []
    count = 0  

    for i in range(len(prices)):
        bought = prices[i] 
        count = 0
        for j in range(i+1,len(prices)):
            count += 1

            if bought > prices[j]:
                break
        
        result.append(count)

    return result


# ========================================
# 테스트 케이스
# ========================================

test_cases = [
    TestCase(name="프로그래머스 예제", input=([1, 2, 3, 2, 3],), expected=[4, 3, 1, 1, 0]),
    TestCase(name="계속 떨어짐", input=([5, 4, 3, 2, 1],), expected=[1, 1, 1, 1, 0]),
    TestCase(name="가격이 계속 같음", input=([1, 1, 1],), expected=[2, 1, 0]),
    TestCase(name="한 번에 여러 시점이 떨어짐", input=([2, 3, 1, 4],), expected=[2, 1, 1, 0]),
    TestCase(name="길이 2", input=([3, 1],), expected=[1, 0]),
]

if __name__ == "__main__":
    run_tests(solution, test_cases)
