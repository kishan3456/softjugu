def binary_search(array,target):
    left=0
    right=len(array)-1
    mid=0
    while left<=right:
      mid=(left+right)//2
      if array[mid]<target:
         left=mid+1
      elif array[mid]>target:
         right=mid-1
      else:
          return mid
    return-1
array=[10,20,30,40,50]
target=40
result=binary_search(array,target)
if result!=-1:
    print("Element is present at index",str(result))
else:
    print("Element is not present in list1")




