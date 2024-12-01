## Part 1
with open("input.txt", "r") as file:

    left = []
    right = []

    for line in file:
        left_right = line.split()
        left.append(int(left_right[0]))
        right.append(int(left_right[1]))

left.sort()
right.sort()

total_distance = 0
for i in range(len(left)):
    distance = abs(left[i] - right[i])
    total_distance += distance

print(total_distance)



## Part 2
similarity_score = 0
for i in range(len(left)):
    count = 0
    for j in range(len(right)):
        if left[i] == right[j]:
            count += 1
    similarity_score += left[i] * count

print(similarity_score)




