#Given an IP address string "192-168-1-1" correct it 
ip = '192-168-1-1'
new_ip = ip.replace('-','.')
print(new_ip)

#Convert "hello world" to uppercase
s = 'hello world'
new_s = s.upper()
print(new_s)

#Swap the case of "PyThOn StRiNgS"
str = "PyThOn StRiNgS"
new_str = str.swapcase()
print(new_str)

# find the length of "Hello, Python!"
l = "Hello, Python!"
print(len(l))

# Count how many times "e" appears in "experience"
e = "experience"
print(e.count('e'))

# Check if "Python programming" starts with "Py"
py = "Python programming"
print(py.startswith('Py'))

# Check if "hello.txt" ends with ".txt"
end = "hello.txt"
print(end.endswith('.txt'))

# Find the index of "world" in "hello world"
idx = "hello world"
print(idx.index('world'))

# Replace "Python" with "Java" in "I love Python"
state = "I love Python"
new_state = state.replace("Python", "Java")
print(new_state)

# Remove leading and trailing spaces from " Python "
st1 = " Python "
new_st1 = st1.strip()
print(new_st1)

# Split "Learn Python Programming" into words
spl = "Learn Python Programming"
print(spl.split())

# Join ['apple', 'banana', 'cherry'] with commas
join = ['apple', 'banana', 'cherry']
new_join = ",".join(join)
print(new_join)

# Check if "Python3" is alphanumeric
p3 = "Python3"
print(p3.isalnum())

# Convert "5" to a 3-digit string ("005")
num = "5"
new_num = num.zfill(3)
print(new_num)

# Given name = "Alice" and age = 25, format "Alice is 25 years old."
name = "Alice"
age = 25
format = "{0} is {1} years old.".format(name, age)
# print(f"{name} is {age} years old)
print(format)

# Check if 'malayalam' is a palindrome

pali = 'malayalam' 
if (pali == pali[::-1]):
    print("palindrome")
else:
    print("not palindrome")

# count no.of vowels
text = input("enter the text: ")
new_text = text.lower()

vowels = ["a","e" ,"i" ,"o" ,"u"]
count = 0

for char in new_text:
    if char in vowels:
        count += 1

print(f"number of vowels is {count}")
