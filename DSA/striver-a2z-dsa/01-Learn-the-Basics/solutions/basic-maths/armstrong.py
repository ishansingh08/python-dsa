n = int(input())

original = n
count = 0
sum = 0

# Count digits
temp = n
while temp > 0:
    temp = temp // 10
    count += 1

# Calculate Armstrong sum
temp = n
while temp > 0:
    digit = temp % 10
    sum = sum + digit ** count
    temp = temp // 10

if sum == original:
    print("Armstrong")
else:
    print("Not Armstrong")
