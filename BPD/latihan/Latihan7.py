start = 1

for i in range(start, 101):
    if i % 10 == 0:
        print(i)
    else:
        print(i, end=" ")
print("\n")
total_lines = 10

# Outer loop for each line
for i in range(total_lines, 0, -1):
    for j in range(9, 9-i, -1):
        print(j, end=" ")
    print()
