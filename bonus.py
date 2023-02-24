sal = float(input("Enter the Salary: "))
years_of_service = int(input("Enter the Years of service: "))


if(years_of_service>10):
    bonus_in_shs = 0.1*sal
    print("The Net Bonus Amount is: ",bonus_in_shs)
elif(years_of_service>=6 and years_of_service<=10):
    bonus_in_shs = 0.08 * sal
    print("The Net Bonus Amount is: ",bonus_in_shs)
elif(years_of_service<6):
    bonus_in_shs = 0.08 * sal
    print("The Net Bonus Amount is: ",bonus_in_shs)
else:
    print("No net Bonus")