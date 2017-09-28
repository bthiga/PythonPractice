# Challenge 11

# Get a number and determine if it is prime or not.

# Get a number, make it an integer.
# Get everything less than it through 1.
# Divide the number by all the numbers in the list except the number itself and 1.
# If any do not return a remainder then it is a prime.

# the function that actually does the work
def run_prime(final_number):
    # put all numbers less than user number into a list#
    final_list = range(2, (final_number))
    print final_list

    for x in final_list:
        result = float(final_number) / x
        # test = list.append(result)
        if result.is_integer():
            return False
            # print test
    return True
            # print test


# the function that interacts with the user to get a number and use the real function
def get_number(help_text):
    return raw_input(help_text)


# the function that checks if the number if actually an interger by "int-ing" it, and if it is not, running the user through a loop until they get it right.  Using variable arguments for changing up the user prompts when the same method is called multipe times.

def check_number(number):
    try:
        val = int(number)
        print "Thanks for the number... hold please, your call is important to us...\n"
        if run_prime(val) == True:
            print "Yes your number, %s, is a Prime Number" % val
        else:
            print "Nope, your number, %s, is not a Prime" % val

    except ValueError:
      print("\nThat's not an int! Pleases use real numbers only.  That is, REAL numbers from math class.")
      new_number = get_number("Let's try this again, give a REAL number, please.\n")
      check_number(new_number)

number = get_number("Please give me a number and I will tell you if it is prime!\n")
check_number(number)