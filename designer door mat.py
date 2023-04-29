n, m = input().split
n = int(n)
m = int(m)
# create top half of the mat
for i in range(n//2):
    pattern = ".|." * (2*i+1)
    print(pattern.center(m, "-"))

# create center of the mat
print("WELCOME".center(m, "-"))

# create bottom half of the mat
for i in range(n//2-1, -1, -1):
    pattern = ".|." * (2*i+1)
    print(pattern.center(m, "-"))
