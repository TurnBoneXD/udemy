def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True #Leap year
      else:
        return False #Not leap year
    else:
      return True #Leap year
  else:
    return False #Not leap year

def days_in_month(year_input,month_input):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
    if is_leap(year_input) == True: #Leap year
        if month_input == 2:
            return "29"
    elif is_leap(year_input) == False: #Not leap year
        return month_days[month_input-1]

#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)

