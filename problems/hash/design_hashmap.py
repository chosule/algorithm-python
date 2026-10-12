"""
문제: 해시맵 설계 (Design HashMap)
난이도: 보통
출처: LeetCode 706
링크: https://leetcode.com/problems/design-hashmap/

문제 설명:
내장 해시 테이블 라이브러리를 쓰지 않고 HashMap을 직접 설계하라.
- put(key, value): key가 이미 있으면 값을 덮어쓰고, 없으면 새로 추가한다.
- get(key): key에 대응하는 value를 리턴한다. key가 없으면 -1을 리턴한다.
- remove(key): key와 그 값을 제거한다. key가 없으면 아무 것도 하지 않는다.

제약 조건:
- 0 <= key, value <= 10^6
- 최대 10^4번 정도 put/get/remove 호출

예제:
MyHashMap map = new MyHashMap();
map.put(1, 1);
map.put(2, 2);
map.get(1);      // 1 리턴
map.get(3);      // -1 리턴 (없음)
map.put(2, 1);   // key=2 값을 덮어씀
map.get(2);      // 1 리턴
map.remove(2);
map.get(2);      // -1 리턴 (제거됨)
"""

import sys
from pathlib import Path

_here = Path(__file__).resolve().parent
for _parent in (_here, *_here.parents):
    if (_parent / "utils" / "test_helper.py").exists():
        sys.path.insert(0, str(_parent))
        break

from utils.test_helper import TestCase, run_tests  # noqa: E402


class MyHashMap:
    """
    시간복잡도: put/get/remove 평균 O(1) (해시 충돌이 적다는 가정 하에)
    공간복잡도: O(버킷 개수 + 저장된 키 개수)

    접근 방법:
    1. 고정 개수의 버킷(리스트들의 리스트)을 미리 만들어둔다.
    2. key % 버킷 개수로 어느 버킷에 넣을지 정한다 (해시 함수).
    3. 같은 버킷 안에서는 (key, value) 쌍을 순서대로 저장한다 (체이닝 방식).
    4. 버킷 하나를 뒤지는 건 그 버킷에 충돌로 몰린 것들만 보면 되니 평균적으로 빠르다.
    """

    def __init__(self):
        self.size = 1000
        self.buckets = [[] for _ in range(self.size)]

    def _hash(self, key: int) -> int:
        return key % self.size

    def put(self, key: int, value: int) -> None:
        bucket = self.buckets[self._hash(key)]
        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))

    def get(self, key: int) -> int:
        bucket = self.buckets[self._hash(key)]
        for k, v in bucket:
            if k == key:
                return v
        return -1

    def remove(self, key: int) -> None:
        bucket = self.buckets[self._hash(key)]
        for i, (k, _) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return


def solution(operations, values):
    """
    operations: 호출할 메서드 이름 리스트 (첫 원소는 항상 "MyHashMap")
    values: 각 연산에 대응하는 인자 리스트 (인자가 없으면 빈 리스트)

    각 연산의 결과를 순서대로 리스트에 담아 리턴한다.
    (생성자/put/remove처럼 리턴값이 없는 연산은 None을 담는다.)
    """
    results = []
    hashmap = None

    for op, args in zip(operations, values):
        if op == "MyHashMap":
            hashmap = MyHashMap()
            results.append(None)
        elif op == "put":
            hashmap.put(args[0], args[1])
            results.append(None)
        elif op == "get":
            results.append(hashmap.get(args[0]))
        elif op == "remove":
            hashmap.remove(args[0])
            results.append(None)

    return results


test_cases = [
    TestCase(
        name="기본 케이스 (LeetCode 예제)",
        input=(
            ["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"],
            [[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]],
        ),
        expected=[None, None, None, 1, -1, None, 1, None, -1],
    ),
    TestCase(
        name="없는 key를 get/remove 해도 안전해야 함",
        input=(
            ["MyHashMap", "get", "remove", "get"],
            [[], [100], [100], [100]],
        ),
        expected=[None, -1, None, -1],
    ),
    TestCase(
        name="해시 충돌 (같은 버킷에 걸리는 key들)",
        input=(
            ["MyHashMap", "put", "put", "get", "get", "remove", "get", "get"],
            [[], [1, 10], [1001, 20], [1], [1001], [1], [1], [1001]],
        ),
        expected=[None, None, None, 10, 20, None, -1, 20],
    ),
    TestCase(
        name="같은 key에 여러 번 put (덮어쓰기)",
        input=(
            ["MyHashMap", "put", "put", "put", "get"],
            [[], [5, 1], [5, 2], [5, 3], [5]],
        ),
        expected=[None, None, None, None, 3],
    ),
]

if __name__ == "__main__":
    run_tests(solution, test_cases)
