def Topper(register_number):



    oddSum, evenSum = 0, 0

    for i in range(len(register_number)):
        if int(register_number[i]) % 2 == 0:
            evenSum += int(register_number[i])
        else:
            oddSum += int(register_number[i])

    if oddSum == evenSum:
        print("true")
    else:
        print("false")
    
register_number = input()
print(Topper(register_number))