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

# def solution(bridge_length, weight, truck_weights):
#     lists = deque([0]*bridge_length)
#     count = 0
#     while truck_weights:
#         if sum(lists, truck_weights[0]-lists[0]) <= weight:
#             lists.popleft()
#             lists.append(truck_weights.pop(0))
#             count += 1
#             print(lists)
#             print(truck_weights)
#         else:
#             lists.popleft()
#             lists.append(0)
#             count += 1
#             print(lists)
#             print(truck_weights)
#
#
#     count += bridge_length
#     print(count)
#     return lists
#
# bridge_length = 2
# weight = 10
# truck_weights = [7, 4, 5, 6]
#
# print(solution(bridge_length, weight, truck_weights))