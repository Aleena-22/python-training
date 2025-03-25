'''
program to separate the prime numbers form the user input
Notes:
    use input validation

'''

#input

print("This app separate prime numbers from user print")
print('-'*80)

print("Enter your inputs: ")

input_numbers = []  #container for user input number

while True:
    #get the input
    user_input = input()

    # check input for terminating condition
    if(user_input == '!'):
        break

    #validate if it is a dighit and add to container
    if(user_input.isdigit()):
        input_numbers.append(int(user_input))

#process

# find max from list
max_number = max(input_numbers)

#find min from list
min_number = min(input_numbers)

#output

print("maximum from the list is ", max_number)
print("minimum from the list is ", min_number)


