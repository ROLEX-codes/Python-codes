nationality = input("Enter Nationality: ")
age = int(input("Enter age: "))
EA = ["Kenyan", "Ugandan", "Tanzanian"]

if nationality not in EA or age <= 18:

    print("Not allowed to vote")

else:
    print("You are allowed to vote")
