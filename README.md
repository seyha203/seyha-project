# Exercise Python


## Exercise1

* Reverse string below
```python
text = "Hello Baby"

reverseText = ""
for index in range(1,len(text)+1):
    reverseText += text[-index]

print(reverseText)
```

## Exercise2

* Siple Reverse string

```python
text = "Hello Baby"

lastIndex = len(text) -1 
reverseIndex = ""

for index in range(len(text)):
    reverseText += text[lastIndex - index]

print(reverseText)
```

## Exercise3
* Index of Odd number

```python
arr = [5,7,8,4,3]
indexOfOdd = []

for i in range(len(arr)):
    if arr[i] % 2 == 1:
        indexOfOdd.append(i)
print(indexOfOdd)
```

## Exercise4

* Average of number

```python
arr = [5,7,8,4,3]
average = 0
sum = 0

for value in arr:
    sum += value
average = sum / len(arr)

print(average)
```

## Exercise5

* Simple Array Dictionary

```python
arr = [
    {'neme': 'bopha', 'age': 18}
    {'neme': 'thida', 'age': 12}
    {'name': 'kanha', 'age': 16}
]

for dics in arr:
    print(dics['name'])
```

## Exercise6

* Sum number

```python
arr = [5,7,8,4,3]
sum = 0
for value in arr:
    sum += value 
print(sum)
```


## Exercise6

* Even number

```python
arr = [5,7,8,4,3]

for value in arr:
    if value % 2 == 0:
        print(value)
```


## Exercise7

* Minimum number

```python
arr = [10,40,20,4,3]

min = arr[0]
for value in arr:
    if value < min:
        min = value
print(min)

```


## Exercise8

* Move one step to right

```python
arr = [0,0,1,0,0]
isFound = False
for i in range(len(arr) -1):
    if arr[i] == 1 and not isFound:
        arr[i] 0
        arr[i+1] = 1
        isFound = True
print(arr)
```

## Exercise9

* Move one step to left

```python
arr = [0,0,1,0,0]

isFound = False
for i in range(len(arr) -1):
    if arr[i] == 1 and not isFound:
        arr[i] = 0
        arr[i - 1] = 1
        isFound = True
print(arr)
```