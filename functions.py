def sum_three_numbers (x,y,z):
    return x + y + z
#print (sum_three_numbers (10,10,10))
#print (sum_three_numbers (5,5,5) + 1)
sum_one = sum_three_numbers (6,6,6)
print (sum_one)
if sum_three_numbers (2,10,2) > 9:
    print ("sum is two-digit number")

def sum_three_numbers (x,y,z):
    print (x + y + z)
#print (sum_three_numbers (10,10,10))
#print (sum_three_numbers (5,5,5) + 1)
sum_one = sum_three_numbers (6,6,6)
print (sum_one)
"""if sum_three_numbers (2,10,2) > 9:
    print ("sum is two-digit number")"""


def test_function ():
    for x in range (1,10):
        print (x)
        if x == 5:
            return x
                    
print (test_function())
