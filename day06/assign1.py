# Create a function to get the span of substrings

def spanSubstrings(main_str, sub_str):
    count = 0
    spans = []

    for i in range(len(main_str) - len(sub_str) + 1):
        if main_str[i: i + len(sub_str)] == sub_str:
            count = count + 1
            spans.append((i , i + len(sub_str)))
    return count, spans

str1= input("enter the string -> ")
str2 = input("enter the sub-string -> ")
res = spanSubstrings(str1, str2)
print(res)

