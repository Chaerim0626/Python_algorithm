apple,banana = map(int,input().split())
friend=1
for i in range(min(apple,banana)):
    if apple % friend == 0 and banana % friend ==0:
        a = apple / friend
        b = banana / friend
        print(friend,int(a),int(b))
    friend+=1
