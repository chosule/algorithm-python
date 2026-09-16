"""
문제: Daily Temperatures
난이도: 보통
출처: LeetCode 739
링크: https://leetcode.com/problems/daily-temperatures/

문제 설명:
일별 기온 배열 temperatures가 주어질 때, answer[i]는 i번째 날 이후
더 따뜻해지기까지 기다려야 하는 날의 수다. 그런 날이 없으면 0.

제약 조건:
- 1 <= len(temperatures) <= 10^5
- 30 <= temperatures[i] <= 100

예제:
입력: [73,74,75,71,69,72,76,73]
출력: [1,1,4,2,1,1,0,0]
"""

import sys
from pathlib import Path

_here = Path(__file__).resolve().parent
for _parent in (_here, *_here.parents):
    if (_parent / "utils" / "test_helper.py").exists():
        sys.path.insert(0, str(_parent))
        break

from utils.test_helper import TestCase, run_tests  # noqa: E402


def solution_bruteforce(temperatures):
    """
    시간복잡도: O(n^2)
    공간복잡도: O(n)

    접근 방법:
    1. 각 날을 기준으로 그 뒤를 끝까지 훑는다.
    2. 처음으로 더 따뜻한 날을 만나면 날짜 차이를 기록한다(flag로 한 번만).
    3. 끝까지 못 만나면 0을 넣는다.
    """
    result = []

    for index, v in enumerate(temperatures):
        flag = False
        for i in range(index + 1, len(temperatures)):
            if temperatures[i] > v and flag is False:
                flag = True
                result.append(i - index)

        if flag is False:
            result.append(0)

    return result


def solution(temperatures):
    t = temperatures
    # 대기열
    stack = []
    result = [0] * len(t)
    for index,v in enumerate(t):
        # 현재 온도가 이전보다 높으면 그냥 pop 만 , 현재온도가 이전보다 낮으면 index 대기열에 추가
        while stack and v > t[stack[-1]]:
            last = stack.pop()
            result[last] = index - last
        stack.append(index)

    return result

_PERF_N = 3000

test_cases = [
    TestCase(name="기본 케이스", input=([73, 74, 75, 71, 69, 72, 76, 73],),
             expected=[1, 1, 4, 2, 1, 1, 0, 0]),
    TestCase(name="계속 상승", input=([30, 40, 50, 60],), expected=[1, 1, 1, 0]),
    TestCase(name="짧은 상승", input=([30, 60, 90],), expected=[1, 1, 0]),
    TestCase(name="계속 하강", input=([90, 80, 70],), expected=[0, 0, 0]),
    TestCase(name="같은 기온", input=([50, 50, 50],), expected=[0, 0, 0]),
    TestCase(name="원소 하나", input=([30],), expected=[0]),
    # 성능 비교용. 계속 오르는 입력이라 정답은 계산 없이 [1,1,...,1,0]으로 확정된다.
    # 기온 범위(30~100) 제약은 벗어나지만 알고리즘 동작에는 영향이 없다.
    TestCase(name=f"성능 비교 (n={_PERF_N})",
             input=(list(range(_PERF_N)),),
             expected=[1] * (_PERF_N - 1) + [0]),
]

if __name__ == "__main__":
    run_tests({"브루트포스": solution_bruteforce, "스택": solution}, test_cases)
