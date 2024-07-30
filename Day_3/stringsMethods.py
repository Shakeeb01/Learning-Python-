# Strings are immutable
# **************** Strings Methods ******************** 
LowerName = "shah"
print(LowerName.upper())  #Converts all characters in the string to uppercase.
UpperName = "SHAH"
print(UpperName.lower()) #Converts all characters in the string to lowercase.


Name = "Shakeeb@ ur Rehman"
print(Name.rstrip("@"))  #Removes trailing characters (whitespace by default).
print(Name.replace("Ronaldo","Shakeeb")) #Returns a string where all occurrences of a substring are replaced with another substring.
print(Name.capitalize())   #Capitalizes the first character of the string.
print(Name.title())         #Converts the first character of each word to uppercase.
print(Name.swapcase())      #Swaps the case of all characters in the string.
print(Name.find("Rehman"))  #Returns the lowest index of the substring if found, otherwise returns -1.
print(Name.index("Rehman"))  #Similar to find() but raises a ValueError if the substring is not found.
print(Name.split())         #Splits the string at the specified separator and returns a list of substrings.
print(Name.splitlines())    #Splits the string at line breaks and returns a list of lines.
s = "-"  
print(s.join(["Shakeeb", "world"]))  #Concatenates the elements of an iterable into a single string with the string as a separator.
print(Name.strip())            #Removes leading and trailing characters (whitespace by default).
print(Name.lstrip())             #Removes leading characters (whitespace by default).
print(Name.startswith("hello"))   #Returns True if the string starts with the specified prefix.
print(Name.endswith("world"))   # Returns True if the string ends with the specified suffix.
print(Name.isalpha())    #Returns True if all characters in the string are alphabetic.
print(Name.isdigit())   #Returns True if all characters in the string are digits.
print(Name.isalnum())  #Returns True if all characters in the string are alphanumeric.
s = "   "
print(s.isspace())  #Returns True if all characters in the string are whitespace.

s = "hello"
print(s.center(10, '-')) #Centers the string in a field of the specified width

s = "hello"
print(s.ljust(10, '-')) #Left-justifies the string in a field of the specified width

s = "hello"
print(s.rjust(10, '-'))  #Right-justifies the string in a field of the specified width