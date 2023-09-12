#!/usr/bin/env python3

def happy_new_year():
    # Write a function happy_new_year() using a while 
    # loop that outputs numbers starting at 10 and 
    # counting down to 1. After reaching 1, print 
    # out "Happy New Year!"
    count_down = 10
    while count_down > 0:
        print(count_down)
        count_down -= 1
    print("Happy New Year!")

def square_integers(int_list):
    # code goes here!
    squared_list = [num**2 for num in int_list]
    return squared_list

  

    


def fizzbuzz():
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz") 
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num) 
  
