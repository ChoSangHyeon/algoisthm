# Chapter09_31. 상위 K 빈도 요소 (307p)
# 난이도 : ★★
# Leet code Num. : 347

# 상위 K 이상 등장하는 요소를 추출하라
# 예제 1.
# 입력 >> nums = [1, 1, 1, 2, 2, 3], k = 2
# 출력 >> [1, 2]
import collections


def count(li:list,k:int):
    t = {}
    cnt = collections.Counter
    for i in li:
        if not cnt[i]:
            cnt[i] = 1
        else:
            cnt[i] = cnt[i]+1
    print(cnt)
nums = [1,1,1,2,2,3]
k = 2
count(nums,k)