# *************** AIRTHEMATIC OPERATOR *******************

a = 14
b = 3

print("addition of a and b is ", a+b)

print("substraction of a and b is ", a-b)

print("Mutiple of a and b is ", a*b)

print("Division of a and b is ", a/b)

print("Modules of a and b is ", a%b)

print("Exponents of a and b is ", a**b)

print("Floor division of a and b is ", a//b)


# ************** ASSIGNMENT OPERATOR **********

a = 12
b =10 
a+=5
print(a)
b-=7
print(b)


#  ********** COMPARISION OPERATOR ***********

# x=9
# y=4

# # == Equal

# print(x==y)

# # != Not equal

# print(x!=y)

# #  >   greater than

# print(x>y)

# # < less than

# print(x<y)

# # >=  Greater than equal to

# print(x>=y)

# # <=  Less than equal to

# print(x<=y)


# ****** LOGICAL OPERATOR **********

# a = 12
# b = 7
# c = 14

# #   and : Return TRUE if Both statement are TRUE

# print(a>b and b<c)

# print(a>b and b>c)

# #   or :  Return TRUE if one statement are True

# print(a>b or b>c)

# print(a<b or b>c)

# #   not : Reverse the result , Return True if Staement is FALSE

# print(a>b not b>c)

# print(a<b not b>c) 


## ******************  MEMBERSHIP OPERATOR ****************


# DEF :: ISKA UPYOG HAM SUB_STRING KO MAIN STRING  ME DHUDHNE KE LIYE KARTE HAI

a = "RAJA RAM MOHAN RAI"

# in : Return TRUE if specified value in the object

print("RAJA" in a)

print("RAM CHARI" in a)

# in : Return TRUE if specified value in the object

print("RAM CHARI" not in a)

print("MOHAN" not in a)


#  ********************** IDENTITY OPERATOR ********************

a = 9
b = 8
c = 9

# is : Return TRUE if both variable are the in same object

print(a is c ,  a==c)

print(a is b ,  a!=b)

# is not : REturn  TRUE if Both variable have not same object

print(a is not b , a!= b)

print(a is not c , a!= c)

# ************************ BITWISE OPERATOR **************************

# DEF :  YE HAMESA 0 AND 1 KE ROOP ME HOTA HAI 

a = 12
b = 9
c = 11

#  & : AND  both conddition will be true 

print(a>b & b<c ,", -- if one side is false then retturn :",a>c & c<b)

# | :  "OR" if one side statement is true the return true

print(a>b | b<c ,a>c | c<b)

#   ^ : "XOR" IF COMBINTION IS SAME THEN RETURN false

print(a>b ^ c >a )