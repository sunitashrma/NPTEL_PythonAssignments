# A list is a palindrome if it reads the same forwards and backwards

def mypalindrome (list):
    if list==[] or len(list)==1:
        return (True)
    else:
        return (list[::-1] == list)

# Test samples
# print(mypalindrome([12,22,12]))
# print(mypalindrome([10,9,8,6,5]))
