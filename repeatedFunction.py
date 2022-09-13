# repeated function should return the number of values that are repeated in the input list

def repeated(list):

    count = 0
    new =[ ]
    for i in list:
         if list.count(i) > 1 and i not in new:
             new.append(i)
    return (len(new))

# Test samples

# print(repeated([1,2,4,2,5,2,6]))
# print(repeated(["the","more","you","work","hard","the","more","you","get","close","to","success"]))
             
         
