num = int(input("How many numbers do you want to input?:"))
max_value = 0
total = 0
for i in range(num):
    number = int(input("Input a number :"))
    total += number
    if max < number:
        max = number
    

print(f"total : {total}")  
print(f"average : {total/num}")  
print(f"max : {max}")
