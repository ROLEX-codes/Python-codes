# creating grading system
mark1 = float(input("Enter mark1: "))
mark2 = float(input("Enter mark2: "))
mark3 = float(input("Enter mark3: "))
avg = (mark1 + mark2 + mark3) / 3
print("The Average is: ", avg)

if (avg >= 70 and avg <= 100):
    print("A")
elif (avg >= 60 and avg <= 69):
    print("B")
elif (avg >= 50 and avg <= 59):
    print("C")
elif (avg >= 40 and avg <= 49):
    print("D")
elif (avg >= 0 and avg <= 39):
    print("Fail")
else:
    print("Invalid marks")
