
#   Write a Python program to convert more than one list to nested dictionary.
#   Original strings:
#  ['S001', 'S002', 'S003', 'S004']
#  ['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
#  [85, 98, 89, 92]

#  Nested dictionary:
#  [{'S001': {'Adina Park': 85}}, {'S002': {'Leyton Marsh': 98}}, {'S003': {'Duncan Boyle': 89}},
#                                                               {'S004': {'Saim Richards': 92}}]



def Nested_dict (l1, l2,l3) :
    result= [{x : {y : z}} for x,y,z in zip (l1,l2,l3)]
    return(result)

student_id = [ 'S001', 'S002','S003', 'S004' ]
student_name= ["Adina Park", "Leyton Marsh", "Duncan Boyle", "Saim Richards"]
student_marks= [85,98,89,92]
print(student_id)
print(student_name)
print(student_marks)
print("\nNested_dict:")

print(Nested_dict(student_id, student_name, student_marks))

