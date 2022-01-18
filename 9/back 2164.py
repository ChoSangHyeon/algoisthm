from collections import deque
def get_card(num):
    queue = deque([n for n in range(1,num+1)])
    while len(queue)>1:
        queue.popleft()
        queue.append(queue.popleft())
    return queue.pop()

assert get_card(6)==4
