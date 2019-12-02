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
# filename = "file.csv"
# mode = "w"
# file = open(filename, mode)
# text = "Atha, Science, Eating"
# file.write(text)

# myrange = range(20,60,3)

# print(myrange)

# print(type(myrange))

# print(list(myrange))

# print(list(reversed(myrange)))
# x1 = list("abimbola")
# x = [1,2,5,3,10,1,0,4]
# print(sorted(x1))
# print(sorted(x, reverse=True))
# mydict = dict(a=20,b=30)
# thenumber = [1,2,3,4,5,5,7]
# mylist = ["seed", "bee", "a", "checked","print"]
# print(sorted(mylist,key=len,reverse=True))
# print(sum(thenumber))
# print(mydict)
# print(mydict["a"])
# name = "abimbola"
# print(set(name))

# ##..............Mapping class................
# nums = [1,2,3,4,5]
# mapped = map(lambda x:x*2, nums)
# print(list(mapped))

# nums = ["ade","john","shola"]
# mapped = map(lambda x:'mr '+ x, nums) #....Adding to MR to the list
# print(list(mapped))

# word = 'the word'
# print(any(word))
# print(word.upper())


# word = input("Enter your words: ")
# word = word.lower()
# response = 'a' in word or 'e' in word or 'i' in word or 'o' in word or 'u' in word

# print(f"{word} contains vowel: {response}")

# #.............working with replace..........
# theword = input('Enter your comment: ')
# thewordl = theword.lower()
# thewordl = theword.replace('Pre','Post')
# print(theword)


# nums = ["gem","hem","blem","chem"]
# mapped = map(lambda x:x.replace('e','a'), nums) #....Adding to MR to the list
# print(list(mapped))

#............calculating for meand and mean deviation......
# thevalues = [1,3,1,2,2,4]
# answer = sum(thevalues) / len(thevalues)
# mapped = map(lambda x:x-answer, thevalues) #....Adding to MR to the list
# mapped2 = map(lambda x:(x-answer)**2, thevalues) 
# answer = sum(mapped2) / 5
# print(list(mapped))
# print(list(mapped2))
# print(answer)

#...Joining text together....
# a = ["Hello", "World"]
# answer = ' '.join(a)

# print(answer)


# filename = "my_music.txt"
# mode = "r"
# data = open(filename, mode)
# lyrics = data.read()

# answer = lyrics.find('Gongo aso')
# thecount = lyrics.count('Gongo aso')
# print(thecount)
# print(answer)

#...............Assignment one..........
# friend_1 = int(input("Friend 1: "))
# friend_2 = int(input("Friend 2: "))
# friend_3 = int(input("Friend 3: "))

# total_sum = friend_1 + friend_2 + friend_3
# to_crush = total_sum % 3
# to_take = int((total_sum - to_crush) / 3aaa)
# print(f"Each friend will take {to_take} candy and {to_crush} will be crush.")


#...........Assignment 2.......................
# import random
# dice1 = random.randint(1,7)
# dice2 = random.randint(1,7)

# if (dice1 == 6) &  (dice2 == 6):
#     print("Yes! You won")
# else:
#     print("Awww! Try again")
#.................................
# behaviour = "bad"
# age = 80

# if (behaviour == "good") & (age < 18):
#     print("You get a toy")
    
# elif (behaviour == "good") & (age > 18):
#     print("You get a car")
    
# else:
#     print("Left alone")

#.........tenery operator.............
# result = 49
# response = "pass" if result > 50 else "fail"

# print(response)



# if question_time == "false":
#     response1 = input("do you have pains")
# elif response1 == "true":
#     response2 = input("did you sleep well")
# elif response2 == "true":
#     response3 = input("have you done road work")
# elif response3 == "false":
#     response4 = input("do you have fever")
# elif response4 == "true":
#     response5 = input("are you vomitting")
# elif response5 == "true":
#     print("Please see a doctor")



#.................if statement........
# question_time = input("Are you okay")
# if question_time == "false":
#     response1 = input("do you have pains")
#     #else question_time == "true":
#         #print("PLease get a life")
#     if response1 == "true":
#         response2 = input("did you sleep well")
#     #if response1 == "false":
#         #print("Unable to diagnos now")
#         if response2 == "true":
#             response3 = input("have you done road work")
                
