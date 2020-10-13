# all accpeted

num = int(input())
rst = num * 2
if(sorted(str(num)) == sorted(str(rst))):
    print("Yes")
else:
    print("No")
print(rst)