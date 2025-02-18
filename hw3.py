# Q1:do powers
def computePower(x,y):
    ans = 1
    for _ in range(y):
        ans *= x
    return ans
x = 2
y = 3 
print(computePower(x,y))

# Q2: temp range
def temperatureRange(readings):
    return (min(readings), max(readings))
readings = [15, 14, 17, 20, 23, 28, 20]
print(temperatureRange(readings))

# Q3: weekend
def isWeekend(day):
    return day == 6 or day == 7
print(isWeekend(5))
print(isWeekend(6))

# Q4: fuel efficiency
def fuel_efficiency(distance, fuel):
     FE = (distance/fuel)
     return FE
distance = 70
fuel = 21.5
print(fuel_efficiency(distance, fuel))

# Q5: decode
def decodeNumbers(n):
    if n < 10:
        return n
    lastDig = n % 10
    remNum = n // 10
    numDig= 1
    temp = remNum
    while temp > 0:
        temp //= 10
        numDig *= 10
    return lastDig * numDig + remNum
n = 12345
print(decodeNumbers(n))

# Q6.1:  for loops
def find_min_with_for_loop(nums):
    minVal = nums[0]  
    for num in nums:
        if num < minVal:
            minVal = num
    return minVal

def find_max_with_for_loops(nums):
    maxVal = nums[0]  
    for num in nums:
        if num > maxVal:
            maxVal = num
    return maxVal
nums = [2024, 98, 131, 2, 3, 72]
print(find_min_with_for_loop(nums))  
print(find_max_with_for_loops(nums)) 

# Q6.2: while loops
def find_min_with_while_loop(nums):
    i = 1
    minVal = nums[0]  
    while i < len(nums):
        if nums[i] < minVal:
            minVal = nums[i]
        i += 1
    return minVal

def find_max_with_while_loop(nums):
    maxVal = nums[0]  
    i = 1  
    while i < len(nums):
        if nums[i] > maxVal:
            maxVal = nums[i]
        i += 1
    return maxVal


nums = [2024, 98, 131, 2, 3, 72]
print(find_min_with_while_loop(nums))  
print(find_max_with_while_loop(nums)) 

# Q7: counting vowels
def vowel_and_consonant_count(text):
    vowels = "aeiouAEIOU"  
    vowelCount = 0
    consonantCount = 0

    for char in text:
        if char.isalpha():  
            if char in vowels:
                vowelCount += 1  
            else:
                consonantCount += 1 

    return (vowelCount, consonantCount)

text = "UC Berkeley, founded in 1868!"
print(vowel_and_consonant_count(text))  

# Q8: digital root
def digital_root(num): 
    rootSum = 0
    while num > 9:
        rootSum += (num % 10)
        num //= 10
    rootSum += num
    return rootSum
num = 2468
print(digital_root(num))