#             if response3 == "false":
#                 response4 = input("do you have a fever")

#                 if response4 == "true":
#                     response5 = input("are you vomiting")

#                     if response5 == "true":
#                             print("Please see a doctor")
#                     else:
#                         print("bill")
#                 else:
#                     print("Take some anti maleria")
#             else:
#                 print("have some pain relief")
#         else:
#             print("try to sleep well")
#         #if response2 == "false":
#     else:           
#         print("Unable to diagnose")

#.............for loop........

# a = ["car", "men", "boys"]

# for i in a:
#     print(i)

# for i in range(20):
#     print(i)


# print("x".center(4),"|", "x_xbar".center(7),"|", "x_xbar2".center(7), sep="")
# print("____".center(4),"|", "_______".center(7),"|", "_______".center(7),sep="")

# mean = sum(range(10)) / len(range(10))

# for i in range(10):
#     xbar = i - mean
#     xbar2 = xbar ** 2
#     print(f"{i}".center(4), "|", f"{xbar}".center(7), "|", f"{xbar2}".center(7), sep="")

#....class assignment.....
# names = ["John", "Clem"]

# for i in names:
#     print("Hello ", i)


# your_word = input("Enter your word here: ")
# word = ['a','e','i','o','u']
# for i in your_word:
#     if i in word:
#         print(i)

# word = input("Enter your word: ")
# vowels = ['a','e','i','o','u']
# total_vowels = 0


# print(f"Vowels | Count")
# print(f"_______|_______")
# for i in vowels:
#     if i in word:
#         #print(i)
#         count = word.count(i)
#         total_vowels = total_vowels + count
#         print(f"{i.center(6)} | {str(count).center(6)}")
# print(f"Total vowels: {total_vowels}")

#..............working with continue............
# scores = [20,30,70,10,67,50]
# import random
# for score in scores:

#     c_assess = random.randint(10,30)
#     f_score = score + c_assess

#     marked_up = int(f_score * 1.2)
#     if f_score > 70:
#         print(score, c_assess, f_score, f_score)
#         continue

#     print(score, c_assess, f_score, marked_up, "marked")

#.........Dice Games Assignment...........#

# def roll_dice():

#     i = 0
#     while i < 6:

#         input("PRESS ENTER TO ROLL DICE")

#         import random
#         dice1 = random.randint(1,6)
#         dice2 = random.randint(1,6)

#         dice = [dice1, dice2]

#         if dice[0] == 6 and dice[1] == 6:
#             print("WOW! YOU ROLLED:", dice1, dice2, ". !!!! YOU WON !!!")
#             break
#         i += 1
#         print("What you currently ROLLED:",dice1,dice2)
        
    
#     else:
#         print("You have exhausted your 6 attempt")
            
# roll_dice()


#...............My amortization calculation.............
#monthly interest
annual_rate = float(input("Enter annual interest rate")) / 100
monthly_rate = ((1 + annual_rate) ** (1/12)) - 1
print(monthly_rate)

#Monthly pay
repayment_period = int(input("How many years of repayment period")) * 12
loan_amount = int(input("Enter the loan amount"))
monthly_pay = round((loan_amount * monthly_rate) / (1 - ((1 + monthly_rate) ** -repayment_period)),2)
print(monthly_pay)

print("Month".center(5),"|", "Payment Required".center(16),"|", "Principal Paid".center(15), "|", "Interest Payment".center(16), "|", "Balance".center(7), sep="")
principal_paid = 0
current_loan = loan_amount - principal_paid
i = 0
while i <= repayment_period:
    monthly_interest = round(current_loan * monthly_rate,2)
    principal_paid = round(monthly_pay - monthly_interest,2)
    remaining_balance = round(current_loan - principal_paid,2)
    current_loan = remaining_balance

    i += 1
    print(f"{i}".center(5), "|", f"{monthly_pay}".center(16), "|", f"{principal_paid}".center(15), "|", f"{monthly_interest}".center(16), "|", f"{remaining_balance}".center(7), sep="")