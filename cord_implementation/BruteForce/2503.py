from itertools import permutations
num = list(permutations([1,2,3,4,5,6,7,8,9],3)) #모든 3자리 수를 다 뽑아놓자
n= int(input())

for _ in range(n):
    q, s, b = map(int, input().split())
    q = list(str(q))
    remove_num = 0 #num에서 제거된 튜플개수

    for i in range(len(num)):
        s_cnt = b_cnt = 0
        i -= remove_num

        for j in range(3):
            q[j] = int(q[j])
            if q[j] in num[i]:
                if j == num[i].index(q[j]):
                    s_cnt+=1
                else:
                    b_cnt+=1
        if s_cnt != s or b_cnt != b:
            num.remove(num[i])
            remove_num +=1

print(len(num))