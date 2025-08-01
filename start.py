# arr = [5,7,8,4,3]
# sum = 0
# for value in arr:
#     sum += value 
# print(sum)

# arr = [10,40,20,4,3]

# min = arr[0]
# for value in arr:
#     if value < min:
#         min = value
# print(min)

arr = [0,0,1,0,0]
isFound = False
for i in range(len(arr) -1):
    if arr[i] == 1 and not isFound:
        arr[i] 0
        arr[i + 1] = 1
        isFound = True
print(arr)