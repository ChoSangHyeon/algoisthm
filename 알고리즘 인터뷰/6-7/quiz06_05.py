# Chapter06_05. 그룹 애너그램 (153p)
# 난이도 : ★★
# Leet code Num. : 49

# 문자열 배열을 받아 애너그램 단위로 그룹핑하라.
# 예제 1.
# 입력 >> ["eat", "tea", "ate", "nat", "tan", "bat"]
# 출력 >> [ ["ate", "eat", "tea"], ["nat", "tan"], ["bat"] ]

import collections
class hi:

    def anagram(self, strs: list[str])->list[list[str]]:
        anagrams = collections.defaultdict(list)
        # anagrams = {}
        # print(anagrams[''])

        for word in strs:
            # print(word[2])
            anagrams[''.join(sorted(word))].append(word)

        return anagrams.values()


if __name__ == "__main__":
    # num_list = list(map(str, input().split()))
    a = ['eat','tea','tan','ate','nat','bat']

    b = hi()
    print(b.anagram(a))
    print(' ')
    print(list(b.anagram(a)))