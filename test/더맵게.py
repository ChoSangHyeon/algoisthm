import heapq
def solution(scoville, K):
    heap = []
    cnt = 0
    for i in scoville:
        heapq.heappush(heap,i)
    while heap[0] < K:
        if len(heap) == 1:
            cnt = -1
            break
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        heapq.heappush(heap,a+b*2)
        cnt += 1
    return cnt


#  최소값이나 최대값을 지지고 볶으면서 결과값을 만들때에는 힙을써서 최적화를 한다.
#  이번 문제같은경우는 최소값이 K를 넘기면 실행횟수를 반환하는 문제였는데
#  처음에 내가 풀었던 리스트에 빼고 넣고는 정렬하고는 시간이 너무 많이걸리니
#  힙을 사용해서 최소값을 빨리뽑게해줘야한다.