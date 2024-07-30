#********** TypeCasting ************
# Typecasting, also known as type conversion, is the process of converting a value from one data type to another in Python
#*****Types of Casting*****
# 1. Explicit Conversion  => This is when you manually convert a variable from one type to another type.
# 2. Implicit Conversion  => This happens automatically when Python converts one data type to another type.

#integer to string:
num = 9
num_Str= str(num)
print(num_Str , type(num_Str))

# String to integer:
val = "10"
str_val = int(val)
print(str_val,type(str_val))

# Float to integer
num_float = 123.45
num_int = int(num_float)
print(num_int)  


#String to float
num_str = "123.45"
num_float = float(num_str)
print(num_float)  

#integer to boolean
num = 0
bool_val = bool(num)
print(bool_val)

# boolean to integer
bool_val = True
num = int(bool_val)
print(num)