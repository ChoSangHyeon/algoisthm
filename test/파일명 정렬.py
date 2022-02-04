import re
def solution(files):
    answer = []
    num = re.compile('[0-9]+')
    for i in files:
        temp = []
        find = num.search(i)
        start,end = find.span()
        temp.append(i[:start])
        temp.append(i[start:end])
        temp.append((i[end:]))
        answer.append(temp)
    print(answer)
    answer.sort(key=lambda x:(str.lower(x[0]),int(x[1])))
    answerf = []
    for i in answer:
        answerf.append(i[0]+str(i[1])+i[2])

    return answerf

test = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
print(solution(test))

# b = re.compile('[0-9]+')
# a = 'hi2213hi21'
# c = b.search(a)
# d,e = c.span()
# print(d,e)

#  문자에서 내가 원하는 값을 찾는 re 함수의 컴파일 서치를 이용해 원하는 문자가 처음나올때의 범위를
# 스팬을 통해서 구하고 이를 이용해준다. 또 정렬을 할때 원하는 형식안에 정렬할값을 넣어줘도 괜찮다.