#A tool to calculate collision points for a kinematics assignment

print("This is a tool for making Buggy's Life calculations.")

while True:

    v = float(input("Enter the velocity of the buggy in m/s: "))
    a = float(input("Enter the acceleration of the pullback car in m/s^2: "))

    choice = int(input("Which scenario? Enter 1 or 2: "))

    if choice == 1:

        delay = float(input("Enter the time delay in seconds: "))
        displacement = (v**2 + (v*a*delay) + (v**4 + (2*(v**3)*a*delay))**0.5) / a
        print("The cars will meet at", "%.2f" % displacement, "m in front of the starting line.")

    elif choice == 2:

        sep = float(input("Enter the intial separation distance in metres: "))
        delay = float(input("Enter the time (reaction) delay in seconds: "))
        displacement = (v**2 - (a*v*delay) - ((v**4 - ((2*(v**3)*a*delay)) - ((2*(v**2)*a*sep)))**0.5)) / a
        print("The cars will meet at", displacement, "m in front of the starting line.")
        
    else:
        print("Input error.")

    again = input("Try another? y/n ")
    if again.lower() != "y":
        break
