year = int(input())
reminder_4 = year % 4
reminder_100 = year % 100
reminder_400 = year % 400

if reminder_4 == 0:
    first_pass = print("remider_4 pass - Leap")
    if reminder_400 == 0:
        print("The year is Leap")
    elif reminder_100 == 0:
        print(f"The year {year} is not a Leap year")
else:
    print(f"The year {year} is not a Leap year.")

