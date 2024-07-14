def stringConstruction(string):
    unique_characters = set(string)  
    return len(unique_characters)

import sys

input = sys.stdin.read
data = input().splitlines()

num_cases = int(data[0])
results = []  
for i in range(1, num_cases + 1):
    string = data[i]
    result = stringConstruction(string)
    results.append(result)

for result in results:
    print(result)
