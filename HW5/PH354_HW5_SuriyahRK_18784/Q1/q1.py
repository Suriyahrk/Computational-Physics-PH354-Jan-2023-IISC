import numpy as np

# Generating array two random numbers between 1 and 6 simulating a die

# part -a 
X = np.random.randint(1, 6, size=2)
print(X)

# output
"""
[5 3]
"""

"""
Note : The output everytime will be different, so any output that will be saved cannot be reproduced by running the code again
"""
# part - b
Sum = []
limit = 1000000
for k in range(0,limit):
    Y = np.random.randint(1 ,7 , size = 2)
    Sum.append(np.sum(Y))

i = 0

for j in range(0,limit):
    if Sum[j] == 12 :
        i = i+1
    else:
        continue

print(f"The Number of time double six was obtained {i}")
print(f"The fraction of times double six was obtained {i/limit} ")
print(f"The predicted value through probabilit is {np.around(1/36, decimals = 5)}")

"""
Output:

The Number of time double six was obtained 27695
The fraction of times double six was obtained 0.027695 
The predicted value through probabilit is 0.02778
"""   


