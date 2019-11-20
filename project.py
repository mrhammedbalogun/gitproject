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

# name = input("Please enter your name:")
# age = input("Please enter your age:")
# current_age = 2019 - int(age)

# leap_year = [1804,1808,1812,1816,1820,1824,1828,1832,1836,1840,1844,1848,1852,1856,1860,1864,1868,1872,1876,1880,1884,1888,1892,1896,1904,1908,1912,1916,1920,1924,1928,1932,
# 1936,1940,1944,1948,1952,1956,1960,1964,1968,1972,1976,1980,1984,1988,1992,1996,2000,2004,2008,2012,2016]

# for i in leap_year:
#     if i == current_age:
#         print(name,",", "Youre born in a leap year")
#         break
#     else:
#         print(name,",", " Youre not born in a leap year")
#         break

# name = input("Please enter your name:")
# lenthy =  input("Please enter the lenth:")

# halfy = int(lenthy) / 2

# print(name[int(halfy):])

# print(name[0],name[1],name[4])

# print(name[-1])

# print(name[0:5])

# name = input("Please enter your name:")
# lenthy =  input("Please enter the lenth:")
# halfy = int(int(lenthy) / 2) - 1
# halfy_val = halfy + 2

# first_set = name[0:2]
# middle_set = name[halfy:halfy_val]
# last_set = name[-2:]

# answer = f"{first_set}{middle_set}{last_set}"   #We have used this method to ensure there is no space

# print(answer)

# print(first_set, middle_set, last_set)  #This will also print, but will have space
#...............reversing statement..............
# word = "sweet mum"
# slice = word[::-1]
# print(slice)

# #......reverse only the last word...... 
# word = "sweet mum"
# slice = word[-5::-1]
# print(slice)

#formular calculator

# a = input("Please enter a value:")
# b =  input("Please enter b value:")

# c = int(int(a)**2 + int(b)**2)**0.5

# print("the value of C is: ", c)

#..................almighty formular calculation.........

# a = int(input("Please enter a value:"))
# b = int(input("Please enter b value:"))
# c = int(input("Please enter c value:"))


# formular = (b**2 - (4 * a * c))**0.5
# calb = 2 * a
# answer = formular / calb

# x1 = (-b) + answer
# x2 = (-b) - answer

# print(x1, x2)

#..........comparison operators..........
# age = int(input("Please enter your age:"))
# can_drink = age >= 20
# can_pay_tax = age >= 18
# can_take_pension = age > 60
# can_retire = age == 40

# statement = f"Can drink : {can_drink}\nCan Pay Tax : {can_pay_tax}\nCan take pension : {can_take_pension}\nCan now retire : {can_retire}"

# print(statement)



#..............checking for palindrome........... ie words with the same meaning when reversed

# the_string = input("Enter the string: ")
# rev_string = the_string[::-1]

# if the_string == rev_string:
#     print(the_string,"is a palindrome")
# else:
#     print(the_string, "is not a palindrome")


# print("a" in "bola")

# print("a" not in "bola")


# a = int(input("Enter a value: "))
# b = int(input("Enter b value: "))
# c = int(input("Enter c value: "))
# d = int(input("Enter d value: "))

# divide = b * d

# working = (a * d) + (b * c) 

# print(f"{working} / {divide}")

#........Working with split.......

# fraction = input("Please enter a fraction in this format 'a/b+c/d': ")
# splitted_fraction = fraction.split("+")
# frac1 = splitted_fraction[0]
# frac2 = splitted_fraction[1]

# splitted_frac1 = frac1.split('/')
# splitted_frac2 = frac2.split('/')

# a = splitted_frac1[0]
# b = splitted_frac1[1]
# c = splitted_frac2[0]
# d = splitted_frac2[1]

# print(fraction)
# print(splitted_fraction)
# print(splitted_frac1)
# print(splitted_frac2)
# print(a,b,c,d)


# #...............Shorter process for above splitting......
# frac1, frac2 = fraction.split("+")
# a,b,c,d = *frac1.split('/'), *frac2.split('/')

# print(a,b,c,d)

#........Split class assignment........

# dob = input("Please enter date of birth in this format '1988-16-20: ")
# workings = dob.split("-")
# year_of_birth =  workings[0]

# print(year_of_birth)

# #................Built in function............
# print(1,2,3,sep="\n",end="-")
# print("new line")

#......updating a file....

# file = open ("my_data.csv","w")
# print("Name","Age","State","Due", file=file, sep=",")
# print("Ade",20,"Ogun State",20000, file=file, sep=",")

#....Getting input from users and writting to excel........
# details = input("Enter your details 'Eg first_name Age State Due: ")
# splited_details = details.split(" ")
# first_name = splited_details[0]
# age = splited_details[1]
# state = splited_details[2]
# due = splited_details[3]
# file = open ("my_data.csv","a")
# print(first_name,age,state,due, file=file, sep=",")

#.............Getting input from users and writting to excel(shorter format)......
# details = input("Enter your details 'Eg first_name Age State Due: ")
# first_name, age, state, due = details.split(" ")
# file = open ("my_data.csv","a")
# print(first_name,age,state,due, file=file, sep=",")

#.......opening a file..............
# filename = "my_music.txt"
# mode = "r"
# data = open(filename, mode)
# lyrics = data.read()
# print(lyrics)

#.....creating and writing a file.....
filename = "file.csv"
mode = "w"
file = open(filename, mode)
text = "Atha, Science, Eating"
file.write(text)