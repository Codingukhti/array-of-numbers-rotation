def Rotate(arr, d, n):
  p = 1
  while(p <= d):
    last = arr[0]
    for i in range (n - 1):
      arr[i] = arr[i + 1]
    arr[n - 1] = last
    p = p + 1
     
# Function to print an array
def printArray(arr, size):
  for i in range (size):
    print(arr[i] ,end = " ")
     
# Driver code
arr = [1, 3, 2, 7, 4, 6]
N = len(arr)
d = 3
 
# Function calling
Rotate(arr, d, N)
printArray(arr, N)
 