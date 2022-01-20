import collections


def solution(bridge_length, weight, truck_weights):
    ready = collections.deque(truck_weights)
    que = collections.deque()
    cnt = collections.deque()
    answer = 0
    while True:
        t = 0
        if ready:
            for i in que:
                t += i
            t += ready[0]
        print(ready)
        print(cnt)
        print(t)

        if len(que) < bridge_length and t <= weight and ready:
            que.append(ready.popleft())
            cnt.append(0)
        print(que)

        # copy = cnt.copy()
        # for i in range(len(cnt)):
        #     cnt.append(copy[i] + 1)
        #     cnt.popleft()
        # 멍청한 위에 스마트한 아래
        cnt =collections.deque(map(lambda a: a +1,cnt))

        # print(f'cnt={cnt[0]}')
        if cnt[0] >= bridge_length:
            que.popleft()
            cnt.popleft()
        answer += 1
        print(f'answer={answer}=================================================')
        if not ready and not que:
            answer += 1
            break
    return answer


a= 100
b= 100
c =[10]

print(solution(a,b,c))