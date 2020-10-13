# all accepted

num, base = [int(i) for i in input().split()]
stack = []

if 1:
    while num:
        stack.append(str(num % base))
        num //= base

    r = stack[:]
    r.reverse()
    if r == stack:
        print('Yes')
    else:
        print('No')
    print(' '.join(r))
        
