n = int(input(""))
ar=[]
for _ in range(n):
    ar.append(int(input()))
print("---")
target = int(input(""))
start =0
end = n-1


while(start<=end):
    if (ar[start]+ar[end]==target):
        print("{} and {}".format(start,end))
        break
    elif(ar[start]+ar[end]>target):
        end=end-1
    else:
        start=start+1
