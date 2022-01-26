a,b = map(int,input().split())

if b-45 < 0:
    if a==0:
        print(f'{a+23} {b+15}')
    else:
        print(f'{a-1} {b+15}')
else:
    print(f'{a} {b-45}')