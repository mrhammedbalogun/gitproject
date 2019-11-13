# x = 20
# y = 30

# answer = x + y

# print(answer)

# num = 20
# den = 60
# pi = den / num
# print(pi)

# nameTe = "Hammed"
# print(nameTe)

# phone = 8023900964 * 2

# print(phone)

# firstName = "Hammed"
# surname = "Balogun"
# fullname = firstName + ' ' + surname

# print(fullname)
# day = "10"
# month = "06"
# year = "1988"
# print(day + ' / ' + month + ' / ' + year )
# pi = 22 / 7
# statement = "pi is " + str(round(pi,2))
# print(statement)

# akara = input("Please how many akara do you want: ")
# akamu = input("Please how many akamu do you want: ")

# akaraPrice = 20
# akamuPrice = 50

# cost1 = akaraPrice * int(akara)

# cost2 = akamuPrice * int(akamu)

# total = cost1 + cost2

# print("You bill is: ", "#",total)

# name = input("Please enter your name: ")
# age = input("Please enter your age: ")

# currentAge = 2019 - int(age)

# answer = f"Hello {name} you are {age}, you were born in {currentAge}"

# print(answer)

name = input("Please enter your name:")
age = input("Please enter your age:")
current_age = 2019 - int(age)

leap_year = [1804,1808,1812,1816,1820,1824,1828,1832,1836,1840,1844,1848,1852,1856,1860,1864,1868,1872,1876,1880,1884,1888,1892,1896,1904,1908,1912,1916,1920,1924,1928,1932,
1936,1940,1944,1948,1952,1956,1960,1964,1968,1972,1976,1980,1984,1988,1992,1996,2000,2004,2008,2012,2016]

for i in leap_year:
    if i == current_age:
        print(name,",", "Youre born in a leap year")
        break
    else:
        print(name,",", " Youre not born in a leap year")
        break