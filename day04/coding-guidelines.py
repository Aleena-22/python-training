'''
program to separate the prime numbers form the user input
Notes:
    use input validation

'''

#input

print("This app separate prime numbers from user print")
print('-'*80)

print("Enter your inputs: ")

#collect the data from user from console
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

#prime number container
primes = []

#go through every number
for num in input_numbers:
    
    #check for 
    for i in range(2, num):
        if(num%i == 0):
            break
    else:
        primes.append(num)

# find max from list
max_number = max(primes)

#find min from list
min_number = min(primes)

#output

print("maximum from the list is ", max_number)
print("minimum from the list is ", min_number)




