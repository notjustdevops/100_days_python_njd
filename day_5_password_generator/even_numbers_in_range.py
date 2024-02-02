target = int(input())

total_sum = 0
for number in range(0, target + 1):
    if number % 2 == 0:
        total_sum += number
print(total_sum)