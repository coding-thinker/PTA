# all accepted

mapping_set = {10:'A', 11:'B', 12:'C'}
mapping = lambda x: mapping_set[x] if x > 9 else str(x)
radix = lambda x: ''.join([mapping(i) for i in [x//13, x%13]])

RGB_dec = [int(i) for i in input().split()]
print('#%s' % ''.join([radix(i) for i in RGB_dec]))