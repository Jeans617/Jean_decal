#2.1 making a list variable
ListTo20 = list(range(21))
# I forgot the range() function was exclusive of the upper bound so i changed the range(20) to range(21)
print(ListTo20)

#2.2 square list
def squareList(numbers):
 return [num ** 2 for num in numbers]
SquareTo20 = squareList(ListTo20)
print(SquareTo20)

#2.3 slicing
def first_fifteen_elements(numbers):
 return numbers[:15]
#I originally got the stop and start elements of the slicing mixed up, so I just fixed 15: to :15 EZPZ
print(first_fifteen_elements(SquareTo20))

#2.4 Striding 
def every_fifth_element(numbers):
 return numbers[4::5]
#I wasnt sure if I was using the striding correctly because I used [::5] and kept returning [0, 25, 100, 225, 400] but i relaized that this started from the 0th entry then added 5 for the next entry, so I changed it to [4::5] and got the expexcted result
print(every_fifth_element(SquareTo20))

#2.5 slicing & striding
def fancy_function(numbers):
 return numbers[:-3][::-3]
#I'm actually really confused by the prompt because the expected result doesnt slice off the last 3 elements from the list, just puts every 3rd element in reverse order so I'm unsure if my answer is correct but this is how I interpretted it
print(fancy_function(SquareTo20))

#3.1 5X5 2d list
def create_2d_list():
 result = []
 count = 1
 for i in range(5):
  row = []
  for j in range(5):
   row.append(count)
   count += 1
  result.append(row)
  #I had this line nested in the 2nd for loop so i got 5 copies of each list, so I just made sure it was in the 1st for loop to fix it
 return result
matrix = create_2d_list()
print(matrix)

#3.2 replace 2d list
def modified_2d_list(matrix):
 new_matrix = [row[:] for row in matrix]
 for i in range(len(new_matrix)):  
        for j in range(len(new_matrix[i])):  
            if new_matrix[i][j] % 3 == 0:  
                new_matrix[i][j] = "?" 
 return new_matrix 
print(modified_2d_list(matrix))

#3.3 summing none-'?' elements
def sum_non_question_elements(numbers):
 total = 0 
 for row in numbers: 
     for value in row:  
         if value != "?":  
                total += value  
 return total  # Return the final sum
new_matrix = modified_2d_list(matrix)
print(sum_non_question_elements(new_matrix))