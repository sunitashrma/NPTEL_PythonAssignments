# Map function examples
#1
numbers=[2,3,4,5,6]
def square(numbers):
    return numbers*numbers

# apply square() function to each item of the numbers list

squared_numbers_iterators= map(square,numbers)

squared_numbers=list(squared_numbers_iterators)

print(squared_numbers)


#2
my_list=[2.6743,3.63526,4.2325,5.9687967,6.3265,7.6988,8.232,9.6907]

updated_list=map(round,my_list)
print(updated_list)
print(list(updated_list))

