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

# def roll_segun():

#     i = 0
#     while i < 5:

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
#         print("You have exhausted your 5 attempt")
            
# roll_segun()


#...............My amortization calculation.............
#monthly interest
# annual_rate = float(input("Enter annual interest rate")) / 100
# monthly_rate = ((1 + annual_rate) ** (1/12)) - 1
# print(monthly_rate)

# #Monthly pay
# repayment_period = int(input("How many years of repayment period")) * 12
# loan_amount = int(input("Enter the loan amount"))
# monthly_pay = round((loan_amount * monthly_rate) / (1 - ((1 + monthly_rate) ** -repayment_period)),2)
# print(monthly_pay)

# print("Month".center(5),"|", "Payment Required".center(16),"|", "Principal Paid".center(15), "|", "Interest Payment".center(16), "|", "Balance".center(7), sep="")
# principal_paid = 0
# current_loan = loan_amount - principal_paid
# i = 0
# while i <= repayment_period:
#     monthly_interest = round(current_loan * monthly_rate,2)
#     principal_paid = round(monthly_pay - monthly_interest,2)
#     remaining_balance = round(current_loan - principal_paid,2)
#     current_loan = remaining_balance

#     i += 1
#     print(f"{i}".center(5), "|", f"{monthly_pay}".center(16), "|", f"{principal_paid}".center(15), "|", f"{monthly_interest}".center(16), "|", f"{remaining_balance}".center(7), sep="")

#    

# name = ["hammed", "yusuf", "Ade"]

# picked = random.choice(name)

# print(picked)

# n = 5

# for i in range(n):
#     i = i-1
#     print(i)
    
# while n > 0:
#     n -= 1
#     print(n)

# x = "boy Toys Junk"
# y = "Mum Girl Luch"

# n = 0
# word_lenght = len(x)

# while n < word_lenght:
#     print(x[n], y[n])

#     n += 1

#.................Multiplication Table Assignment.......................

# start_value = int(input("Start Multiplying from What Number ? :"))
# end_value = int(input("End Multiplying from What Number ? :"))
# mult_lenth = int(input("Enter Multiplication Table Length. Between 1 and 12 ? :"))
# for i in range(start_value,(end_value + 1)):
#     print("=====================================")
#     print("Multiplication Table for ", i, "Time(s)")
#     print("=====================================")
#     for j in range(1,(mult_lenth + 1)):
#         result= j * i
#         print(f"{i}".center(4), " X ", f"{j}".center(4), " = ", f"{result}".center(5), '|' sep="")


#.................Multiplication Table Assignment Format || .......................

# start_value = int(input("Start Multiplying from What Number ? :"))
# end_value = int(input("End Multiplying from What Number ? :"))
# mult_lenth = int(input("Enter Multiplication Table Length. Between 1 and 12 ? :"))
# for i in range(start_value,(end_value + 1)):
#     for j in range(1,(mult_lenth + 1)):
#         result= j * i
#         print(f"{i}".center(3), " X ", f"{j}".center(3), " = ", f"{result}".center(5), end = "")
#     print("\n")    

#.........Woorking with List...........

# mylist = [1,2,3,4,5]
# print(mylist)

# name = "Hammed"
# new_name = list(name)
# print(new_name)

#....append....
# prducts = "shes,bags,pencil"
# new_product = prducts.split(",")
# print(new_product)

# new_product.append("Beans")

# print(new_product)

# tried = 2
# while True:

#     action = input("What do you want to do: ")

#     if action == "add":
#         new_prop = input("Enter a new prop : ")
#         new_product.append(new_prop)
#         print(new_product)

#     elif action == "rem":
#         new_prop = input("Enter a new prop : ")
#         new_product.remove(new_prop)
#         print(new_product)

#     tried -= 1

#     if tried == 0:
#         print("You have exhausted attempt........!!")
#         break

#.....................Class work.....................
# goods =  "yam,beans,bread"
# new_goods = goods.split(",")

# while True:
#     already_counted = []

#     for item in new_goods:
#         if item not in already_counted:
#             occurences = new_goods.count(item)
#             already_counted.append(item)
#             print(item, occurences)

#     action = input("What do you want to do: ")
    
#     if action == "add":
#         new_prop = input("Add new words : ")
#         new_goods.append(new_prop)
#         #print(new_goods, count)

#     elif action == "rem":
#         new_prop = input("Remove old words : ")
#         new_goods.remove(new_prop)
#         #print(new_goods, count)

#............class on pop, extend and extend.....
# x = [1,2,3,4,5]

# x.extend([1,2,3,4])

# x.insert(1,50)

# x.pop(2)

# q = [1,2,3,4,5,6]

# squared = [x**2 for x in q]

# x.index(2)
# print(squared)



# import this 



