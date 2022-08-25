
#Nested Dictionary
score = { }
score ["Test 1"] = { }
score [ "Test 2"] = { }
score ["Test 3"] = { }

score ["Test 1"] ["Dhawan"] =84
score ["Test 1" ] ["Kohli" ] = 200
score ["Test 2"]  ["Dhawan"] = 27
score ["Test 3"]  ["Dhawan"] = 78



print (score)
KEYS = score.keys ()
print (KEYS)

score ["Test 1"] ["Dhawan"] = 90
print ("New value of score is :" ,score ,'\n')

