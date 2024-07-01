n = int(input())
l = (input()).split(" ")
lr = l[::-1]
count=0
for i in l:
    if (l.count(i))%2 == 0 and count!=n:
        print (l.index(i)+1, 6-lr.index(i))
        count+=1
    elif (l.count(i))%2 != 0 and count!=n:
        print (-1)
        count+=1
