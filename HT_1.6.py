arr = input("Please write group of numbers: ").split(",")
arr = list(map(int, arr))
number_check = int(input("Please write number for check: "))
if number_check in arr:
    print ("True")
else:
    print("False")
print(arr)
print(number_check)