# for a in range(1000):
#     for i in range(20):
#         thenumber = random.randint(1,7)
#         the_numbers.append(thenumber)
            
#     already_counted = []

#     for item in the_numbers:
#         if item not in already_counted:
#             occurences = the_numbers.count(item)
#             already_counted.append(item)
#             print(item, occurences)

# new_occurences = []
#for a in range(5):

#..............ASSIGNMENT ON RANDOM ROLLING.....................
# import random
# for b in range(5): 
#     print("")
#     print("TRIAL ",b)
#     the_numbers =  []

#     for i in range(1000):
#         thenumber = random.randint(1,7)
#         the_numbers.append(thenumber)
        
                    
#     already_counted = []
#     total_occurrence = []
#     items_list = []
#     percentage = []


#     for item in the_numbers:

#         if item not in already_counted:
            
#             occurences = the_numbers.count(item)
#             already_counted.append(item)
#             total_occurrence.append(occurences)
#             items_list.append(occurences) 

#             sum_occurence = sum(total_occurrence)
                
#             for a in items_list:
#                 result = (a / 1000) * 100

#             percentage.append(result)


                
            
#             print(f"{item} {occurences} {round(result,3)}%")
#     print(f"The Highest Percentage is {max(percentage)}")
                    
                    

# # print(sum_occurence)
# # print(items_list)
# # print(percentage)


#.......... Dictionary Class.............

# my_bio = {"name": "Hammed", "age":"100", "gender":"male"}

# print(my_bio["name"].upper())

# my_bio["course"] = ""   #To add a new key

# print(my_bio.keys())

# print(my_bio["age"])
# print(my_bio.get("age")) #Works as above. And it better because it doenst pust error message when key not found, rather it say none. You can also add a default value eg print(my_bio.get("age","key not found")) 

# del my_bio["age"] #To delete a key in a dict

# #Another way to create a list

# new_dict = dict(
#     (
#         (1,[2,3,"name"]),
#         (2,3),
#         (4,1)
#     )
# )
  

#............Class Assignment............

# question = input("Please pick an option, RISKY or PERFECT:")
# if question == "risky":
#     def risky():
#         file = open("risky.txt", "r")

#         data = file.readlines()
#         risky_dict = {}
#         line_num = 1

#         for line in data:
#             risky_dict[line_num] = line
#             line_num +=1
#         #print(risky_dict)

#         while True:
#             requested_line = int(input("Please what line do you want to listing too: "))
#             print(risky_dict[requested_line])
#     risky()

# elif question == "perfect":
#     def perfect():
#         file = open("perfect.txt", "r")

#         data = file.readlines()
#         perfect_dict = {}
#         line_num = 1

#         for line in data:
#             perfect_dict[line_num] = line
#             line_num +=1
#         #print(perfect_dict)

#         while True:
#             requested_line = int(input("Please what line do you want to listing too: "))
#             print(perfect_dict[requested_line])
#     perfect()


#................Assignment Correction................
# risky = "risky_lyrics"
# perfect = "perfect_lyrics"
# brown = "brown_lyrics"

# file = open(f"{risky}.txt", "r")

# data = file.readlines()
# lyrics_dict = {}
# line_num = 1
# lyrics_dict[risky] = {}

# for line in data:
#     lyrics_dict[risky][line_num] = line
#     line_num +=1
# file.close()

# file = open(f"{brown}.txt", "r")

# data = file.readlines()
# lyrics_dict = {}
# line_num = 1
# lyrics_dict[brown] = {}

# for line in data:
#     lyrics_dict[brown][line_num] = line
#     line_num +=1
# file.close()

# file = open(f"{perfect}.txt", "r")

# data = file.readlines()
# line_num = 1
# lyrics_dict[perfect] = {}

# for line in data:
#     lyrics_dict[perfect][line_num] = line
#     line_num +=1
# file.close()

# print(lyrics_dict.keys())

# while True:
#     requested_song = (input("Please what song would you like to get: "))
#     print(lyrics_dict.keys())
#     requested_line = int(input("Please what line would you like to get: "))

#     print(lyrics_dict[requested_song][requested_line])

#........option 2 ............
# while True:
#     requested_song = (input("Please what song would you like to get: "))
#     print(lyrics_dict.keys())
#     song = lyrics_dict.get(requested_song, "Song does not exist.")

#     if song == "Song does not exist.":
#         print(song)
#         continue

#     requested_line = int(input("Please what line would you like to get: "))
#     print(song[requested_line])


#.....................Working with API and assignment pulling data from an API................

