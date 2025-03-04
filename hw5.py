#1 HW1/HW2 review
""" 1. The command 'pwd' will show my working directory.
2. 'ls' prints all files in the directory
3. 'cd ../brianna_repo' moves me to right directory and 'git pull' pulles the changes made to the assignment.
4. 'mv python_decal/brianna_repo/homework.py python_decal/judy_decal/homework/'
5. nano homework.py
6. nano homework.py
7. While still in nano, ctrl + O saves work, then you use ctrl + X to exit. the use 'git add homework.py' then 'git commit -m "adding homework.py"' and then 'git push origin main'
8. This error means that the remote repository has changes that we don't have in our local repository. we can fix this by first pulling from the remote repository using 'git pull origin main'. We might have to make some changes to files based on the edits, but then we can 'git push origin main'
9. cd ~/Recent/ """

#2 HW3 review: 2.1 data types
def checkDataType(input_type):
    return type(input_type).__name__
#2.2 conditionals
def evenOrOdd(number):
    if number%2 == 0:
        return "Even"
    else:
        return "Odd"

#3 loops
def sumWithLoop(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

#4 HW4 review: lists 4.1 Lists
def duplicateList(inputList):
    result = []
    for item in inputList:
        result.append(item)
        result.append(item)
    return result
#4.2 debugging
def square(num): #there was no colon (:) so I added it in EZ PZ
    return num*num

#5 HW2 review: Git
