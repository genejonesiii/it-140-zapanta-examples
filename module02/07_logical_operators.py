# NAME:     Javier E. Zapanta (j.zapanta@snhu.edu)
# DATE:     15 May 2009
# COURSE:   IT-140
# PROGRAM:  Loan Qualification
#
# PURPOSE:  This program will demonstrate the use of logical operators.
# RUNTIME:  Python 2+
#
# CREDIT:  Gaddis, T. (2012). Starting Out with C++: From Control Structures Through Objects. Pearson Addison-Wesley. Retrieved from https://books.google.com/books?id=Xbt0uQAACAAJ

# Display program heading
print("LOAN QUALIFICATION PROGRAM")
print()                             # Just another way to add an extra line break
print ("Please answer the following questions")
print ("with either Y for Yes or N for No.")

# Get responses to loan qualification questions
employed = input("Are you employed? ")
recent_grad = input("Have you graduated from college in the past two years? ")


# Determine the user's loan qualification
if (employed == 'Y' and recent_grad == 'Y'):
    print("You qualify for the special interest rate.")
else:
    print("You must must be employed and have\ngraduated from college in the\npast two years to qualify.\n")
   