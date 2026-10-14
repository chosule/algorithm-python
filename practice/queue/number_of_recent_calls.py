"""
문제: 최근 요청 수 세기 (Number of Recent Calls)
난이도: 쉬움
출처: LeetCode 933
링크: https://leetcode.com/problems/number-of-recent-calls/

문제 설명:
최근 일정 시간 동안 들어온 요청 수를 세는 RecentCounter 클래스를 설계하라.
- RecentCounter(): 요청이 하나도 없는 상태로 초기화한다.
- ping(t): 시각 t(밀리초)에 새 요청을 추가하고,
  [t - 3000, t] 구간(양 끝 포함)에 들어온 요청 수를 리턴한다.

제약 조건:
- 1 <= t <= 10^9
- ping은 매번 이전보다 큰 t로 호출된다. (t는 계속 커지기만 한다)
- ping은 최대 10^4번 호출된다.

예제:
RecentCounter recentCounter = new RecentCounter();
recentCounter.ping(1);     // [1] → 1
recentCounter.ping(100);   // [1, 100] → 2
recentCounter.ping(3001);  // [1, 100, 3001] → 3
recentCounter.ping(3002);  // [100, 3001, 3002] → 3 (1은 구간 [2, 3002] 밖)
"""

import sys
from collections import deque
from pathlib import Path

_here = Path(__file__).resolve().parent
for _parent in (_here, *_here.parents):
    if (_parent / "utils" / "test_helper.py").exists():
        sys.path.insert(0, str(_parent))
        break

from utils.test_helper import TestCase, run_tests  # noqa: E402
from collections import deque

class RecentCounter:

    def __init__(self):
        self.queue = deque()
        self.count = 0

    def ping(self, t: int) -> int:
        # t 가 1, 100, 3001, 3002 일단 들어오는데로 넣기
        self.queue.append(t)
        # deque에 들어온 t들을 [1, 100, 3001, 3002] 에서 pop 한거랑 popleft
        
        while len(self.queue) >= 1:
            # queue = self.queue
            # l = queue.popleft() 
            # r = queue.pop()

            # 가장 왼쪽이랑 가장 끝에있는거랑 비교해서 가장끝에잇는거 빼기 3000 해서 그 사이에 있으면 카운트++
            if self.queue[0] >= self.queue[-1] - 3000:
                self.queue.popleft()
                self.count += 1

        return self.count;

    


def solution(pings):
    """ping할 시각 리스트를 받아 RecentCounter에 차례로 넣고, 각 ping의 결과를 리스트로 리턴한다."""
    counter = RecentCounter()
    return [counter.ping(t) for t in pings]


test_cases = [
    TestCase(name="리트코드 예제", input=([1, 100, 3001, 3002],), expected=[1, 2, 3, 3]),
    TestCase(name="요청 하나", input=([5],), expected=[1]),
    TestCase(name="딱 3000ms 차이는 포함", input=([1, 3001],), expected=[1, 2]),
    TestCase(name="3001ms 차이는 제외", input=([1, 3002],), expected=[1, 1]),
    TestCase(name="한꺼번에 여러 개 밀려남", input=([1, 2, 3, 10000],), expected=[1, 2, 3, 1]),
    TestCase(name="간격이 넓어 매번 혼자", input=([1, 5000, 10000],), expected=[1, 1, 1]),
]

if __name__ == "__main__":
    run_tests(solution, test_cases)
