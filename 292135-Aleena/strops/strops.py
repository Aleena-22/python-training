import itertools

def spanSubstrings(s,ss):
    spans = []

    for i in range(len(s) - len(ss) + 1):
        if s[i: i + len(ss)] == ss: # checking whether the substring and index of that is equal
            spans.append((i , i + len(ss))) # adding the result to spans
    return spans

def words_reverse(s):
    words = s.split()
    return ' '.join(words[::-1])

def remove_punctuations(s):
    punctuation = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
    return ''.join(char for char in s if char not in punctuation)

def countWords(s):
    wordList = s.split()
    return len(wordList)

def charMaps(s):
    make_list = list(s)
    return {ch:make_list.count(ch) for ch in make_list}

def makeTitle(s):
    return s.title()

def removeSpaces(s):
    return ' '.join(s.split())

def transform(s):
    trans = s[::-1]
    return trans.swapcase()

def getPermutations(s):
    return [''.join(p) for p in itertools.permutations(s)]

# str1= input("enter the string -> ")
# str2 = input("enter the sub-string -> ")
# res1 = spanSubstrings(str1, str2)

# sentence = input("enter a sentence -> ")
# res2 = words_reverse(sentence)

# puct = input("enter sentence -> ")
# res3 = remove_punctuations(puct)

# str3 = input("enter sentence for counting -> ")
# res4 = countWords(str3)

# str5 = input("enter the word for charMap -> ")
# res5 = charMaps(str5)

# str6 = input("enter the sentence -> ")
# res6 = makeTitle(str6)

# str7 = input("enter the sentence -> ")
# res7 = removeSpaces(str7)

# str8 = input("enter the string -> ")
# res8 = transform(str8)

# str9 = input("enter the string -> ")
# res9 = getPermutations(str9)

# print("Span is -> ",res1)
# print("Reverse of string is -> ", res2)
# print("Sentence after removing -> ", res3)
# print("length of words -> ",res4 )
# print("ouput with the charMap -> ", res5)
# print("output after title -> ", res6)
# print("output after removing spaces -> ", res7)
# print("output after tranforimg -> ", res8)
# print("perumuations of string is -> ", res9)

