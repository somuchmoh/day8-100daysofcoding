#Write your code below this line 👇
def prime_checker(number):
    if number % 2 != 0:
        if number % 3 != 0:
            if number % 5 != 0:
                if number % 7 != 0: 
                    print ("It's a prime number.")
                else:
                    print("It's not a prime number.")
            else:
                print("It's not a prime number.")
        else:
            print("It's not a prime number.")
    else:
        print("It's not a prime number.")

#The problem with the above code is that is we do 11 x 13 then it will not give you the wrong answer.

def prime_checker1(number):
    for checker in range (2, number):
        if number % checker == 0:
            is_prime = False
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")


#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker1(number=n)
