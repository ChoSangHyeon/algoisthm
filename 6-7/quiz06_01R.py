# ★ 오늘 하루도 열공하는 하루 되세요 ★ - 작성자 5기 D반 8조 구름

# Chapter06_01. 유효한 팰린드롬 (138p)
# 난이도 : ★
# Leet code Num. : 125

# 주어진 문자열이 팰린드롬인지 확인하라. 대소문자룰 구분하지 않으며, 영문자와 숫자만을 대상으로 한다.
# 예제 1.
# 입력 >> "A man, a plan, a canal: Panama"
# 출력 >> true
# 예제 2.
# 입력 >> "race a car
# 출력 >> false


def isPalindrome(str):
    str = str.lower()

    i = 0
    j = - i - 1
    isPalin = True
    while True:
        if i + 1 == len(str) // 2 or j + 1 == len(str) // 2:
            break

        if not str[i].isalnum():
            i += 1
        if not str[j].isalnum():
            j -= 1

        if str[i] != str[j]:
            isPalin = False
            break

        i += 1
        j -= 1

    return isPalin


if __name__ == "__main__":
    # mom, rotator, ...
    palin = isPalindrome("m.om")
    print(palin)
