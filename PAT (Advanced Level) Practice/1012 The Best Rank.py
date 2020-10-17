# all accepted

def enquire(ID):
    C, M, E, A = 0, 0, 0, 0
    i = 0
    flag_C, flag_M, flag_E, flag_A = False, False, False, False
    while True:
        if i < len(sorted_Average) and not flag_A:
            if ID in Average[sorted_Average[i]]:
                A += 1
                flag_A = True
            else:
                A += len(Average[sorted_Average[i]])
                
        if i < len(sorted_Clang) and not flag_C:
            if ID in Clang[sorted_Clang[i]]:
                C += 1
                flag_C = True
            else:
                C += len(Clang[sorted_Clang[i]])
                
        if i < len(sorted_Math) and not flag_M:
            if ID in Math[sorted_Math[i]]:
                M += 1
                flag_M= True
            else:
                M += len(Math[sorted_Math[i]])
            
        if i < len(sorted_Eng) and not flag_E:
            if ID in Eng[sorted_Eng[i]]:
                E += 1
                flag_E= True
            else:
                E += len(Eng[sorted_Eng[i]])
        if flag_C  and flag_M and flag_E and flag_A:
            listing = [A, C, M, E]
            minimum = min(listing)
            index = listing.index(minimum)
            if index == 0:
                return 'A', minimum
            elif index == 1:
                return 'C', minimum
            elif index == 2:
                return 'M', minimum
            elif index == 3:
                return 'E', minimum
        i += 1

def renew(ID, C, M, E, A):
    if C not in Clang:
        Clang[C] = [ID]
    else:
        Clang[C].append(ID)
        
    if M not in Math:
        Math[M] = [ID]
    else:
        Math[M].append(ID)
        
    if E not in Eng:
        Eng[E] = [ID]
    else:
        Eng[E].append(ID)
    
    if A not in Average:
        Average[A] = [ID]
    else:
        Average[A].append(ID)



n, m = (int(i) for i in input().split())
Clang, Math, Eng, Average = ({} for i in range(4))
Name = []

for _ in range(n):
    ID, C, M, E = input().split()
    ID = ID.strip()
    C, M, E = (int(i) for i in (C, M, E))
    A = sum((C, M, E)) / 3
    
    Name.append(ID)
    renew(ID, C, M, E, A)

sorted_Clang = sorted(Clang, reverse = 1)
sorted_Math = sorted(Math, reverse = 1)
sorted_Eng = sorted(Eng, reverse = 1)
sorted_Average = sorted(Average, reverse = 1)

for _ in range(m):
    ID = input().strip()
    if ID not in Name:
        print("N/A")
    else:
        course, index = enquire(ID)
        print(index, course)