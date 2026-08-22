# <<<<<<<<<<<<<<<< Loops in Python >>>>>>>>>>>>>>>>>

# for loop : Used when you want to repeat something for each item in a collection.
files = ["data1.csv", "data2.csv", "data3.csv"]
for file in files:
    print(f"Processing: {file}")

# while loop : Used when you want to repeat until a condition becomes False.
count = 0
while count < 3:
    print(f"Count: {count}")
    count+=1

# break : Stops the loop immediately.
for num in [1,2,3,4,5]:
    if num == 3:
        break
    print(num)  # It will print 1, 2

# continue : Skips the current iteration and moves to the next.
for num in [1,2,3,4,5]:
    if num == 3:
        continue
    print(num)

