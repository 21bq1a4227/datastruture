def linearsearch(l,n,key):
    for i in range(0,n):
        if(l[i]==key):
            return i
    return -1
n=int(input("enter the size:"))
l=[]
for i in range(n):
    ele=int(input("enter the elements:"))
    l.append(ele)
key=int(input("enter key element:"))
result=linearsearch(l,n,key)
if result==-1:
    print("element not found")
else:
    print("element found at index:",result)