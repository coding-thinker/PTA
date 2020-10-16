# all accepted


import math

def work():
    maps = {j:i for i, j in {i:str(i) if i <10 else chr(i+87)for i in range(36)}.items()}
    mapping = lambda x: maps[x]

    src, dst, tag, radix = input().split()
    radix = int(radix)
    if tag == '2':
        dst, src = src, dst

    src = list(map(mapping, src[::-1]))
    dst = list(map(mapping, dst[::-1]))
    start = max(1, max(dst))
    src = sum([src[i]*radix**i for i in range(len(src))])


    rst = start + 1
    jump_list = []
    try:
        temp = 10**int(math.log(src, 10))
        while int(temp // 10) > 1:
            jump_list.append(temp // 10)
            temp /= 10
        jump_list.append(1)
    except:
        jump_list = [10, 1]

    exit_flag = False
    for index, radix in enumerate(jump_list):
        while True:
            temp = sum(int(dst[i])*int(rst)**int(i) for i in range(len(dst)))

            if src == temp == 0:
                return 1

            if index % 2 == 0:
                if temp == src:
                    exit_flag = True
                    break
                if temp > src:
                    if radix == 1:
                        exit_flag = True
                        rst =  'Impossible'
                    break
                rst += radix
            elif index % 2 == 1:
                if temp == src:
                    exit_flag = True
                    break
                if temp < src:
                    if radix == 1:
                        exit_flag = True
                        rst =  'Impossible'
                    break
                rst -= radix
        if exit_flag:
            break
    if type(rst) == int:
        if rst > 2:
            while rst - 1 > 2:
                if src == sum([dst[i]*(rst-1)**i for i in range(len(dst))]) and src > start:
                    rst -= 1
                else:
                    break
    if type(rst) != str:
        rst = '%.0f' % rst
    return rst


print(work())