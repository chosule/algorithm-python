"""연결 리스트 문제용 노드와 변환 함수

ListNode를 문제 파일 안에 두면 scripts/practice.py가 클래스 메서드를 지워버리므로
여기에 따로 둔다. 테스트는 파이썬 리스트로 적고 from_list/to_list로 변환한다.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def from_list(values):
    """[1, 2, 3] -> 1 -> 2 -> 3. 빈 리스트면 None."""
    head = None
    for value in reversed(values):
        head = ListNode(value, head)
    return head


def to_list(head):
    """1 -> 2 -> 3 -> [1, 2, 3]. None이면 빈 리스트."""
    values = []
    while head:
        values.append(head.val)
        head = head.next
    return values
