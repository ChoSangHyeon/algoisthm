import collections


def solution(numbers, target):
    if sum(numbers) < target:
        return 0
    tag = collections.deque(numbers)
    stack = collections.deque()
    while tag:
        a = tag.popleft()
        if stack:
            abc = stack.copy()
        else:
            stack.append(a)
            stack.append(-a)
            continue
        while abc:
            b = abc.popleft()
            stack.popleft()
            if (b + a + sum(tag)) >= target:
                stack.append(b + a)
            if (b - a + sum(tag)) >= target:
                stack.append(b - a)

    answer = stack.count(target)
    return answer


a = [1, 1, 1, 1, 1]

print(solution(a, 3))
