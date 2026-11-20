"""
문제: Group Anagrams
난이도: 보통
출처: LeetCode 49
링크: https://leetcode.com/problems/group-anagrams/

문제 설명:
문자열 배열 strs가 주어질 때, 서로 애너그램인 문자열끼리 묶어서 리턴한다.
(LeetCode는 그룹과 원소의 순서를 신경 쓰지 않지만, 여기서는 테스트를 위해
처음 등장한 순서대로 그룹을 만들고 그룹 안에서도 입력 순서를 유지한다.)

제약 조건:
- 1 <= strs.length <= 10^4
- 0 <= strs[i].length <= 100
- strs[i]는 영어 소문자로만 이루어져 있다.

예제:
입력: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
출력: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]

입력: strs = [""]
출력: [[""]]
"""

import sys
from collections import defaultdict
from pathlib import Path

_here = Path(__file__).resolve().parent
for _parent in (_here, *_here.parents):
    if (_parent / "utils" / "test_helper.py").exists():
        sys.path.insert(0, str(_parent))
        break

from utils.test_helper import TestCase, run_tests  # noqa: E402


def solution(strs):
    # dic = {}
    dic = defaultdict(list)

    for v in strs:
        sort = sorted(v) 
        key = ''.join(sort)
                
        dic[key].append(v)
    
    return list(dic.values())
    
    



test_cases = [
    TestCase(
        name="LeetCode 예제 1",
        input=(["eat", "tea", "tan", "ate", "nat", "bat"],),
        expected=[["eat", "tea", "ate"], ["tan", "nat"], ["bat"]],
    ),
    TestCase(name="LeetCode 예제 2", input=([""],), expected=[[""]]),
    TestCase(name="LeetCode 예제 3", input=(["a"],), expected=[["a"]]),
    TestCase(name="전부 애너그램", input=(["abc", "bca", "cab"],), expected=[["abc", "bca", "cab"]]),
    TestCase(name="전부 다름", input=(["a", "b", "c"],), expected=[["a"], ["b"], ["c"]]),
    TestCase(name="빈 문자열 여러 개", input=(["", ""],), expected=[["", ""]]),
]

if __name__ == "__main__":
    run_tests(solution, test_cases)
