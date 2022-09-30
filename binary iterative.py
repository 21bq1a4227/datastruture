def binarySearch(l,low,high,key):
    while low<=high:
        mid=(low+high)//2
        if l[mid]==key:
            return mid
        elif l[mid]>key:
            high=mid-1
        else:
            low=mid+1
    return-1
l=[1,2,3,7,8,9]
low=0
high=len(l)-1
key=int(input("enter any key elements:"))
result=binarySearch(l,low,high,key)
if result==1:
    print("element not found")
else:
    print("element found at index :",result)
    