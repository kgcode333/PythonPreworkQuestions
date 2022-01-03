#Kimbreal Griffin
#Python Prework Questions





#Question1:Takes user input
#write a function to print "hello_USERNAME!" USERNAME is the users' input of the function
def hello_name(user_name):
    """print hello_ + user input name"""
    user_input = ("hello_" + user_name.upper())
    return user_input
user_input_name = hello_name(input("Enter your name: "))
print(user_input_name)

#Question1: Username provided
def hello_name(user_name):
    """print 'hello_USERNAME"""
    print("hello_" + user_name.upper())
hello_name('username')








#Question 2
#Print all odd nummbers between 1 and 100
def first_odds():
    """print odd numbers from 1-100"""
    for num in range(1,101):
        if num % 2 != 0:
            print(num)
first_odds()









#Question3
#Return the max number in a given list
def max_num_in_list(a_list):
    """  """
    for num in a_list:
        largest = (a_list)
        return largest
my_list = [2,45,12,22]
print("\nThe largest number in your list is: ")
print(max(my_list))








#Question4
#write a function to to return if given year is a leap year
def is_leap_year(a_year):
    """boolean type leap year """
    leap_year = False
    if a_year % 4 ==0 and a_year % 100 !=0:
        leap_year = True
    elif a_year % 400==0:
        leap_year = True
    else:
        leap_year = False
    return leap_year
leap = int(input("Enter a year to find out if it is a leap year: "))
print(is_leap_year(leap))






#Question5
#Write a function to check if all numbers in a list are consecutive
def is_consecutive(a_list):
    """check if all numbers in a list are consecutive"""
    my_list = .sorted([])
    return my_list
user_list =
#incomplete not really understanding how others have gotten to the solution that works
    



    
    

















