from collections import deque
def solution(progresses, speeds):
    answer = []
    temp = deque([])
    c = 0 # 일한 일 수

    for i in range(len(progresses)):
        while progresses[i] < 100:
            progresses[i] += speeds[i]
            c += 1

        if progresses[i] >= 100:
            temp.append(c)
            c = 0

    print(temp)
    lll = range(len(temp))
    for _ in lll:
        if temp:
            w1 = temp[0]
            c = 0
            for _ in lll:
                if temp:
                    w2 = temp[0]

                    if w1 >= w2:
                        c += 1
                        temp.popleft()
            answer.append(c)

    #print(temp)

    return answer