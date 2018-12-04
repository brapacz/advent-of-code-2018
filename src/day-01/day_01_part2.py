sum = 0
frequencies = [0]
running = True
changes = []

for line in open("inputs/day-01.txt", "r"):
    changes.append(int(line))

while running:
    for change in changes:
        sum += change
        if sum in frequencies:
            print(sum)
            running = False
            break
        frequencies.append(sum)
