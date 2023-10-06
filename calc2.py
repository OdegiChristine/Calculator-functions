# Name : ODEGI CHRISTINE
# Reg no : SCT211-0093/2022

name = input("Enter name: ")
print(f"Hello, {name}")

year_of_birth = int(input("Enter year of birth: "))
current_year = 2023

def age_in_years(yob: int):
    age_years = current_year - yob
    print(f"Age in years = {age_years}")
    return age_years

years = age_in_years(year_of_birth)

def age_in_months(yrs: int):
    age = yrs * 12
    print(f"Age in months = {age}")
    return age

months = age_in_months(years)

def age_in_days(num : int):
    days = num * 365
    print(f"Age in days: {days}")
    return days

age_days = age_in_days(years)
