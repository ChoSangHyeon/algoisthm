import collections
def solution(progresses, speeds):
    a = []
    for i in range(len(progresses)):
        a.append([progresses[i],speeds[i]])
    zip2 = collections.deque(a)
    cnt = 0
    answer = []
    while True:
        for i in range(len(zip2)):
            zip2[i][0] = zip2[i][0] + zip2[i][1]
        for _ in range(len(zip2)):
            if zip2[0][0]>= 100:
                cnt += 1
                zip2.popleft()
        if cnt > 0:
            answer.append(cnt)
            cnt = 0
        if not zip2:
            break
    return answer

pro = [95, 90, 99, 99, 80, 99]
spd = [1, 1, 1, 1, 1, 1]
print(solution(pro,spd))



# import collections
# def solution(progresses, speeds):
#     answer = [] # 정답
#     work = collections.deque(progresses) # 큐를 사용하기 위해 사용
#     speed = collections.deque(speeds) # 큐를 사용하기 위해 사용
#     end = 0 # 끝낸 작업 수
#
#     # while 한 바퀴가 하루
#     while work:
#
#         # 일하기 남은 작업량 + speeds
#         for i in range(len(work)):
#             print(f'오늘도 열심히 {i}번 : {work[i]} {speed[i]}')
#             work[i] += speed[i]
#
#         # 맨 앞의 작업이 끝이나면 큐로 popleft() 하고 다음 작업도 끝났는지 확인
#         try:
#             while work[0] >= 100:
#                 work.popleft()
#                 speed.popleft()
#                 end += 1
#                 print(f"작업 끝 {end}")
#         except:
#             pass
#
#         # 끝난 작업 있다면 정답 리스트에 오늘 끝난 작업 수를 append 함
#         if end > 0:
#             answer.append(end)
#             end = 0
#
#     return answer