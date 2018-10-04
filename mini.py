in arr[] of size n
def largest(arr,n):
    min = arr
     current min 
    for i in range(1, n): 
        if arr[i] > min: 
            min = arr[i] 
    return min
arr = [10, 324, 45, 90, 9808] 
n = len(arr) 
Ans = largest(arr,n) 
print ("Largest in given array is",Ans) 
