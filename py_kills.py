a = [12,230,10,220,9,100]

max_number = 0
max_drop = 0

for i in range(len(a)):
    if a[i] > max_number:
        max_number = a[i]
    elif (max_number -a[i]) > max_drop:
        max_drop = max_number - a[i]
print("Max drop is", max_drop)