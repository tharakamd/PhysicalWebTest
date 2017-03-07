n = int(input())
list = []
for x in range(1, n+1):
    i = int(input())
    list.append(i)
    if x%2 == 0: # even number
        print (list[x/2] + list[x/2-1])/2.0
    else: # odd number
        print list[x/2]