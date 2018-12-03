import fileinput

sum = 0

for line in fileinput.input():
    sum = sum + int(line)

print(sum)
