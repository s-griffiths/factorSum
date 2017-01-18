# FactorSum.py
# This program returns the percentages of perfect, abundant, and deficient numbers between 2 and a user supplied number.

# states what the program's purpose is to the user
print("Find the percentages of perfect, abundant, and deficient numbers")
print("between 2 and your number.")

# variable to hold user entered number
N = int(input("\nEnter a positive whole number: "))

# requests that N is a positive whole number if the original N was not
while N <= 0:
    N = int(input("Must be a POSITIVE WHOLE number: "))

# variables to hold total, perfect, abundant, and deficient number counts
totalCount = 0
perfectTotal = 0
abundantTotal = 0
deficientTotal = 0

# steps through each number from 2 to user-entered number
for i in range(2, N + 1):

    # variable to hold the sum of the factors of the current number
    currentSum = 0

    # steps through the current number's factors and adds them to the currentSum
    for j in range(1, i):
        if i % j == 0:
            currentSum += j
            
    # uncomment this print statement to troubleshoot
    #print(i, ",", currentSum)
    
    # increments totalCount by 1 for each number factored
    totalCount += 1

    # counts the numbers according to their factors' sums
    if currentSum == i:
        perfectTotal += 1
    elif currentSum < i:
        deficientTotal += 1
    else:
        abundantTotal += 1

# uncomment these three print statements to troubleshoot
# print("Perfect =", perfectTotal)
# print("Abundant =", abundantTotal)
# print("Deficient =", deficientTotal)

# Converts perfect, abundant, and deficient number counts to percentages
perfectTotal = (perfectTotal / totalCount) * 100
abundantTotal = (abundantTotal / totalCount) * 100
deficientTotal = (deficientTotal/ totalCount) * 100

# Prints the percentages of the three number types
print("\nPerfect numbers make up {:.4f}%".format(perfectTotal), "of the numbers between 2 and", str(N) + ".")
print("Abundant numbers make up {:.4f}%".format(abundantTotal), "of the numbers between 2 and", str(N) + ".")
print("Deficient numbers make up {:.4f}%".format(deficientTotal), "of the numbers between 2 and", str(N) + ".") 

