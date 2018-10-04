def  largest(arr,n):
 int arr[] of size n  
  max = arr[0] 
   current max 
    for i in range(1, n): 
       if arr[i] > max: 
        max = arr[i] 
    return max
arr = [10, 324, 45, 90, 9808] 
n = len(arr) 
Ans = largest(arr,n) 
    print ("Largest in given array is",Ans) 
