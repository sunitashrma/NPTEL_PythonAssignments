# f strings using two variables

name = " Shweta"
age = 25

print(f"My name is {name}. I am {age} years old.")

print('%s is %d years old.' % (name, age))


# f strings for expressions

bag = 4

apples_in_bag = 6

print (f'There are total of {bag *apples_in_bag} apples.')

# f strings for dictionary

user = {}
name = {}
occupation={ }
user ['name'] = 'Sunita Sharma'
user ['occupation'] = 'Research Scholor'

print(user)

print(f"{user['name']} is a {user['occupation']}.")


