number = []
for i in range(0,5,1):
    num= int(input("please enter a number"))
    number.append(num)
print("the first number is", number[0])
print("the last number is", number[4])
print("the smallest number is", min(number))
print("the largest number is", max(number))
print("the average number is", sum(number)/len(number))