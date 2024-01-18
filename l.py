
arr = []
n = int(input("Enter length of array: "))     
# n = len(arr)
 
for i in range(n):
    x = int(input("Enter number: "))
    arr.append(x)  
 
print(arr)

max = arr[0]
for i in range(1, n):
    if arr[i] > max:
        max = arr[i]

print("Largest in given array ", max)
