input_number = int(input("Enter positive integer:"))
total = 0

for i in range(1, input_number):
    if input_number % i == 0:
        total += i 
        
if total == input_number:
    print("Yes, " + str(input_number) + " is a perfect number")
else:
    print(str(input_number) + " is not a perfect number")
