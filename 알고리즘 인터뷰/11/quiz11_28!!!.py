# Chapter09_28. 해시맵 디자인 (291p)
# 난이도 : ★
# Leet code Num. : 706

# 다음의 기능을 제공하는 해시맵을 디자인하라
# - put(key, value) : 키, 값을 해시맵에 삽입한다. 만약 이미 존재하는 키라면 업데이트한다.
# - get(key) :  키에 해당하는 값을 조회한다. 만약 키가 존재하지 않는다면 -1을 리턴한다.
# - remove(key) : 키에 해당하는 키, 값을 해시맵에서 삭제한다


# MyHashMap hashMap = new MyHashMap();
# hashMap.put(1, 1);
# hashMap.put(1, 2);
# hashMap.get(1);       // 1을 리턴한다
# hashMap.get(3);       // -1을 리턴한다 (키가 존재하지 않음)
# hashMap.put(2, 1);    // 값을 업데이트한다
# hashMap.get(2);       // 1을 리턴한다
# hashMap.remove(2);    // 키 2에 해당하는 키, 값을 삭제한다
# hashMap.get(2);       // -1을 리턴한다 (키가 삭제되어 존재하지 않음)
import collections

class ListNode:
    def __init__(self,key=None,val=None):
        self.key = key
        self.val = val
        self.next = None

class MyHashMap:
    def __init__(self):
        self.dic = collections.defaultdict(ListNode)
        self.size = 1000

    def put(self,key:int,val):
        index = key % self.size
        # self.dic[index] is None 으로 선언시 defaultdict설정과 충돌해 True 가 나오는경우가 없어진다.
        if self.dic[index].val is None:
            self.dic[index] = ListNode(key,val)
            return
        temp = self.dic[index]
        while temp:
            if temp.key == key:
                temp.val = val
                return
            if temp.next is None:
                break
            temp = temp.next

        temp.next = ListNode(key,val)
        return

    def get(self,key:int):
        index = key % self.size
        if self.dic[index].val is None:
            return -1
        temp = self.dic[index]
        while temp:
            if temp.key == key:
                return temp.val
            temp = temp.next
        return -1

    def remove(self,key:int):
        index = key % self.size
        if self.dic[index].val is None:
            return
        temp = self.dic[index]
        if temp.key == key:
            self.dic[index] = ListNode() if temp.next is None else temp.next
            return
        temp1 = temp
        # 와일문에서 temp1 이 이전 리스트를 가르키는데 첫번째 노드가 메인 리스트인경우 오류발생 하지만 위에서 첫번째 노드 검증을 마치고 두번째 노드부터시작한다,
        while temp:
            if temp.key == key:
                temp1.next = temp.next
                return
            temp1,temp = temp,temp.next

        return

def test():
    ht = MyHashMap()
    ht.put(1,1)
    ht.put(2,2)
    assert ht.get(1) == 1
    assert ht.get(3) == -1
    ht.put(2, 1)
    assert ht.get(2) == 1
    ht.remove(2)
    assert ht.get(2) == -1
test()