"""
import requests 

url = "http://checklight.pythonanywhere.com/streets"

response = requests.get(url)
data = response.json()

print(data.keys())

print(type(data["streets"]))

streets = data["streets"]



for area in streets:
    #print(street.get("name"), "-", street.get("last_no_light"), "-", street.get("lga"), "-", street.get("status"))
    name = area.get("name")
    lga = area.get("lga")
    print(f"\n",f"----------------------------------------------------","\n",f"New Street Information".center(60),"\n","\n",f"{name}----{lga} lga".center(60),"\n",f"----------------------------------------------------","\n", end = "")
    all_data = area.get("history").get("time_line")
    #all_data_new = area.get 
    for street in all_data:
        average_light_time = area.get("avg_power")
        last_light_off = area.get("last_no_light")
        last_light_on = area.get("last_light")
        
        duration_of_time = round(street.get("period") / 3600, 2)
        light_of = street.get("time")
        nepa_status = "ON (LIGHT UP)" if street.get("status") == 1 else "OFF (BLACK OUT)"
        re_nepa_status = "brought" if street.get("status") == 1 else "took"
        
        print(f"\n",f"Street Name:".ljust(30), "| ", f"{name}","\n",f"LGA:".ljust(30), "| ", f"{lga}","\n",f"Down NEPA(Last date & time):".ljust(30), "| ", f"{last_light_off}","\n",f"Up NEPA(Last date & time):".ljust(30), "| ", f"{last_light_on}","\n",f"Light averagely stay for:".ljust(30), "| ", f"{duration_of_time}hr","\n",f"Current light status:".ljust(30), "| ", f"{nepa_status}. They {re_nepa_status} it on{light_of}","\n", end = "")

"""
    

#......................... Ploting the Graph...................
"""
import requests
import matplotlib.pyplot as plt 

url = "http://checklight.pythonanywhere.com/streets"

response = requests.get(url)
data = response.json()

print(data.keys())

print(type(data["streets"]))

streets = data["streets"]



for area in streets:
    
    all_data = area.get("history").get("time_line")
    
    daily_supply = area.get("history").get("daily_supply")
    print(daily_supply)

    labels = daily_supply["labels"]
    values = daily_supply["values"]

    plt.bar(labels, values)
    plt.title(area.get("name"))
    plt.show()

"""

#............Class Assignment ........................
"""
import requests 

url = "http://checklight.pythonanywhere.com/get_readings/1x0d001/5/"

response = requests.get(url)
data = response.json()

streets = data["streets"]

total = []
for area in streets:
    
    status = area.get("status")
    time = area.get("time")
    
    if status == 0:
            #counting = status.count(item)
        total.append(status)


print(total)

print(len(total))
"""

#...........New Assignment..............
"""
import requests 
device = ["1x0d001","1x0d002","1x0d003","1x0d004"]
device_result = {}

for i in device:

    url = f"http://checklight.pythonanywhere.com/get_readings/{i}/5/"

    response = requests.get(url)
    data = response.json()

    streets = data["streets"]

    days = {}

    for street in streets:
        status = street["status"]
        time = street["time"]
        day = time[5:7]

        if status == 0:
            if day not in days:
                days[day] = 0
            days[day] += 1

    device_result[i] = days
    #print(i, days)
print(device_result)
"""            

#...................Assignment | Working with MAP weather......................
# import citylist
# import requests
# data = citylist.citylist


# user_city = input("Please enter city name : ")
# user_country = input("Please enter country name : ")

# def fetch_id(user_city, user_country, data):
#     city_id = ""

#     for city in data:
#         if city["name"] == user_city and city["country"] == user_country:
#             city_id = city["id"]
#             print(city["name"], city["country"], city["id"], "\n\n\n\n\n")
    
#     return city_id

# id = fetch_id(user_city, user_country, data)
# #print(id)
# api_key = "2b4abe1ddf6cc0ae335b794c5ef3e900"
# url = f"http://api.openweathermap.org/data/2.5/forecast?id={id}&APPID={api_key}"

# r = requests.get(url)
# # print(r.json())
# #file_name = "weather_data.py"

# #file = open(file_name, "w")
# #print(r.json(), file= file)
# print(r.json())
        

















# a = int(input("Enter the value to multiply: "))
# b = int(input("Enter the second value: "))

# print(a * b)

"""
your_name = input("Enter your name: ")

if your_name == "bunmi":
    print(your_name, "is a girl, and she use to be a photographer")
elif your_name == "ola":
    print(your_name, "is a boy and currently a web developer")
else:
    print("You have entered a wrong value")
"""



