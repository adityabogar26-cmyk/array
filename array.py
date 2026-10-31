scores = list(map(float, input("Enter scores separated by spaces: ").split()))

total = sum(scores)
average = total / len(scores)

print("Sum of scores:", total)
print("Average of scores:", average)