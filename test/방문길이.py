import collections

def solution(dirs):
    if not dirs:
        return 0
    input = collections.deque()
    for i in dirs:
        input.append(i)
    x=y=0
    record = []
    while input:
        a = input.popleft()
        if a == 'U':
            if y < 5:
                if not (x,y,'U') in record and not (x,y+1,'D') in record:
                    record.append((x,y,'U'))
                y += 1
        if a == 'D':
            if y > -5:
                if not (x,y,'D') in record and not (x,y-1,'U') in record:
                    record.append((x,y,'D'))
                y -= 1
        if a == 'L':
            if x > -5:
                if not (x,y,'L') in record and not (x-1,y,'R') in record:
                    record.append((x,y,'L'))
                x -= 1
        if a == 'R':
            if x < 5:
                if not (x,y,'R') in record and not (x+1,y,'L') in record:
                    record.append((x,y,'R'))
                x +=1
    print(record)
    print(x,y)
    return len(record)


a = 'RRRRRLLLLLUUUUUDDDDD'
print(solution(a))