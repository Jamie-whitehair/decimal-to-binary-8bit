loop0 = True
while loop0 is True:
    dec = int(input("Type the number you want to convert to Binary: \n"))
    if dec > 255:
        print("Value cannot exceed 255.")
    else:
        loop0 = False
# loop0 is for numbers input
# loop1 is for the binary loop

loop1 = True
while loop1 is True:
    if dec == 0:
        loop1 = False
    else: 
        dec1 = dec // 2
        dec3 = dec % 2
        dec = dec1
        print(dec3)
        # simple loop to solve problem

input()
