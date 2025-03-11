import numpy as np
#1 prime clusters
def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
#I made a function to check if its prime so i dont have to do that in the loop
        
def containsPrimes(clusterArray):
    arr_with_prime = [row for row in clusterArray if any(isPrime(x) for x in row)]
    return np.array(arr_with_prime)
clusterArray = np.array([[2, 3, 5], [4, 6, 8], [11, 13, 17], [7, 10, 13]])
print(containsPrimes(clusterArray))

#2 checker board
def checkerboard():
    return np.zeros((8,8), dtype=int)
print(checkerboard())
#2.2
def checkerboardP2():
    board = np.zeros((8,8), dtype=int)
    for i in range(0,8,2):
        board[i] = [1 if j % 2 ==0 else 0 for j in range(8)]
    return board
print(checkerboardP2())
#2.3
def checkerboardP3():
    board = np.zeros((8,8), dtype=int)
    for i in range(0,8):
        if i % 2 ==0:
            board[i] = [1 if j % 2 ==0 else 0 for j in range(8)]
        else:
            board[i] = [0 if j % 2 ==0 else 1 for j in range(8)]
    return board
print(checkerboardP3())
#2.4
def reverse_checkerboard():
    board = np.zeros((8,8), dtype=int)
    for i in range(0,8):
        if i % 2 ==0:
            board[i] = [0 if j % 2 ==0 else 1 for j in range(8)]
        else:
            board[i] = [1 if j % 2 ==0 else 0 for j in range(8)]
    return board
print(reverse_checkerboard())

#3 expanding universe
def expansion(strings, numSpaces):
    expandedStrings = []
    for string in strings:
        expandedString = (' ' * numSpaces).join(string)
        expandedStrings.append(expandedString)
    return np.array(expandedStrings)
universe = np.array(['galaxy', 'clusters'])
print(expansion(universe, 1))
print(expansion(universe, 2)) 

#4 second dimmest star
def secondDimmest(stars):
    secondSmallest = []
    for col in stars.T:
        uniqueStar = np.unique(col)
        if len(uniqueStar) > 1:
            secondSmallest.append(np.partition(uniqueStar,1)[1])
        else:
            secondSmallest.append(uniqueStar[0])
    return np.array(secondSmallest)
np.random.seed(123)
stars = np.random.randint(500, 2000, (5, 5))
print(stars)
print(secondDimmest(stars))

