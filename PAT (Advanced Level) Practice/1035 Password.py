# all accepted

account_num = int(input())
modify_flag = 0
mapping = {'1':'@',
           '0':'%',
           'l':'L',
           'O':'o',
           }

def check(pwd:str):
    pwd = list(pwd)
    sample = []
    flag = False
    global modify_flag
    for i in range(len(pwd)):
        if pwd[i] in mapping:
            if not flag:
                flag = True
            pwd[i] = mapping[pwd[i]]
    if flag:
        modify_flag += 1
        return ''.join(pwd)
    else:
        return False
        
output = []
for _ in range(account_num):
    team_name, team_pwd = input().split()
    team_pwd = check(team_pwd)
    if team_pwd:
        output.append((team_name, team_pwd))

if not modify_flag:
    if account_num > 1:
        print('There are %d accounts and no account is modified' % account_num)
    else:
        print('There is %d account and no account is modified' % account_num)
else:
    print(modify_flag)
    for each in output:
        print(" ".join(each))