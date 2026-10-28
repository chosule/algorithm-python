"""
문제: 더 맵게
난이도: 보통 (Lv.2)
출처: 프로그래머스 42626
링크: https://school.programmers.co.kr/learn/courses/30/lessons/42626

문제 설명:
모든 음식의 스코빌 지수를 K 이상으로 만들고 싶다.
스코빌 지수가 가장 낮은 두 개의 음식을 아래 방법으로 섞어 새 음식을 만든다.
    섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식 + (두 번째로 맵지 않은 음식 * 2)
모든 음식이 K 이상이 될 때까지 반복해서 섞는다.
스코빌 지수 배열 scoville과 원하는 지수 K가 주어질 때, 섞어야 하는 최소 횟수를 리턴하라.
모든 음식을 K 이상으로 만들 수 없으면 -1을 리턴한다.

제약 조건:
- scoville의 길이는 2 이상 1,000,000 이하
- K는 0 이상 1,000,000,000 이하
- scoville의 원소는 각각 0 이상 1,000,000 이하

예제:
입력: scoville = [1, 2, 3, 9, 10, 12], K = 7
출력: 2
- 1 + 2*2 = 5  → [5, 3, 9, 10, 12]
- 3 + 5*2 = 13 → [13, 9, 10, 12] (모두 7 이상)
"""

import heapq
import sys
from pathlib import Path

_here = Path(__file__).resolve().parent
for _parent in (_here, *_here.parents):
    if (_parent / "utils" / "test_helper.py").exists():
        sys.path.insert(0, str(_parent))
        break

from utils.test_helper import TestCase, run_tests  # noqa: E402

def solution(scoville, K):
    heapq.heapify(scoville)  # 리스트를 최소 힙으로 바꿈 → scoville[0]이 항상 가장 작은 값
    count = 0

    while scoville[0] < K:  # 가장 작은 게 K 이상이면 전부 K 이상
        if len(scoville) < 2:  # 섞을 짝이 없으면 실패
            return -1
        first = heapq.heappop(scoville)  # 가장 맵지 않은 음식
        second = heapq.heappop(scoville)  # 두 번째로 맵지 않은 음식
        heapq.heappush(scoville, first + second * 2)  # 섞은 음식을 다시 넣기
        count += 1

    return count


# ========================================
# 테스트 케이스
# ========================================

test_cases = [
    TestCase(name="프로그래머스 예제", input=([1, 2, 3, 9, 10, 12], 7), expected=2),
    TestCase(name="처음부터 모두 K 이상", input=([10, 12], 7), expected=0),
    TestCase(name="한 번 섞어서 딱 K", input=([1, 2], 5), expected=1),
    TestCase(name="끝까지 섞어도 안 됨", input=([1, 1], 10), expected=-1),
    TestCase(name="0끼리 섞으면 계속 0", input=([0, 0, 0], 1), expected=-1),
    TestCase(name="K가 0", input=([0, 0], 0), expected=0),
]

if __name__ == "__main__":
    run_tests(solution, test_cases)
