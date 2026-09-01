marks = [80, 90, 70, 85, 95]
print(marks)

print(len(marks))

print(marks[0])
print(marks[1])
print(marks[2])

print(marks[-1])

print(marks[0:3])

total = 0
for mark in marks:
    print(mark)
    total = total + mark

print("total:")
print(total)

avg = total / len(marks)
print("average:")
print(avg)

print("min:")
print(min(marks))
print("max:")
print(max(marks))