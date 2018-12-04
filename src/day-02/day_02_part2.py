def count_differences(word_a, word_b):
  differences = 0
  for i in range(0, len(word_a)):
    if word_a[i] != word_b[i]:
      differences += 1
  return differences

def common_characters(word_a, word_b):
  commons = ''
  for i in range(0, len(word_a)):
    if word_a[i] == word_b[i]:
      commons += word_a[i]
  return commons

def solve(codes):
  for i in range(0, len(codes)-2):
    for j in range(i+1, len(codes)-1):
      if count_differences(codes[i], codes[j]) == 1:
        return common_characters(codes[i], codes[j])


codes = []

for line in open("inputs/day-02.txt", "r"):
  codes.append(line.rstrip())

print(solve(codes))