#...........................Assignemnt .........................
"""
import requests 
import citylist

data = citylist.citylist

user_city = input("Please enter city name : ")


user_country = input("Please enter country name : ")

def fetch_id(user_city, user_country, data):
    city_id = ""

    for city in data:
        if city["name"] == user_city and city["country"] == user_country:
            city_id = city["id"]
            #print(city["name"], city["country"], city["id"], "\n\n")
    
    return city_id

id = fetch_id(user_city, user_country, data)

#print(id)

api_key = "2b4abe1ddf6cc0ae335b794c5ef3e900"

url = f"http://api.openweathermap.org/data/2.5/forecast?id={id}&APPID={api_key}"

response = requests.get(url)
data = response.json()

# city_update = data["list"]
# city_updatee = data["city"]

name = data.get("city").get("name")
country = data.get("city").get("country")
lat = data.get("city").get("coord").get("lat")
lon = data.get("city").get("coord").get("lon")

file = open (f"{user_city}_{user_country}.csv","a")

print("\n", f"City:", f"{name}", "\n", f"Country:", f"{country}", "\n", f"Latitude", f"{lat}", "\n", f"Longitude", f"{lon}", file=file, sep=",")

for i in data.get("list"):
    wind = i.get("wind").get("speed")
    sea_level = i.get("main").get("sea_level")
    #weather = i.get("weather")
    temp = ((i.get("main").get("temp"))-32) * 5/9 
    #dt = i.get("dt")
    weather = i.get("weather")[0].get("main")
    dt_text = i.get("dt_txt")

    # file = open ("newlagos.csv","a")
    # #print("\n",f"...........................","\n",f"Date & Time: {dt_text}".center(26),"\n",f"...........................")
    # print("\n",f"Sea Level".ljust(13),"|", f"{sea_level}".ljust(13), "\n",f"Wind".ljust(13),"|", f"{wind}".ljust(13), "\n",f"Temperature".ljust(13), "|",f"{temp} C".ljust(13),"\n",f"Weather".ljust(13), "|",f"{weather} C".ljust(13), file=file, sep=",")

    
    
    #print("\n",f"...........................","\n",f"Date & Time: {dt_text}".center(26),"\n",f"...........................")
    print("\n",f"Sea Level".ljust(13), f"{sea_level}".ljust(13), "\n",f"Wind".ljust(13), f"{wind}".ljust(13), "\n",f"Temperature".ljust(13), f"{temp} C".ljust(13),"\n",f"Weather".ljust(13), f"{weather} C".ljust(13), file=file, sep=",")

"""
# numbers = [1, 1, 1, 1, 5]

# for number in numbers:
#     output = ""
#     for a in range(number):
#         output += "x"
#     print(output)

# numbers = [1,1,2,2,6,6,8,3,5]
# new_num = []
# for number in numbers:
#     if number not in new_num:
#         new_num.append(number)
# print(new_num)

# x = int(input("Enter your X: "))
# y = int(input("Enter your Y: "))
# def fdivide(x,y):
#     return x / y

# def fmultiply(x,y):
#     return x * y

# def fminus(x,y):
#     return x - y

# def faddition(x,y):
#     return x + y


# add = fdivide(x,y)
# mult = fmultiply(x,y)
# div = fdivide(x,y)
# minus = fminus(x,y)

# print("Addition ",add, "Multiplication ",mult, "Divition ",div, "Minus ",minus)


# def interest(p,r,t):
#     result = (p * r * t) / 100

#     return result


# print(interest(1000,10,5))
# cal = []
# def factorial_iter(n):
#     num = 1
#     while n >= 1:
#         num = num * n
#         cal.append(str(n))
#         n = n -1
        
#     print(" X ".join(cal), "=", num)    
#     print(cal)
#     return num
   



# print(factorial_iter(5))


#.......... Fibonnaci assignment .............
"""
import random
database = []
def Fibonnaci(n):
    while sum(database) < n:
        database.append(random.randint(1, n))

    print(database)

#.............................Check note for complete Fibonnaci assignemnt.

Fibonnaci(20)
"""


#...................Assignment on calculating Variance....................
import random
random_length = 20
list_a = []
list_b = []

def random_number():
    for i in range(random_length):
        ram_a = random.randint(1,20)
        list_a.append(ram_a)
        ram_b = random.randint(1,20)
        list_b.append(ram_b)

        i = i + 1
    

random_number()



def the_mean():
    result_a = sum(list_a) / len(list_a)
    result_b = sum(list_b) / len(list_b)

    
    return result_a, result_b

the_mean()



def the_variance():
    a = []
    b = []
    for item_a in list_a:
        p = (item_a - the_mean()[0]) ** 2 
        a.append(int(p))
        var_result_a = round(sum(a) / (the_mean()[0] - 1),2)

    for item_b in list_b:
        q = (item_b - the_mean()[1]) ** 2 
        b.append(int(q))
        var_result_b = round(sum(b) / (the_mean()[1] - 1),2)

    #return var_result

    print(f"Random Number A: {list_a}")
    print(f"Random Number B: {list_b}")
    print(f"Mean for A: {the_mean()[0]}")
    print(f"Mean for B: {the_mean()[1]}")
    print(f"Variance for A: {var_result_a}")
    print(f"Variance for B: {var_result_b}")


the_variance()