scores = list(map(float, input("Enter scores separated by spaces: ").split()))

total = sum(scores)
average = total / len(scores)

print("Sum of scores:", total)
print("Average of scores:", average)
maximum = max(scores)
minimum = min(scores)

print("Sum of scores:", total)
print("Average of scores:", average)
print("Maximum score:", maximum)
print("Minimum score:", minimum)