year = int(input("Enter the year: "))
modulus = year%4

if modulus == 0:
    print(f"{year} is a leap year")

else:
    print(f"{year} is an odd year")