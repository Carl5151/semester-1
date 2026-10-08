# Week 1.2, Session 2: Task 6
temp = int(input("Enter the machines temperature in degrees Celcius: "))
pressure = int(input("Enter the machine's pressure in PSI: "))
status = int(input("Enter the machine's operational status (1 for operating, 0 for stopped): "))

if temp > 80:
    print("The machine's temperature is too high. Recommend to shut down the machines.")
elif temp >= 50:
    print("The machine's temperature is within the safe limits.")
else:
    print("The machine's temperature is low and no action is needed.")

if pressure > 100:
    print("The machine's pressure is too high. Recommend for maintenance.")
elif pressure >= 70:
    print("The machine's pressure is stable.")
else:
    print("The machine's pressure is low. The system is operating normally")

if status == 1:
    if temp > 80 or pressure > 100:
        print("The machine is running in unsafe conditions. Recommend to shut it down.")
    else:
        print("The machine is running normally")
else:
    print("The machine has stopped. No immediate action is needed.")
    