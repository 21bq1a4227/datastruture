def InsertionSort(a):
    for i in range(1,len(a)):
        key=a[i]
        j=i-1
        while j>0 and key<a[j]:
            a[j+1]=a[j]
            j-=1
        a[j+1]=key
a=[1,9,2,8,3,7]
InsertionSort(a)
lst=[]
print("sorted array is :")
for i in range(len(a)):
    lst.append(a[i])
print(lst)