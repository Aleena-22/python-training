import strops as s

s1 = s.spanSubstrings("apple", "pp")
print("span of string -> ",s1)

s2 = s.words_reverse("hi guys good moring")
print("reverse -> ", s2)

s3 = s.remove_punctuations("hi! how are you?")
print("after permutations", s3)

s4 =s.countWords("hi guys")
print("count of words", s4)

s5 = s.charMaps("mississippi")
print("char map -> ", s5)

s6= s.makeTitle("hi guys")
print("making as title -> ", s6)

s7 = s.removeSpaces("hello guys")
print("after removing spaces -> ", s7)

s8 = s.transform("Hello")
print("transforming -> " ,s8)

s9 = s.getPermutations("its")
print("permutations are -> ", s9)
