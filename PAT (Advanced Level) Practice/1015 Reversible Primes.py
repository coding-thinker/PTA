# all accepted

def radixing(num, from_radix, to_radix):
    if from_radix == to_radix:
        return int(str(num)[::-1])
    
    result = ''
    while num:
        result += str(num % to_radix)
        num = num // to_radix


    for i,each in enumerate(result[::-1]):
        num += int(each) * to_radix ** i

    return num

def is_prime(num):
    if num < 2:
        return False
    if num < 4:
        return True
    for i in range(2, int(num ** 0.5) + 1):
        if not num % i:
            return False
    return True


while(1):
    try:
        num, radix = [int(i) for i in input().split()]
        if(is_prime(num)):
            if(is_prime(radixing(num, 10, radix))):
                print('Yes')
                continue
        print('No')
    except:
        break